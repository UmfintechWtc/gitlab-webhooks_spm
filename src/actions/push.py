from src.cli.download import *
from src.client.git import *
from src.common.exception import *
from src.common.log4py import *

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
			err_module, ok_module = DownloadModule(fmt_module_content).install_packages()

		if len(err_module) == 0:
			try:
				write_content_to_file("\n".join(ok_module),
									  f'{self.config.client_info.module.pipeline_save}/{self.config.client_info.gitlab.parse_filename}')
				xlogger.info(f'module {ok_module} Download successfully.')
				return f'{ok_module} Download successfully.' + "\n"
			except Exception as e:
				xlogger.error(str(WebHooksException(WH_WRITE_ERROR, f'{str(traceback.format_exc())}')))
		elif len(err_module) > 0:
			if len(ok_module) > 0:
				try:
					write_content_to_file("\n".join(ok_module),
										  f'{self.config.client_info.module.pipeline_save}/{self.config.client_info.gitlab.parse_filename}')
					xlogger.info(f'module download successfully. {ok_module}')
					xlogger.info(f'module download failed. {err_module}')
					return f'download successfully. {ok_module}\ndownload failed. {err_module}\n'
				except Exception as e:
					xlogger.error(str(WebHooksException(WH_WRITE_ERROR, f'{str(traceback.format_exc())}')))
			else:
				xlogger.error(f'module download Failed. {err_module}')
				return f'download Failed. {err_module}\n'
