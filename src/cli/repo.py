from src.config.internal_config import InternalConfig
from src.common.utility import *

class RepoInit:
	def __init__(self):
		self.config = self.internal_config

	@property
	def internal_config(self):
		return InternalConfig

	def update_index(self):
		# pypi_save_path = self.config.client_info.module.package_path
		update_index_cmd = f"dir2pi /mnt/pypi"
		exec_cmd(update_index_cmd)