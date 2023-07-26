from flask import Flask
from src.cli.repo import *
from src.config.internal_config import InternalConfig

app_pkg = Flask(__name__)

config = InternalConfig()


@app_pkg.route(f"/{config.client_info.base_url}/{config.client_info.repo.url_suffix}", methods=['GET'])
def pkg():
	RepoInit().update_index()
	return "pkg", 200