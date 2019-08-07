import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from self_checkout import self_checkout
    else:
        from ..self_checkout import self_checkout
else:
    from self_checkout import self_checkout

class SelfCheckoutIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["25", "2", "10", "1", False]

        expected_result = (
            "Subtotal: $60.00\n" +
            "Tax: $3.30\n" +
            "Total: $63.30"
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            self_checkout.main()
            test_val = print_output.getvalue().strip()
            test_val = "Subtotal" + test_val.split("Subtotal",1)[1]

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
