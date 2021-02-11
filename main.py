import unittest

class PerformanceTestIsOdd(unittest.TestCase):

    def is_odd(self, n):
        return n % 2 == 1

    def test_perf(self):
        print(self.is_odd(7))

if __name__ == "__main__":
    unittest.main()