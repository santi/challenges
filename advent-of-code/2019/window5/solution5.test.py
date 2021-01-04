import unittest
from solution5 import decode_instruction


class TestDecodeInstruction(unittest.TestCase):

    def test_decoding_single_digits_no_op_modes(self):
        op, op_modes = decode_instruction(1)
        self.assertEqual(op, 1)
        self.assertListEqual(op_modes, [0, 0, 0])

    def test_decoding_double_digits_no_modes(self):
        op, op_modes = decode_instruction(99)
        self.assertEqual(op, 99)
        self.assertListEqual(op_modes, [0, 0, 0])

    def test_decode_single_op_mode(self):
        op, op_modes = decode_instruction(199)
        self.assertEqual(op, 99)
        self.assertListEqual(op_modes, [1, 0, 0])

    def test_decode_double_op_mode(self):
        op, op_modes = decode_instruction(1199)
        self.assertEqual(op, 99)
        self.assertListEqual(op_modes, [1, 1, 0])

    def test_decode_triple_op_mode(self):
        op, op_modes = decode_instruction(10199)
        self.assertEqual(op, 99)
        self.assertListEqual(op_modes, [1, 0, 1])


if __name__ == '__main__':
    unittest.main()
