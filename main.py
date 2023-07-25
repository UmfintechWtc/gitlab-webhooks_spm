import json

from flask import Flask
from src.config.internal_config import *
from src.webhooks.event import *

app = Flask(__name__)

config = InternalConfig()

# @app.route('/pypi', methods=['POST'])
# def gitlab_webhook():
# 	request_data = json.loads(request.data)
# 	rsp_data = event_type(request_data)
# 	return 'OK', 200

# @app.route(f"/{config.client_info.base_url}/{config.client_info.webhooks.url_suffix}", methods=['GET'])

@app.route(f"/{config.client_info.base_url}/{config.client_info.webhooks.url_suffix}", methods=['GET'])
def parse_config():
	res = InternalConfig()
	print (res)
	return "ok", 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
