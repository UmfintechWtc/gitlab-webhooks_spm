from flask import Flask

from src.config.internal_config import *

app_pypi = Flask(__name__)

config = InternalConfig()


@app_pypi.route(f"/{config.client_info.base_url}/{config.client_info.webhooks.url_suffix}", methods=['GET'])
def pypi():
	print(f"/{config.client_info.base_url}/{config.client_info.webhooks.url_suffix}")
	return "pypi", 200

