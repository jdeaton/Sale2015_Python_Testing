# This file contains some of the useful methods in unit testing described in
# Chapter 2.

import unittest


class TestExamples(unittest.TestCase):

    # Tests for equality or almost equality of values.
    def test_assert_equal(self):
        self.assertEqual(1, 1)

    def test_assert_almost_equal(self):
        self.assertAlmostEqual(1, 1.2, delta=0.5)
        self.assertAlmostEqual(1, 1.001, places=2)

    # Tests on purely boolean values.
    def test_assert_true(self):
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue("Hello, World!")

    def test_assert_false(self):
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse(None)

    # Relative/comparative tests on values.
    def test_assert_greater(self):
        self.assertGreater(2, 1)

    def test_assert_greater_equal(self):
        self.assertGreaterEqual(2, 2)

    def test_assert_less(self):
        self.assertLess(1, 2)

    def test_assert_less_equal(self):
        self.assertLessEqual(1, 2)

    # Tests on dictionaries.
    def test_assert_dict_contains_subset(self):
        expected = {'a': 'b'}
        actual = {'a': 'b',
                  'c': 'd',
                  'e': 'f'}
        self.assertDictContainsSubset(expected, actual)

    def test_assert_dict_equal(self):
        expected = {'a': 'b',
                    'c': 'd'}
        actual = {'a': 'b',
                  'c': 'f'}
        self.assertDictEqual(expected, actual)

    # Tests if two objects are identical (or not identical).
    def test_assert_is(self):
        self.assertIs("a", "a")

    def test_assert_is_not(self):
        self.assertIsNot("a", "b")

    # Test if an object is an instance of a class (or not an instance).
    def test_is_instance(self):
        self.assertIsInstance(1, int)

    def test_is_not_instance(self):
        self.assertNotIsInstance(1, str)

    # Test for None values (or not None values).
    def test_assert_is_none(self):
        self.assertIsNone(None)

    def test_assert_is_not_none(self):
        self.assertIsNotNone(1)

    # Tests on lists.
    def test_assert_in(self):
        self.assertIn(1, [1, 2, 3])

    def test_assert_items_equal(self):
        self.assertItemsEqual([1, 2, 3], [2, 3, 1])

    # Tests for checking that proper exceptions are raised.
    def test_assertRaises(self):
        self.assertRaises(ValueError, int, "A")

    def test_assert_raises_2(self):
        self.assertRaises(IndexError, [].pop, 0)

    def test_assert_raises_alternative(self):
        with self.assertRaises(AttributeError):
            [].get