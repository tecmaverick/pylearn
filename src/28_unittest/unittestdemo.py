import unittest

class Calc(unittest.TestCase):
	def setUp(self):
		print "setup phase"

	def tearDown(self):
		print "teardown"

	def exceptionDemo(self):
		raise ValueError

	def getHello(self):
		return "Hello"

	def test_add(self):
		print "Hello test"
		self.assertEqual(self.getHello(),"Hello")

	def test_raise_err(self):
		with self.assertRaises(ValueError):
			self.exceptionDemo()

unittest.main()
