import unittest
from gencontent import extract_title

class TestStringhe(unittest.TestCase):
    def test_canc(self):
        risultato = extract_title("#   Home   ")
        self.assertEqual(risultato, "Home")

    def test_2row(self):
        result = extract_title("\n#    FH6")
        self.assertEqual(result, "FH6")

    def test_before(self):
        result = extract_title("ugrd\n#    FH6")
        self.assertEqual(result, "FH6")

    def test_solo_sottotitolo(self):
        with self.assertRaises(Exception):
            extract_title("## Primo capitolo")

    def test_senza_titolo(self):
        with self.assertRaises(Exception):
            extract_title("nooki")

if __name__ == "__main__":
    unittest.main(verbosity=2)
