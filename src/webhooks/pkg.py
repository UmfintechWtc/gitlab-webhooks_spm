import traceback

from flask import Flask, send_from_directory

from src.cli.repo import *
from src.common.exception import *
from src.common.log4py import *
from src.config.internal_config import InternalConfig

app_pkg = Flask(__name__)

config = InternalConfig()

xlogger = get_logger()

RepoInit().update_index(config)


@app_pkg.route('/simple/')
def simple_index():
	simple_index_path = f'{config.client_info.module.package_path}/simple/'
	try:
		return send_from_directory(f'{simple_index_path}', f'{config.client_info.module.simple_index_name}')
	except Exception as e:
		xlogger.error(str(WebHooksException(WH_SIMPLE_INDEX, f'{simple_index_path} - {str(traceback.format_exc())}')))
		return f'{simple_index_path} Page not found', 404


@app_pkg.route('/simple/<package_name>/')
def simple_package_index(package_name):
	package_index_file = f'{config.client_info.module.package_path}/simple/{package_name}'
	try:
		return send_from_directory(package_index_file, f'{config.client_info.module.simple_index_name}')
	except Exception as e:
		xlogger.error(str(WebHooksException(WH_SIMPLE_INDEX, f'{package_index_file} - {str(traceback.format_exc())}')))
		return f'{package_index_file}/{config.client_info.module.simple_index_name} Page not found', 404


@app_pkg.route('/simple/<package_name>/<filename>')
def download_file(package_name, filename):
	package_directory = f'{config.client_info.module.package_path}/simple/{package_name}'
	try:
		return send_from_directory(package_directory, filename, as_attachment=True)
	except Exception as e:
		xlogger.error(str(WebHooksException(WH_DOWNLOAD_ERROR, f'{package_directory}/{filename} - {str(traceback.format_exc())}')))
		return f'{package_directory}/{filename} module not found', 404
