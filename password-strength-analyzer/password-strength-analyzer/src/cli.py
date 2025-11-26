import argparse
from analyzer.strength import PasswordStrengthAnalyzer
from generator.wordlist_generator import WordlistGenerator
from exporter.exporter import WordlistExporter

def main():
    parser = argparse.ArgumentParser(description='Password Strength Analyzer and Wordlist Generator')
    
    subparsers = parser.add_subparsers(dest='command')

    # Password strength analysis
    strength_parser = subparsers.add_parser('analyze', help='Analyze password strength')
    strength_parser.add_argument('password', type=str, help='Password to analyze')

    # Wordlist generation
    wordlist_parser = subparsers.add_parser('generate', help='Generate a custom wordlist')
    wordlist_parser.add_argument('inputs', nargs='+', help='Inputs for wordlist generation (e.g., name date pet)')

    # Export wordlist
    export_parser = subparsers.add_parser('export', help='Export wordlist to .txt file')
    export_parser.add_argument('filename', type=str, help='Filename to save the wordlist')

    args = parser.parse_args()

    if args.command == 'analyze':
        analyzer = PasswordStrengthAnalyzer()
        strength = analyzer.analyze_password(args.password)
        print(f'Password strength: {strength}')

    elif args.command == 'generate':
        generator = WordlistGenerator()
        wordlist = generator.generate_wordlist(args.inputs)
        print(f'Generated wordlist: {wordlist}')

    elif args.command == 'export':
        generator = WordlistGenerator()
        wordlist = generator.generate_wordlist(args.inputs)
        exporter = WordlistExporter()
        exporter.export_to_txt(wordlist, args.filename)
        print(f'Wordlist exported to {args.filename}')

if __name__ == '__main__':
    main()