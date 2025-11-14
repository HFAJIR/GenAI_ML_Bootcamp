class BankAccount:
    def __init__(self, username, password, initial_balance=0):
        self.balance = initial_balance
        self.username = username
        self.password = password
        self.authenticated = False
    
    def authenticate(self, username, password):
        """Authenticate the user with username and password"""
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False
    
    def _check_authentication(self):
        """Check if user is authenticated before allowing transactions"""
        if not self.authenticated:
            raise Exception("User not authenticated. Please log in first.")
    
    def _check_positive_amount(self, amount):
        """Check if amount is positive"""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Amount must be a positive number")
    
    def deposit(self, amount):
        """Deposit a positive amount to the account"""
        self._check_authentication()
        self._check_positive_amount(amount)
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw a positive amount from the account"""
        self._check_authentication()
        self._check_positive_amount(amount)
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        """Get current balance"""
        self._check_authentication()
        return self.balance
    
    def logout(self):
        """Log out the user"""
        self.authenticated = False


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, initial_balance=0, minimum_balance=0):
        super().__init__(username, password, initial_balance)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        """Withdraw amount only if balance remains above minimum balance"""
        self._check_authentication()
        self._check_positive_amount(amount)
        
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Minimum balance of {self.minimum_balance} must be maintained")
        
        self.balance -= amount
        return self.balance


class ATM:
    def __init__(self, account_list, try_limit=2):
        # Validate account_list
        if not isinstance(account_list, list) or not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("account_list must be a list of BankAccount or MinimumBalanceAccount instances")
        
        # Validate and set try_limit
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit. Setting to default value of 2.")
            try_limit = 2
        
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.current_user = None
        
        # Start the ATM
        self.show_main_menu()
    
    def show_main_menu(self):
        """Display the main ATM menu"""
        while True:
            print("\n" + "=" * 30)
            print("        ATM MAIN MENU")
            print("=" * 30)
            print("1. Log in")
            print("2. Exit")
            print("=" * 30)
            
            choice = input("Please select an option (1-2): ").strip()
            
            if choice == "1":
                self.log_in()
            elif choice == "2":
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    
    def log_in(self):
        """Handle user login"""
        while self.current_tries < self.try_limit:
            print("\n" + "-" * 20)
            print("      LOGIN")
            print("-" * 20)
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            # Check against all accounts
            for account in self.account_list:
                if account.authenticate(username, password):
                    self.current_user = account
                    self.current_tries = 0  # Reset tries on successful login
                    print(f"\nWelcome, {username}!")
                    self.show_account_menu(account)
                    return
            
            # If no match found
            self.current_tries += 1
            remaining_tries = self.try_limit - self.current_tries
            print(f"Invalid username or password. {remaining_tries} attempt(s) remaining.")
        
        # Max tries reached
        print("\nMaximum login attempts reached. ATM is shutting down for security.")
        exit()
    
    def show_account_menu(self, account):
        """Display account operations menu"""
        while True:
            print("\n" + "=" * 30)
            print("      ACCOUNT MENU")
            print("=" * 30)
            print(f"Current balance: ${account.get_balance():.2f}")
            print("=" * 30)
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Log out")
            print("=" * 30)
            
            choice = input("Please select an option (1-4): ").strip()
            
            try:
                if choice == "1":
                    self.handle_deposit(account)
                elif choice == "2":
                    self.handle_withdraw(account)
                elif choice == "3":
                    self.handle_balance_check(account)
                elif choice == "4":
                    print("Logging out...")
                    account.logout()
                    self.current_user = None
                    break
                else:
                    print("Invalid option. Please try again.")
            except Exception as e:
                print(f"Error: {e}")
    
    def handle_deposit(self, account):
        """Handle deposit operation"""
        try:
            amount = float(input("Enter deposit amount: $"))
            new_balance = account.deposit(amount)
            print(f"Deposit successful! New balance: ${new_balance:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
        except Exception as e:
            print(f"Deposit failed: {e}")
    
    def handle_withdraw(self, account):
        """Handle withdraw operation"""
        try:
            amount = float(input("Enter withdrawal amount: $"))
            new_balance = account.withdraw(amount)
            print(f"Withdrawal successful! New balance: ${new_balance:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
        except Exception as e:
            print(f"Withdrawal failed: {e}")
    
    def handle_balance_check(self, account):
        """Handle balance check operation"""
        balance = account.get_balance()
        print(f"Current balance: ${balance:.2f}")


# Demonstration and testing
if __name__ == "__main__":
    # Create some test accounts
    accounts = [
        BankAccount("john_doe", "password123", 1000),
        MinimumBalanceAccount("jane_smith", "secure456", 2000, 500),
        BankAccount("bob_wilson", "test789", 500)
    ]
    
    print("Creating ATM with test accounts...")
    
    try:
        # Create ATM instance
        atm = ATM(accounts, try_limit=3)
    except Exception as e:
        print(f"ATM initialization error: {e}")
   