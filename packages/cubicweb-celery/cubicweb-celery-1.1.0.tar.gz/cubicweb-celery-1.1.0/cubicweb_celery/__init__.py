"""cubicweb-celery application package

Celery integration with CubicWeb
"""

import contextlib
import logging
import os.path as osp

from celery import Celery, Task
from celery import signals

from click import Option

from cubicweb.cwconfig import CubicWebConfiguration as cwcfg
from cubicweb.cwvreg import CWRegistryStore
from cubicweb.server.session import Connection

log = logging.getLogger(__name__)


@contextlib.contextmanager
def new_user_cnx(repo, user):
    with Connection(repo, user) as cnx:
        yield cnx


class CWTask(Task):
    abstract = True

    @contextlib.contextmanager
    def _cnx(self, user=None):
        if user == -1:
            user = None
        with self.app.cwrepo.internal_cnx() as cnx:
            if user is not None:
                if not hasattr(user, "eid"):
                    user = cnx.entity_from_eid(user)
                with new_user_cnx(cnx.repo, user) as user_cnx:
                    yield user_cnx
            else:
                yield cnx

    @contextlib.contextmanager
    def cnx(self, user=None, atomic=True):
        """context manager that provide an connection as the specified user"""
        with self._cnx(user=user) as cnx:
            if atomic:
                try:
                    yield cnx
                except Exception:
                    cnx.rollback()
                    raise
                else:
                    cnx.commit()
            else:
                yield cnx


class CWCelery(Celery):
    task_cls = "cubicweb_celery:CWTask"

    defaults = {
        "task_serializer": "json",
        "result_serializer": "json",
        "enable_utc": True,
    }

    conf_freezed = False

    def freeze_conf(self):
        self.conf_freezed = True
        self.dummy_conf = dict(self.conf)

    @property
    def cubes_conf(self):
        if self.conf_freezed:
            return self.dummy_conf
        else:
            return self.conf

    def setup_cw(self, cwconfig):
        self.cwconfig = cwconfig

        celery_config = self.defaults.copy()
        if cwconfig.mode == "test":
            celery_config["task_always_eager"] = True
            celery_config["task_eager_propagates"] = True

        if self.conf_freezed:
            return

        if cwconfig.apphome is not None:
            fpath = osp.join(cwconfig.apphome, "celeryconfig.py")
            if osp.isfile(fpath):
                with open(fpath, "rb") as fobj:
                    exec(fobj.read(), celery_config)
        self.config_from_object(celery_config)

    def cwtask(self, *args, **opts):
        opts.setdefault("bind", True)
        if len(args) == 1:
            return self.task(**opts)(args[0])
        return self.task(*args, **opts)


app = CWCelery()

options = [
    Option(
        ("-i", "--instance"),
        prompt=True,
        prompt_required=True,
        help="Cubicweb instance name.",
    ),
    Option(("--debug",), default=False, help="Enable cubicweb debug mode."),
]

for option in options:
    app.user_options["preload"].add(option)

user_options = {}


def init_repo(cwconfig):
    # We do NOT want cubicweb to mess with logging because celery is already
    # doing acrobatic things with it.
    vreg = CWRegistryStore(cwconfig, initlog=False)
    return cwconfig.repository(vreg)


@signals.user_preload_options.connect
def on_preload_parsed(options, **kwargs):
    global user_options
    user_options.update({"instance": options["instance"], "debug": options["debug"]})
    cwconfig = cwcfg.config_for(
        user_options["instance"], debugmode=user_options["debug"]
    )

    # load the repo
    repo = app.cwrepo = init_repo(cwconfig)
    # make sure the 'celery' cube is loaded. The cube has taken care of
    # setting up the app.
    # Any cube depending on the celery cube may update the configuration
    # in its registration callback.
    if "celery" not in repo.get_cubes():
        raise ValueError("The 'celery' cube must be installed in the instance")


@signals.worker_process_init.connect
def on_worker_process_init(**kw):
    # Use a fresh new repository to avoid sharing anything with the forked one.

    global user_options
    cwconfig = cwcfg.config_for(
        user_options["instance"], debugmode=user_options["debug"]
    )

    # Prevent cubes from modifying the configuration
    app.freeze_conf()
    repo = app.cwrepo = init_repo(cwconfig)
    repo.hm.call_hooks("server_startup", repo=repo)
