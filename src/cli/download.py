from src.common.utility import *
from src.config.internal_config import InternalConfig
class DownloadModule:
	def __init__(self):
		self.config = self.__config

	@property
	def __config(self):
		return InternalConfig()

	def download(self):
		pass