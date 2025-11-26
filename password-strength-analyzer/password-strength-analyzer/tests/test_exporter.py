import unittest
from src.exporter.exporter import WordlistExporter

class TestWordlistExporter(unittest.TestCase):

    def setUp(self):
        self.exporter = WordlistExporter()
        self.wordlist = ["password123", "letmein", "123456"]
        self.filename = "test_wordlist.txt"

    def test_export_to_txt(self):
        self.exporter.export_to_txt(self.wordlist, self.filename)
        with open(self.filename, 'r') as file:
            content = file.read().splitlines()
        self.assertEqual(content, self.wordlist)

    def tearDown(self):
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()