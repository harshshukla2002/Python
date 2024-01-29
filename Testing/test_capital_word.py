import unittest
import CapitalWord


class TestCapital(unittest.TestCase):
    def test_one_word(self):
        text = "python"
        result = CapitalWord.capital_word(text)
        self.assertEqual(result, "Python")

    def text_multiple_word(self):
        text = "hello world"
        result = CapitalWord.capital_word(text)
        self.assertEqual(result, "Hello World")


if __name__ == "__main__":
    unittest.main()
