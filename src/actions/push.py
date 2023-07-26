import sys
import traceback
from src.cli.download import *
from src.client.git import *
from src.common.log4py import *
from src.common.exception import *

xlogger = get_logger()


class PushAction:
	def __init__(self, project_id, branch="master"):
		self.config = self.internal_config
		self.project_id = project_id
		self.branch = branch

	@property
	def internal_config(self):
		return InternalConfig()

	@property
	def gitlab_conn(self):
		git_login_info = {
			"url": self.config.client_info.gitlab.url,
			"sk": self.config.client_info.gitlab.sk,
			"project_id": self.project_id,
			"branch": self.branch,
			"file_path": self.config.client_info.gitlab.parse_filename
		}
		try:
			return GitlabApi(**git_login_info)
		except Exception as e:
			return xlogger.error(str(WebHooksException(WH_GITLAB_ERROR, f'{str(traceback.format_exc())}')))

	@property
	def module_read(self):
		"""
		:return: list
		"""
		try:
			return self.gitlab_conn.get_file_raw_content
		except Exception as e:
			return xlogger.error(str(WebHooksException(WH_READ_ERROR, f'{str(traceback.format_exc())}')))

	def save_to_local(self):
		read_local_pipeline_file = check_file(
			f'{self.config.client_info.module.pipeline_save}/{self.config.client_info.gitlab.parse_filename}')
		if read_local_pipeline_file:
			fmt_module_content = find_list_difference(read_local_pipeline_file, self.module_read)
		else:
			fmt_module_content = self.module_read

		if len(fmt_module_content) == 0:
			return "No modules need to download"
		else:
			download_result = DownloadModule(fmt_module_content).install_packages()

		if download_result is None:
			try:
				write_content_to_file("\n".join(fmt_module_content), f'{self.config.client_info.module.pipeline_save}/{self.config.client_info.gitlab.parse_filename}')
				return f'{self.config.client_info.module.pipeline_save}/{self.config.client_info.gitlab.parse_filename} Update Successful.'
			except Exception as e:
				return xlogger.error(str(WebHooksException(WH_WRITE_ERROR, f'{str(traceback.format_exc())}')))
		else:
			return download_result
