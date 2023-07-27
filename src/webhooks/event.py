import json

from flask import request

from src.actions.push import *


def event_type(data):
	request_data = Dict2Obj(json.loads(request.data))
	if request_data.object_kind:
		if request_data.object_kind == 'push':
			handler_res = PushAction(request_data.project.id, request_data.project.default_branch).save_to_local()
			return handler_res, 200
		elif request_data.object_kind == 'merge_request':
			return 'merge_request event received', 200
		else:
			return 'Unknown event received', 500
	else:
		return f'object_kind key is no exists with {request_data}'
