import unittest

from ._core import (TestConfig, LiveServerThreadWithReuse)


class PyhonUnitTest(unittest.TestCase):
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
