from flask import Flask

from src.config.internal_config import *

app_pkg = Flask(__name__)

config = InternalConfig()


@app_pkg.route(f"/{config.client_info.base_url}/{config.client_info.repo.url_suffix}", methods=['GET'])
def pkg():
	print(f"/{config.client_info.base_url}/{config.client_info.repo.url_suffix}")
	return "pkg", 200