from flask import Flask
from src.cli.repo import *
from src.config.internal_config import InternalConfig

app_pkg = Flask(__name__)

config = InternalConfig()


@app_pkg.route("/mnt/pypi", methods=['GET'])
def pkg():
	return "pkg", 200
