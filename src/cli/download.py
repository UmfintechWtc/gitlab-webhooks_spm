import concurrent.futures
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
		download_pip_pkg_cmd = f"mppm download -m {package} -o {self.config.client_info.module.package_path}"
		return exec_cmd(download_pip_pkg_cmd, True), package

	def install_packages(self):
		failed_module = []
		with concurrent.futures.ThreadPoolExecutor(max_workers=self.config.performance.max_workers,
												   thread_name_prefix="module") as executor:
			futures = [executor.submit(self.install_package_cmd, package) for package in self.module]
			for task in concurrent.futures.as_completed(futures):
				try:
					result = task.result()
					if self.config.client_info.ignore_black_key_words.mppm in result[0]:
						failed_module.append(result[1])
				except Exception as e:
					xlogger.error(str(WebHooksException(WH_SHELL_ERROR, f'{str(traceback.format_exc())}')))
		for err_module in failed_module:
			self.module.remove(err_module)
		return failed_module, self.module
