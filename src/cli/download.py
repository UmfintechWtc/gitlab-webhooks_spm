import concurrent.futures
import sys
import traceback

from src.common.exception import *
from src.common.log4py import *
from src.common.utility import *
from src.config.internal_config import InternalConfig

xlogger = get_logger()

class DownloadModule:
	def __init__(self, packages):
		self.config = self.internal_config
		self.module = packages

	@property
	def internal_config(self):
		return InternalConfig()

	def install_package_cmd(self, package):
		download_pip_pkg_cmd = f"mppm download -m {package} -d {self.config.client_info.module.package_path}"
		exec_cmd(download_pip_pkg_cmd)

	def install_packages(self):
		with concurrent.futures.ThreadPoolExecutor(max_workers=self.config.performance.max_workers, thread_name_prefix="module") as executor:
			futures = [executor.submit(self.install_package_cmd, package) for package in self.module]
			for task in concurrent.futures.as_completed(futures):
				try:
					task.result()
				except Exception as e:
					xlogger.error(str(WebHooksException(WH_SHELL_ERROR, f'{str(traceback.format_exc())}')))
					sys.exit(WH_SHELL_ERROR)
