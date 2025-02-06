import unittest
import hashlib


def md5sum(data):
    data = str(data)
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

class test_00 (unittest.TestCase):
    test_cases = ['test_empty_error', 'test_00_true', 'test_00_false', 'test_01_true', 'test_01_false']

    def test_empty_error(self):
        with self.assertRaises(Exception) as cm:
            print(test_cases[0])

    def test_00_true(self):
        answer = 1
        expected_answer = 1

        self.assertEqual(expected_answer, answer)
        self.assertEqual(answer, expected_answer)

    def test_00_false(self):
        answer = 1
        expected_answer = 0

        self.assertFalse(expected_answer, answer)

    def test_01_true(self):
        answer = md5sum('yes')
        expected_answer = md5sum('yes')

        self.assertEqual(expected_answer, answer)

    def test_01_false(self):
        answer = md5sum('yes')
        expected_answer = md5sum('no')

        self.assertFalse(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()