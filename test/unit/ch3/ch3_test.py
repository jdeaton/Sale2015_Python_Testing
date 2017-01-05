import unittest
from ch2.calculate import Calculate

class Ch3TestExamples(unittest.TestCase):

    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        print 'Hello'
        self.assertEqual(4, self.calc.add("Hello", "World"))
        self.assertAlmostEquals(1, 1)