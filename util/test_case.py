import unittest

class TestCase(unittest.TestCase):
    def test_cases(self):
        raise NotImplementedError()

    def method(self):
        raise NotImplementedError()

    def run_tests(self):
        for args in self.test_cases():
            t = args[0]
            expected = args[-1]
            actual = self.method()(*args[0:len(args) - 1])
            try:
                if isinstance(actual, list):
                    self.assertCountEqual(actual, expected)
                else:
                    assert actual == expected
            except AssertionError as e:
                print(e)
                print('\033[91m' + f"Test failed: {t}")
                print('\033[91m' + f"Expected: {expected}\nActual: {actual}")
            else:
                print('\033[92m' + f"Test passed! {t}")