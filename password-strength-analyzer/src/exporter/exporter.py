class WordlistExporter:
    def export_to_txt(self, wordlist, filename):
        with open(filename, 'w') as file:
            for word in wordlist:
                file.write(f"{word}\n")