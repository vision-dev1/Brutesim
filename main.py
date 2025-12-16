#!/usr/bin/env python3
"""
Brute Force Login Simulator - Educational Tool

This script demonstrates how brute force attacks work and how to defend against them.
It simulates a controlled environment to show the effectiveness of strong passwords
and defensive security measures.

Author: Vision KC
GitHub: https://github.com/vision-dev1
Portfolio: https://visionkc.com.np
"""

from login_system import DummyLoginSystem
from brute_force import BruteForceSimulator
import time


def display_welcome():
    """Display welcome message and disclaimer."""
    print("=" * 60)
    print("🔐 BRUTE FORCE LOGIN SIMULATOR - EDUCATIONAL PURPOSES ONLY")
    print("=" * 60)
    print("⚠️  DISCLAIMER: This tool is for educational purposes only.")
    print("   Do NOT use this tool on real systems without permission.")
    print("=" * 60)
    print()


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("MAIN MENU")
    print("=" * 40)
    print("1. Run Brute Force Simulation")
    print("2. Test Login Manually")
    print("3. View Security Information")
    print("4. Exit")
    print("-" * 40)


def run_brute_force_simulation():
    """Run the brute force simulation."""
    print("\n🚀 Starting Brute Force Simulation...")
    print("-" * 40)
    
    # Create login system
    login_system = DummyLoginSystem()
    
    # Show target credentials (for educational purposes)
    print(f"🎯 Target Username: {login_system.username}")
    print(f"🔍 Target Hashed Password: {login_system.password_hash}")
    print()
    
    # Create brute force simulator
    simulator = BruteForceSimulator(login_system, "wordlist.txt")
    
    # Run simulation
    start_time = time.time()
    result = simulator.run_simulation()
    end_time = time.time()
    
    # Display results
    print("\n" + "=" * 50)
    print("📊 SIMULATION RESULTS")
    print("=" * 50)
    if result:
        print(f"✅ PASSWORD FOUND: {result}")
        print(f"🔢 ATTEMPTS MADE: {simulator.attempts}")
    else:
        print("❌ PASSWORD NOT FOUND IN WORDLIST")
        print(f"🔢 ATTEMPTS MADE: {simulator.attempts}")
    
    print(f"⏱️  TIME TAKEN: {end_time - start_time:.2f} seconds")
    print("=" * 50)


def test_manual_login():
    """Allow manual login testing."""
    print("\n🧪 Manual Login Test")
    print("-" * 30)
    
    login_system = DummyLoginSystem()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    success = login_system.authenticate(username, password)
    
    if success:
        print("✅ Login successful!")
    else:
        print("❌ Login failed!")
        print(f"Attempts remaining: {login_system.max_attempts - login_system.failed_attempts}")


def display_security_info():
    """Display information about brute force attacks and defenses."""
    print("\n🛡️  SECURITY INFORMATION")
    print("-" * 30)
    print("HOW BRUTE FORCE ATTACKS WORK:")
    print("• Try many password combinations until finding the right one")
    print("• Can be automated with tools and wordlists")
    print("• More effective against weak passwords")
    print()
    print("DEFENSIVE MECHANISMS IMPLEMENTED:")
    print("• Maximum login attempt limit (locks account)")
    print("• Time delays between attempts (slows attackers)")
    print("• Secure password hashing (SHA-256)")
    print("• Logging of failed attempts")
    print()
    print("BEST PRACTICES:")
    print("• Use strong, unique passwords")
    print("• Enable two-factor authentication")
    print("• Implement account lockout policies")
    print("• Monitor for suspicious activity")


def main():
    """Main program loop."""
    display_welcome()
    
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            run_brute_force_simulation()
        elif choice == "2":
            test_manual_login()
        elif choice == "3":
            display_security_info()
        elif choice == "4":
            print("\n👋 Thank you for using the Brute Force Login Simulator!")
            print("Made By Vision | github.com/vision-dev1")
            break
        else:
            print("❌ Invalid option. Please select 1-4.")


if __name__ == "__main__":
    main()