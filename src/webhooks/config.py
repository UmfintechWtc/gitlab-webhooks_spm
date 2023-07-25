from flask import Flask

from src.config.internal_config import *

app_config = Flask(__name__)

config = InternalConfig()


@app_config.route(f"/{config.client_info.base_url}/{config.client_info.config.url_suffix}", methods=['GET'])
def parse_config():
	"""
		for test
	"""
	print(config)
	return "config", 200