from src.webhooks.config import app_config
from src.webhooks.pkg import app_pkg
from src.webhooks.pypi import app_pypi
from src.config.internal_config import InternalConfig

if __name__ == '__main__':
	config = InternalConfig()
	app_config.run(host=f"{config.client_info.config.host}", port=int(f"{config.client_info.config.port}"))
	app_pkg.run(host=f"{config.client_info.repo.host}", port=int(f"{config.client_info.repo.port}"))
	app_pypi.run(host=f"{config.client_info.webhooks.host}", port=int(f"{config.client_info.webhooks.port}"))