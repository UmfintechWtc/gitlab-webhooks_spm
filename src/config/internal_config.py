import sys
import yaml
import traceback
import collections
from src.common.exception import *
from src.common.log4py import *
from src.common.utility import *

xlogger = get_logger()


class InternalConfig(Dict2Obj):
	def __init__(self, filepath=SOURCE_INTERNAL_CONFIG):
		try:
			self.data = collections.defaultdict(dict)
			data = yaml.safe_load(open(filepath, "r", encoding='utf-8'))
			self.data.update(data)

			super().__init__(self.data)

		except Exception as e:
			xlogger.error(str(WebHooksException(WH_CONFIG_ERROR, f'{str(traceback.format_exc())}')))
			sys.exit(WH_CONFIG_ERROR)
