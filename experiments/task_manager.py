# import colorama
# TODO: do not forget this module

class Task:
	def __init__(self, name: str, thread_type: str, state: str):
		self.name = name
		self.thread_type = thread_type
		self.state = state


class TaskManager:
	thread_pool: dict

	colour_config = {
		"state": {"idle": "yellow"
			, "active": "green"
			, "broken": "red"},
		"thread_type": {"daemon thread"}
	}

	def __init__(self):
		self.thread_pool = {}

	def task_manager(self):
		while True:
			for thread in self.thread_pool:
				thread.get_state()
