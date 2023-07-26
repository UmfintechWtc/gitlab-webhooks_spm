from flask import Flask, request
from src.config.internal_config import InternalConfig
from src.webhooks.event import event_type

app_pypi = Flask(__name__)

config = InternalConfig()


@app_pypi.route(f"/{config.client_info.base_url}/{config.client_info.webhooks.url_suffix}", methods=['POST','GET'])
def pypi():
	webhooks_handler_result, status_code = event_type(request.data)
	return webhooks_handler_result, status_code
