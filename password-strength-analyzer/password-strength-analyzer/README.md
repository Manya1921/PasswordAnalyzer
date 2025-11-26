# Password Strength Analyzer

## Overview
The Password Strength Analyzer is a Python tool designed to evaluate the strength of passwords and generate custom wordlists. It utilizes various heuristics and metrics to analyze passwords and provides users with the ability to create personalized wordlists based on their inputs.

## Features
- **Password Strength Analysis**: Evaluate the strength of a given password using advanced algorithms.
- **Custom Wordlist Generation**: Create wordlists based on user-defined inputs and common patterns.
- **Export Functionality**: Save generated wordlists in .txt format for use with cracking tools.

## Installation
To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage
### Analyzing Password Strength
To analyze a password, you can use the command-line interface. Run the following command:

```
python src/cli.py analyze <your_password>
```

### Generating a Custom Wordlist
To generate a custom wordlist, use the following command:

```
python src/cli.py generate <name> <date> <pet>
```

### Exporting Wordlists
Generated wordlists can be exported to a .txt file using the export functionality in the command-line interface.

## Testing
To run the tests for the project, use the following command:

```
pytest tests/
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.