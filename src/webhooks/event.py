import json

from flask import request
from src.common.utility import *

def event_type(data):
	request_data = json.loads(request.data)

	if request_data.get("object_kind"):
		if request_data['object_kind'] == 'push':
			request_data_fmt = Dict2Obj(request_data)
			print (request_data_fmt.tag)
			print(request_data_fmt.repository.git_http_url)
			print(request_data_fmt.repository.git_ssh_url)
		elif request_data['object_kind'] == 'merge_request':
			print('Merge request event received')
		else:
			return 'Unknown event received'
	else:
		return f'object_kind key is no exists with {request_data}'
