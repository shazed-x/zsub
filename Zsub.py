import dns.resolver
import concurrent.futures
import threading
import signal
import sys
import os
import argparse
from colorama import Fore, init

# Initialize colorama for colored output
init(autoreset=True)

# Global variables
valid_subdomains = []
total_scanned = 0
no_answer_count = 0
timeout_count = 0
failed_count = 0
stop_event = threading.Event()  # Event to stop scanning on CTRL+C
executor = None  # ThreadPoolExecutor reference
output_file = ""  # Will store the filename dynamically

def save_results():
    """Save found subdomains to a file."""
    if valid_subdomains:
        with open(output_file, "w") as f:
            f.write("\n".join(valid_subdomains) + "\n")
        print(Fore.YELLOW + f"\n[INFO] Results saved to {output_file}")

def print_summary():
    """Print the Scan Summary before exiting."""
    print(Fore.CYAN + "\n=== Scan Summary ===")
    print(f"Total subdomains scanned: {total_scanned}")
    print(Fore.GREEN + f"Valid subdomains found: {len(valid_subdomains)}")
    print(Fore.YELLOW + f"No Answer responses: {no_answer_count}")
    print(Fore.RED + f"Timeout errors: {timeout_count}")
    print(Fore.RED + f"Failed subdomains (NXDOMAIN + Errors): {failed_count}")
    print(Fore.YELLOW + f"Results saved to {output_file}")

def handle_exit(signal_received, frame):
    """Handle CTRL+C to stop scanning immediately and ensure clean output."""
    global executor
    print(Fore.RED + "\n[EXIT] CTRL+C detected! Stopping scan immediately...")

    stop_event.set()  # Stop scanning

    if executor:
        executor.shutdown(wait=False, cancel_futures=True)  # Kill all running threads

    save_results()    # Save results before exiting
    print_summary()   # Show Scan Summary
    sys.exit(0)

# Attach signal handler for CTRL+C
signal.signal(signal.SIGINT, handle_exit)

def load_wordlist(wordlist_path):
    """Load words from a file or all .txt files in a directory."""
    words = []
    if os.path.isdir(wordlist_path):
        print(Fore.YELLOW + f"[INFO] '{wordlist_path}' is a directory. Loading all .txt files.")
        for filename in os.listdir(wordlist_path):
            file_path = os.path.join(wordlist_path, filename)
            if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
                try:
                    with open(file_path, "r") as f:
                        file_words = [line.strip() for line in f if line.strip()]
                        words.extend(file_words)
                    print(Fore.YELLOW + f"[INFO] Loaded {len(file_words)} words from {filename}")
                except Exception as e:
                    print(Fore.RED + f"[ERROR] Could not load {filename}: {e}")
    else:
        try:
            with open(wordlist_path, "r") as f:
                words = [line.strip() for line in f if line.strip()]
            print(Fore.YELLOW + f"[INFO] Loaded {len(words)} words from {wordlist_path}")
        except FileNotFoundError:
            print(Fore.RED + f"[ERROR] Wordlist file '{wordlist_path}' not found.")
    return words

def check_subdomain(domain, subdomain):
    """Check if a subdomain is valid."""
    global total_scanned, no_answer_count, timeout_count, failed_count

    if stop_event.is_set():
        return  # Stop if CTRL+C is pressed

    full_subdomain = f"{subdomain}.{domain}"
    resolver = dns.resolver.Resolver()
    resolver.timeout = 3  # Faster timeout
    resolver.lifetime = 3
    total_scanned += 1  # Count each subdomain checked

    try:
        resolver.resolve(full_subdomain, "A")
        print(Fore.GREEN + "[FOUND] " + Fore.RESET + full_subdomain)
        valid_subdomains.append(full_subdomain)
    except dns.resolver.NoAnswer:
        print(Fore.YELLOW + "[NO ANSWER] " + Fore.RESET + full_subdomain)
        no_answer_count += 1
    except dns.resolver.NXDOMAIN:
        if not stop_event.is_set():  # Prevent printing after CTRL+C
            print(Fore.RED + "[FAILED] " + Fore.RESET + full_subdomain)
        failed_count += 1
    except dns.resolver.LifetimeTimeout:
        if not stop_event.is_set():
            print(Fore.RED + "[TIMEOUT] " + Fore.RESET + full_subdomain)
        timeout_count += 1
    except Exception:
        if not stop_event.is_set():
            print(Fore.RED + "[FAILED] " + Fore.RESET + full_subdomain)
        failed_count += 1

def subfinder(domain, wordlist_path):
    """Scan subdomains using multithreading."""
    global executor
    words = load_wordlist(wordlist_path)
    if not words:
        print(Fore.RED + "[ERROR] No words loaded. Exiting.")
        return

    print(Fore.YELLOW + f"\n[INFO] Scanning {len(words)} subdomains...\n")

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

    try:
        futures = [executor.submit(check_subdomain, domain, word) for word in words]
        concurrent.futures.wait(futures)
    except KeyboardInterrupt:
        handle_exit(None, None)  # Handle CTRL+C instantly

def main():
    """Main function to start the subdomain enumeration."""
    global output_file  

    parser = argparse.ArgumentParser(description="Powerful Subdomain Finder")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file or directory")
    args = parser.parse_args()

    domain = args.domain.strip()
    wordlist_path = args.wordlist.strip()

    # Create output file dynamically
    safe_domain = domain.replace(".", "_")  
    output_file = f"{safe_domain}_subdomains.txt"

    print(Fore.CYAN + "\nStarting subdomain enumeration...\n")

    subfinder(domain, wordlist_path)

    print(Fore.CYAN + "\nEnumeration completed!")
    print_summary()
    save_results()

if __name__ == "__main__":
    main()
