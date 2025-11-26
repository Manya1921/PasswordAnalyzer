class WordlistGenerator:
    def __init__(self):
        self.common_patterns = ["123", "abc", "password", "qwerty"]

    def generate_wordlist(self, inputs):
        wordlist = set()
        for input_item in inputs:
            wordlist.add(input_item)
            for pattern in self.common_patterns:
                wordlist.add(input_item + pattern)
                wordlist.add(pattern + input_item)
                wordlist.add(input_item + input_item)
        
        return list(wordlist)