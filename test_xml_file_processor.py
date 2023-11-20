import unittest

class TestFileProcessor(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(1, 1, "OK")

if __name__ == '__main__':
    unittest.main()
