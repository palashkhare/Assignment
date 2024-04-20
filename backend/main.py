import argparse
import logging

from waitress import serve
# CORS

from app.config import BASE_CONFIG, TEST_CONFIG, PROD_CONFIG

from app import flask_app


if __name__=="__main__":

    logger = logging.getLogger(__name__)

    if flask_app.config["ENV"] == PROD_CONFIG.ENV:
        # PROD CONFIG
        logging.basicConfig(level=flask_app.config["LOG_LEVEL"])
        threads = flask_app.config["THREADS"]
        logging.info(f"Starting app in PROD mode with {threads} threads")
        serve(flask_app,host=flask_app.config["APP_HOST"], port=flask_app.config["APP_PORT"], threads=threads)
    else:
        # TEST and DEV Config
        logging.basicConfig(level=flask_app.config["LOG_LEVEL"])
        flask_app.run(host=flask_app.config["APP_HOST"], port=flask_app.config["APP_PORT"])
    