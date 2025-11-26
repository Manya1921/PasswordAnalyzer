import unittest
from src.generator.wordlist_generator import WordlistGenerator

class TestWordlistGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = WordlistGenerator()

    def test_generate_wordlist_basic(self):
        inputs = ['john', 'doe', '2021']
        expected_output = ['john', 'doe', '2021', 'john2021', 'doe2021', 'john_doe', 'doe_john']
        result = self.generator.generate_wordlist(inputs)
        self.assertTrue(set(expected_output).issubset(set(result)))

    def test_generate_wordlist_with_patterns(self):
        inputs = ['alice', 'bob']
        expected_output = ['alice', 'bob', 'alice2023', 'bob2023', 'alice_bob', 'bob_alice']
        result = self.generator.generate_wordlist(inputs)
        self.assertTrue(set(expected_output).issubset(set(result)))

    def test_generate_wordlist_empty_input(self):
        inputs = []
        result = self.generator.generate_wordlist(inputs)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()