def leetspeak_transform(word):
    leet_dict = {
        'a': '4', 'b': '8', 'e': '3', 'g': '9', 'i': '1',
        'o': '0', 's': '5', 't': '7', 'z': '2'
    }
    return ''.join(leet_dict.get(char, char) for char in word)

def append_years(word, years):
    return [f"{word}{year}" for year in years]

def apply_rules(word, years):
    transformed_words = []
    transformed_words.append(leetspeak_transform(word))
    transformed_words.extend(append_years(word, years))
    return transformed_words

def generate_wordlist(base_words, years):
    wordlist = []
    for word in base_words:
        wordlist.extend(apply_rules(word, years))
    return wordlist