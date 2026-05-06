import unittest
from dilution import calculate_final_volume

class TestDilution(unittest.TestCase):
    def test_basic(self):
        # Testing 10mg/ml stock, 5ml used, diluted to 2mg/ml
        # Should result in 25ml total (V2) and 20ml added buffer
        v2, v_add = calculate_final_volume(10, 5, 2)
        self.assertEqual(v2, 25)
        self.assertEqual(v_add, 20)

if __name__ == "__main__":
    unittest.main()