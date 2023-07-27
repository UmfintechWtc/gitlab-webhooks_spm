import time
import traceback

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from src.common.exception import *
from src.common.log4py import *
from src.common.utility import *
from src.config.internal_config import InternalConfig

xlogger = get_logger()


class RepoInit:

	def __init__(self):
		self.config = self.internal_config

	@property
	def internal_config(self):
		return InternalConfig()

	def update_index(self):
		pypi_save_path = self.config.client_info.module.package_path
		update_index_cmd = f"dir2pi {pypi_save_path}"
		try:
			exec_cmd(update_index_cmd, False)
			xlogger.info(f'Update Simple Index Successfully, {pypi_save_path}')
		except Exception as e:
			xlogger.error(
				str(WebHooksException(WH_INDEX_UPDATE, f'{update_index_cmd} - {str(traceback.format_exc())}')))


class PyModuleHandler(FileSystemEventHandler):
	def __init__(self, repo_init: RepoInit):
		self.repo_init = repo_init

	def on_created(self, event):
		if not event.is_directory:
			self.repo_init.update_index()


class CronTask(RepoInit):
	def __init__(self):
		super().__init__()

	@property
	def create_event_handler(self):
		event_handler = PyModuleHandler(RepoInit())
		return event_handler

	@property
	def create_observer_handler(self):
		observer = Observer()
		observer.schedule(self.create_event_handler, self.config.client_info.module.package_path, recursive=False)
		return observer

	def observer_scheduler(self):
		self.create_observer_handler.start()
		try:
			while True:
				time.sleep(1)
		except Exception as e:
			self.create_observer_handler.stop()
			xlogger.error(
				str(WebHooksException(WH_INDEX_UPDATE, f'observer - {str(traceback.format_exc())}')))

		self.create_observer_handler.join()


def create_observer_handler():
	task = CronTask()
	return task.observer_scheduler()
