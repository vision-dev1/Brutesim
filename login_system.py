"""
Dummy Login System Module

This module implements a secure login system with defensive mechanisms
against brute force attacks for educational purposes.

Author: Vision KC
GitHub: https://github.com/vision-dev1
Portfolio: https://visionkc.com.np
"""

import hashlib
import time
import logging
from datetime import datetime


class DummyLoginSystem:
    """
    A dummy login system that demonstrates secure authentication practices
    and defensive mechanisms against brute force attacks.
    """
    
    def __init__(self, username="admin", password="SecurePass123!"):
        """
        Initialize the dummy login system.
        
        Args:
            username (str): The username for the account
            password (str): The plaintext password (will be hashed)
        """
        self.username = username
        self.password_hash = self._hash_password(password)
        self.max_attempts = 3
        self.failed_attempts = 0
        self.locked_until = None
        self.lockout_duration = 30  # Lockout for 30 seconds
        self.delay_duration = 1  # 1 second delay between attempts
        
        # Setup logging
        logging.basicConfig(
            filename='security.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def _hash_password(self, password):
        """
        Hash a password using SHA-256.
        
        Args:
            password (str): The plaintext password
            
        Returns:
            str: The SHA-256 hash of the password
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def is_account_locked(self):
        """
        Check if the account is currently locked.
        
        Returns:
            bool: True if account is locked, False otherwise
        """
        if self.locked_until is not None and time.time() < self.locked_until:
            return True
        elif self.locked_until is not None and time.time() >= self.locked_until:
            # Unlock account
            self.locked_until = None
            self.failed_attempts = 0
            return False
        return False
    
    def authenticate(self, username, password):
        """
        Authenticate a user with username and password.
        
        Args:
            username (str): The username to authenticate
            password (str): The plaintext password to check
            
        Returns:
            bool: True if authentication successful, False otherwise
        """
        # Check if account is locked
        if self.is_account_locked():
            remaining_time = int(self.locked_until - time.time()) if self.locked_until is not None else 0
            self.logger.warning(f"Login attempt on locked account. Remaining lock time: {remaining_time}s")
            return False
        
        # Add delay to slow down brute force attempts
        time.sleep(self.delay_duration)
        
        # Check credentials
        if username == self.username and self._hash_password(password) == self.password_hash:
            # Reset failed attempts on successful login
            self.failed_attempts = 0
            self.logger.info("Successful login")
            return True
        else:
            # Increment failed attempts
            self.failed_attempts += 1
            self.logger.warning(f"Failed login attempt ({self.failed_attempts}/{self.max_attempts})")
            
            # Lock account if max attempts reached
            if self.failed_attempts >= self.max_attempts:
                self.locked_until = time.time() + self.lockout_duration
                self.logger.critical(f"Account locked for {self.lockout_duration} seconds due to repeated failed attempts")
                self.logger.critical(f"Account locked for {self.lockout_duration} seconds due to repeated failed attempts")
            
            return False