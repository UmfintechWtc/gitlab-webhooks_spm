import json
from flask import request


def event_type(data):
	request_data = json.loads(request.data)
	if request_data.get("object_kind"):
		if request_data['object_kind'] == 'push':
			print('Push event received')
		elif request_data['object_kind'] == 'merge_request':
			print('Merge request event received')
		else:
			return 'Unknown event received'
	else:
		return f'object_kind key is no exists with {request_data}'
