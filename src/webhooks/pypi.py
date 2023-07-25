from flask import Flask, request

import event
from src.config.internal_config import InternalConfig

app_pypi = Flask(__name__)

config = InternalConfig()


@app_pypi.route(f"/{config.client_info.base_url}/{config.client_info.webhooks.url_suffix}", methods=['POST'])
def pypi():
	webhooks_handler_result = event.event_type(request.data)
	return webhooks_handler_result, 200
