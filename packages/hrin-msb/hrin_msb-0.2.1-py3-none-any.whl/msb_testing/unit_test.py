from ._core import (TestCase,TestConfig, LiveServerThreadWithReuse)


class UnitTest(TestCase):
	port = 8000
	server_thread_class = LiveServerThreadWithReuse

	def setUp(self) -> None:
		"""
		 implement this
		"""
		pass

	@property
	def config(self):
		return TestConfig()
