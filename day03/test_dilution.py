import unittest
from dilution import calculate_final_volume

class TestDilution(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(calculate_final_volume(10, 5, 2), 25)

if __name__ == "__main__":
    unittest.main()