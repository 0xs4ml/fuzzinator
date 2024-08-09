import requests
import argparse

class Colors:
    GREEN = '\033[92m'  # Green
    RED = '\033[91m'    # Red
    GRAY = '\033[90m'   # Gray
    RESET = '\033[0m'   # Reset color

    @staticmethod
    def print_intro():
        fuzzinator_art = r"""
 _____              _             _              
|  ___|   _ _______(_)_ __   __ _| |_ ___  _ __  
| |_ | | | |_  /_  / | '_ \ / _` | __/ _ \| '__| 
|  _|| |_| |/ / / /| | | | | (_| | || (_) | |    
|_|   \__,_/___/___|_|_| |_|\__,_|\__\___/|_|    
        """
        creator_name = "s4ml"
        print(f"{Colors.GRAY}{fuzzinator_art}{Colors.RESET}")
        print(f"{Colors.GRAY}Creator: {creator_name}{Colors.RESET}\n")

def enumDir(url, wordlist):
    with open(wordlist, 'r') as interactWordlist:
        directories = interactWordlist.read().splitlines()
        
        for directory in directories:
            full_url = f"{url}/{directory}"
            try:
                response = requests.get(full_url)
                
                if response.status_code == 200:
                    print(f"{Colors.GREEN}[+] Directory found: {full_url}{Colors.RESET}")
                else:
                    print(f"{Colors.RED}[-] Not found: {full_url} - Status: {response.status_code}{Colors.RESET}")
            except requests.RequestException as error:
                print(f"{Colors.RED}[!] Connection error with {full_url}: {error}{Colors.RESET}")

def main():
    Colors.print_intro()
    
    parser = argparse.ArgumentParser(description="Script for Directory Enumeration")
    
    parser.add_argument('-u', required=True, help="Target URL")
    parser.add_argument('-w', required=True, help="Wordlist Path")
    
    args = parser.parse_args()
    
    enumDir(args.u, args.w)

if __name__ == "__main__":
    main()
