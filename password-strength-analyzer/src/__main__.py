# This file serves as the entry point for the application, coordinating the analysis and generation processes based on user input.

from analyzer.strength import PasswordStrengthAnalyzer
from generator.wordlist_generator import WordlistGenerator
from exporter.exporter import WordlistExporter

def main():
    print("Welcome to the Password Strength Analyzer and Wordlist Generator!")
    while True:
        print("\nChoose an option:")
        print("1. Analyze a password")
        print("2. Generate a custom wordlist")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            password = input("Enter the password to analyze: ")
            analyzer = PasswordStrengthAnalyzer()
            strength = analyzer.analyze_password(password)
            print(f"Password strength: {strength}")
        
        elif choice == '2':
            inputs = input("Enter inputs for wordlist generation (comma-separated): ").split(',')
            generator = WordlistGenerator()
            wordlist = generator.generate_wordlist([input.strip() for input in inputs])
            filename = input("Enter the filename to save the wordlist (without .txt): ") + ".txt"
            exporter = WordlistExporter()
            exporter.export_to_txt(wordlist, filename)
            print(f"Wordlist saved to {filename}")
        
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()