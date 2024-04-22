import logging
import inject
from waitress import serve
# CORS

from app.config import PROD_CONFIG
from app import flask_app

from app.core.adapters.sqlalchemy_adapter import DBAdapter
from app.core.interfaces.database import DBInterface
from app.core.adapters.local_fs_adapter import FilestorageAdapter
from app.core.interfaces.filestorage import FilestorageInterface
from app.core.application import Application
from app.core.interfaces.application import BaseApplication


def configure_dependency_injection(
        binder: inject.Binder, file_storage_base_dir: str
):
    binder.bind(DBInterface, DBAdapter())
    binder.bind(FilestorageInterface, FilestorageAdapter(
        base_dir=file_storage_base_dir
    ))
    binder.bind(BaseApplication, Application())


if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(message)s')

    if flask_app.config["ENV"] == PROD_CONFIG.ENV:
        # PROD CONFIG
        logging.basicConfig(level=flask_app.config["LOG_LEVEL"])
        threads = flask_app.config["THREADS"]
        logging.info(f"Starting app in PROD mode with {threads} threads")
        inject.clear_and_configure(
            lambda injector_binding: configure_dependency_injection(
                injector_binding, PROD_CONFIG.FILE_STORAGE
            )
        )
        serve(
            flask_app, host=flask_app.config["APP_HOST"],
            port=flask_app.config["APP_PORT"], threads=threads
        )
    else:
        # TEST and DEV Config
        logging.basicConfig(level=flask_app.config["LOG_LEVEL"])
        inject.clear_and_configure(
            lambda injector_binding: configure_dependency_injection(
                injector_binding, flask_app.config["FILE_STORAGE"]
            )
        )
        flask_app.run(
            host=flask_app.config["APP_HOST"],
            port=flask_app.config["APP_PORT"]
        )
