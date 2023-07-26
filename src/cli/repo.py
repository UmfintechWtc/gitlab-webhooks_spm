from src.common.utility import *

class RepoInit:

	def update_index(self, config):
		pypi_save_path = config.client_info.module.package_path
		update_index_cmd = f"dir2pi {pypi_save_path}"
		exec_cmd(update_index_cmd)