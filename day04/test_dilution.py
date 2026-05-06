# Change your test line to:
def test_basic(self):
    v2, v_add = calculate_final_volume(10, 5, 2)
    self.assertEqual(v2, 25)
    self.assertEqual(v_add, 20)