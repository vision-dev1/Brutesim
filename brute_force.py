"""
Brute Force Simulator Module

This module simulates a brute force attack on a dummy login system
using a wordlist for educational purposes.

Author: Vision KC
GitHub: https://github.com/vision-dev1
Portfolio: https://visionkc.com.np
"""

import time


class BruteForceSimulator:
    """
    A brute force simulator that attempts to crack passwords using a wordlist.
    """
    
    def __init__(self, login_system, wordlist_file):
        """
        Initialize the brute force simulator.
        
        Args:
            login_system (DummyLoginSystem): The login system to attack
            wordlist_file (str): Path to the wordlist file
        """
        self.login_system = login_system
        self.wordlist_file = wordlist_file
        self.attempts = 0
    
    def load_wordlist(self):
        """
        Load passwords from the wordlist file.
        
        Returns:
            list: List of passwords from the wordlist
        """
        try:
            with open(self.wordlist_file, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"❌ Wordlist file '{self.wordlist_file}' not found.")
            return []
    
    def attempt_login(self, password):
        """
        Attempt to login with a specific password.
        
        Args:
            password (str): The password to try
            
        Returns:
            bool: True if login successful, False otherwise
        """
        self.attempts += 1
        print(f"[{self.attempts:3}] Trying: {password:<20}", end="")
        
        success = self.login_system.authenticate(
            self.login_system.username, 
            password
        )
        
        if success:
            print("✅ SUCCESS")
            return True
        else:
            print("❌ FAILED")
            # Check if account is locked
            if self.login_system.is_account_locked():
                print(f"🔒 Account locked! Waiting for unlock...")
                # Wait for account to unlock
                if self.login_system.locked_until:
                    remaining_time = int(self.login_system.locked_until - time.time())
                    time.sleep(remaining_time + 1)  # Wait for unlock plus 1 second
                return False
        return False
    
    def run_simulation(self):
        """
        Run the brute force simulation using the wordlist.
        
        Returns:
            str or None: Found password if successful, None otherwise
        """
        print("Loading wordlist...")
        wordlist = self.load_wordlist()
        
        if not wordlist:
            print("🚫 Cannot proceed without wordlist.")
            return None
        
        print(f"📄 Loaded {len(wordlist)} passwords from wordlist")
        print("\nStarting brute force attack...\n")
        print("Attempt Password             Result")
        print("-" * 40)
        
        for password in wordlist:
            # Skip if account is locked
            if self.login_system.is_account_locked():
                print(f"🔒 Account is locked. Waiting for unlock...")
                # Wait for account to unlock
                if self.login_system.locked_until:
                    remaining_time = int(self.login_system.locked_until - time.time())
                    if remaining_time > 0:
                        time.sleep(remaining_time + 1)  # Wait for unlock plus 1 second
            
            # Attempt login
            if self.attempt_login(password):
                return password
            
            # Small delay to simulate network latency and be respectful
            time.sleep(0.1)
        
        return None