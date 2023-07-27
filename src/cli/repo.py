import asyncio
import time
import traceback

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from src.common.exception import *
from src.common.log4py import *
from src.common.utility import *
from src.config.internal_config import InternalConfig

xlogger = get_logger()


class PyPIEventHandler(FileSystemEventHandler):
	def __init__(self, pypi_save_path):
		self.pypi_save_path = pypi_save_path

	def on_any_event(self, event):
		if event.is_directory:
			return

		update_index_cmd = f"dir2pi {self.pypi_save_path}"
		process = await asyncio.create_subprocess_shell(update_index_cmd)
		await process.communicate()
		xlogger.info(f"{self.pypi_save_path} 已更新[{update_index_cmd}]")


class RepoInit:
	def __init__(self):
		self.event_handler = None
		self.observer = Observer()
		self.config = self.internal_config

	@property
	def internal_config(self):
		return InternalConfig()

	async def update_index(self):
		pypi_save_path = self.config.client_info.module.package_path
		self.event_handler = PyPIEventHandler(pypi_save_path)
		self.observer.schedule(self.event_handler, pypi_save_path, recursive=True)
		xlogger.info(f"开始监听目录：{pypi_save_path}")
		try:
			while True:
				await asyncio.sleep(1)
		except Exception as e:
			xlogger.error(str(WebHooksException(WH_SHELL_ERROR, f'{str(traceback.format_exc())}')))
		finally:
			self.observer.stop()
			self.observer.join()


	async def main(self):
		repo_init = RepoInit()
		await repo_init.update_index()
