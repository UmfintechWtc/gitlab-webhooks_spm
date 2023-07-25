import base64
import gitlab
from src.common.const import *
from src.config.internal_config import InternalConfig


class GitlabApi(object):
	def __init__(self, url: str, sk: str, project_id: str, file_path: str, branch="master", timeout=60):
		self.id = project_id
		self.branch = branch
		self.url = url
		self.token = base64.b64decode(sk.encode("utf-8")).decode("utf-8")
		self.timeout = timeout
		self.file_path = file_path
		self.config = self.internal_config
		self.conn = gitlab.Gitlab(self.url, self.token)
		self.projects = self.conn.projects.get(self.id, self.timeout)

	@property
	def internal_config(self):
		return InternalConfig()

	def check_dir_exists(self, check_path, check_branch):
		pass

	@property
	def get_file_raw_content(self):
		"""
		:return: module list
		"""
		content = self.projects.files.get(file_path=f'{self.file_path}', ref=self.branch)
		return content.decode().decode("utf8").split("\n")

	def pull(self, project_url, project_branch, project_save_path):
		pass

	def delete(self, commit_message):
		pass

	def push(self, commit_message):
		pass
