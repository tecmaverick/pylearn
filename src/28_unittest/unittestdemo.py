import unittest

class Calc(unittest.TestCase):
	def setUp(self):
		print "setup phase"

	def tearDown(self):
		print "teardown"

	def getHello(self):
		return "Hello"

	def test_add(self):
		print "Hello test"
		self.assertEqual(self.getHello(),"Hello")
unittest.main()
