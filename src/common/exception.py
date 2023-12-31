############################ 异常定义
WH_UNEXPECTED_ERROR = 'WH-99999'
WH_CONFIG_ERROR = 'WH-00001'
WH_DOWNLOAD_ERROR = 'WH-00002'
WH_INDEX_ERROR = 'WH-00003'
WH_GITLAB_ERROR = 'WH-00004'
WH_READ_ERROR = 'WH-00005'
WH_WRITE_ERROR = 'WH-00006'
WH_SHELL_ERROR = 'WH-00007'
WH_SIMPLE_INDEX = 'WH-00008'
WH_INDEX_UPDATE = 'WH-00009'

_exception_definition = {
	WH_UNEXPECTED_ERROR: '未知异常',
	WH_CONFIG_ERROR: '配置文件解析异常',
	WH_DOWNLOAD_ERROR: '模块下载异常',
	WH_INDEX_ERROR: '仓库更新元数据异常',
	WH_GITLAB_ERROR: '调用GITLAB SDK异常',
	WH_READ_ERROR: '读文件异常',
	WH_WRITE_ERROR: '写文件异常',
	WH_SHELL_ERROR: '执行SHELL CLI异常',
	WH_SIMPLE_INDEX: 'pypi仓库索引文件不存在',
	WH_INDEX_UPDATE: 'pypi仓库索引更新异常'

}

loc = locals()


def _get_variable_name(variable):
	for k, v in loc.items():
		if loc[k] == variable:
			return k
	return ""


class WebHooksException(Exception):

	def __init__(self, code, context_msg=""):
		self.code = code
		self.code_description = _exception_definition.get(code, "异常编码: " + str(code))
		self.message = context_msg
		super().__init__(self.message)

	def __str__(self):
		code_name = _get_variable_name(self.code)
		return '#' * 120 + f'\n{self.code} [{code_name}] -> {self.code_description}\n\n {self.message}\n\n' + '#' * 120


if __name__ == "__main__":
	print(_exception_definition)
