from src.common.const import *
from src.common.utility import *
from src.cli.download import *
from src.config.internal_config import InternalConfig
from src.client.git import *


class PushAction:
	def __init__(self, project_id, branch="master"):
		self.config = InternalConfig
		self.project_id = project_id
		self.branch = branch
		self.gitlab = self.gitlab_conn

	@property
	def internal_config(self):
		return InternalConfig()

	@property
	def gitlab_conn(self):
		git_login_info = {
			"url": self.config.client_info.gitlab.url,
			"sk": self.config.client_info.gitlab.url,
			"project_id": self.project_id,
			"branch": self.branch,
			"file_path": self.config.client_info.gitlab.parse_filename
		}
		return GitlabApi(**git_login_info)

	@property
	def module_read(self):
		return self.gitlab_conn.get_file_raw_content

	def save_to_local(self):
		read_local_pipeline_file = check_file(self.config.client_info.module.pipeline_save)
		if read_local_pipeline_file:
			fmt_module_content = find_list_difference(read_local_pipeline_file, self.module_read)
		else:
			fmt_module_content = "\n".join(read_local_pipeline_file)

		return fmt_module_content

