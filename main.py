from src.webhooks.config import app_config
from src.webhooks.pkg import app_pkg
from src.webhooks.pypi import app_pypi
from src.config.internal_config import InternalConfig
from src.common.utility import *
from src.cli.repo import *
import concurrent.futures

if __name__ == '__main__':
	config = InternalConfig()
	create_dir(config.client_info.module.pipeline_save)
	create_dir(config.client_info.module.package_path)
	RepoInit().update_index()
	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
		pool.submit(app_config.run, host=config.client_info.config.host, port=int(config.client_info.config.port))
		pool.submit(app_pkg.run, host=config.client_info.repo.host, port=int(config.client_info.repo.port))
		pool.submit(app_pypi.run, host=config.client_info.webhooks.host, port=int(config.client_info.webhooks.port))