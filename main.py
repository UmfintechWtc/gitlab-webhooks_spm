import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/pypi', methods=['POST'])
def gitlab_webhook():
    request_data = json.loads(request.data)
    if 'object_kind' in data and data['object_kind'] == 'push':
        # Handle push event
        print('Push event received')
        # TODO: Add your code to handle push event here
    elif 'object_kind' in data and data['object_kind'] == 'merge_request':
        # Handle merge request event
        print('Merge request event received')
        # TODO: Add your code to handle merge request event here
    else:
        # Handle other events
        print('Unknown event received')
        # TODO: Add your code to handle other events here
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
