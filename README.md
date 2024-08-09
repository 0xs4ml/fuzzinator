### Performs directory enumeration on websites using a wordlist.
- Green for found directories.
- Red for not found directories or connection errors.

### Usage:
- -u or --url: Base URL of the target site.
- -w or --wordlist: Path to the wordlist file containing directories to be tested.
- `python fuzzinator.py -u http://example.com -w /path/to/wordlist.txt`

### Dependencies:
- requests: Library for making HTTP requests -> `pip install requests`

- argparse: Standard library for command-line argument parsing -> `pip install argparse`
