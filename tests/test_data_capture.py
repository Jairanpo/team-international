# Standard library:
import unittest
# -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Third party:
# -- -- -- -- -- -- -- -- -- -- -- -- -- --
# project:
from data_capture import DataCapture
# =============================================================================


class TestDataCapture(unittest.TestCase):

    def test_add_values(self):
        dc = DataCapture()
        dc.add(1)
        dc.add(2)
        self.assertEqual(len(dc.values), 2)

    def test_using_wrong_amount_of_arguments(self):
        capture = DataCapture()

        with self.assertRaises(Exception) as context:
            capture.add()

        self.assertTrue('add' in str(context.exception))

        amount_of_values = 10
        # Create samples from 1 to 10
        for n in range(1, amount_of_values + 1):
            capture.add(n)

        stats = capture.build_stats()
        with self.assertRaises(Exception) as context:
            stats.less()
        self.assertTrue('less' in str(context.exception))

        with self.assertRaises(Exception) as context:
            stats.greater(3, 5, 5)
        self.assertTrue('greater' in str(context.exception))

        with self.assertRaises(Exception) as context:
            stats.between(1, 2, 3)

        self.assertTrue('between' in str(context.exception))

    def test_using_wrong_data_type_arguments(self):
        capture = DataCapture()

        with self.assertRaises(Exception) as context:
            capture.add('a')
        self.assertTrue('add' in str(context.exception))

        amount_of_values = 10
        # Create samples from 1 to 10
        for n in range(1, amount_of_values + 1):
            capture.add(n)

        stats = capture.build_stats()
        with self.assertRaises(Exception) as context:
            stats.less('a')
        self.assertTrue('less' in str(context.exception))

        with self.assertRaises(Exception) as context:
            stats.greater('a')
        self.assertTrue('greater' in str(context.exception))

        with self.assertRaises(Exception) as context:
            stats.between('a', 'b')

        self.assertTrue('between' in str(context.exception))

    def test_less_values(self):
        capture = DataCapture()
        amount_of_values = 10
        for n in range(amount_of_values):
            capture.add(n)

        stats = capture.build_stats()

        self.assertEqual(len(stats.less(3)), 3)

    def test_greater_values(self):
        capture = DataCapture()
        amount_of_values = 10
        sample = 3
        # Create samples from 1 to 10
        for n in range(1, amount_of_values + 1):
            capture.add(n)

        stats = capture.build_stats()
        self.assertEqual(
            len(stats.greater(sample)),
            amount_of_values - sample
        )

    def test_between_values(self):
        capture = DataCapture()

        amount_of_values = 10
        # Create samples from 1 to 10
        for n in range(1, amount_of_values + 1):
            capture.add(n)
        stats = capture.build_stats()

        self.assertEqual(len(stats.between(1, 10)), 10)
        self.assertEqual(len(stats.between(1, 8)), 8)
        self.assertEqual(len(stats.between(4, 5)), 2)
        self.assertEqual(len(stats.between(5, 5)), 1)

    def test_challenge_values(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        self.assertEqual(stats.less(4), [3, 3])
        self.assertEqual(stats.between(3, 6), [3, 3, 4, 6])
        self.assertEqual(stats.greater(4), [6, 9])
