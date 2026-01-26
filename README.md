# 🔐 Brute Force Login Simulator

An educational tool demonstrating how brute force attacks work and how to defend against them in a controlled environment.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [How Brute Force Attacks Work](#how-brute-force-attacks-work)
- [Defensive Mechanisms Implemented](#defensive-mechanisms-implemented)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Sample Output](#sample-output)
- [Ethical Usage Warning](#ethical-usage-warning)
- [License](#license)

---

## 🎯 Project Overview

This project simulates a brute force attack on a dummy login system to demonstrate:
- How weak passwords can be compromised
- The effectiveness of strong passwords
- Defensive mechanisms against brute force attacks

The simulator uses a wordlist-based approach to guess passwords and shows how security measures can protect against such attacks.

---

## ⚔️ How Brute Force Attacks Work

A brute force attack systematically tries different password combinations until the correct one is found. This tool demonstrates:

1. **Password Guessing**: Iterating through a list of common passwords
2. **Hash Comparison**: Comparing SHA-256 hashes instead of plaintext
3. **Performance Measurement**: Tracking attempts and time taken
4. **Attack Persistence**: Continuing until password is found or wordlist exhausted

---

## 🛡️ Defensive Mechanisms Implemented

Our dummy login system includes several security measures:

1. **Maximum Attempt Limit**: Locks account after 3 failed attempts
2. **Time Delays**: 1-second delay between login attempts
3. **Account Lockout**: 30-second lockout period after failed attempts
4. **Security Logging**: Records all login attempts for monitoring
5. **Secure Hashing**: Uses SHA-256 for password storage

---

## 📁 Project Structure

```
bruteforce-login-simulator/
├── main.py                 # Main program entry point
├── login_system.py         # Dummy login system with security features
├── brute_force.py          # Brute force simulation engine
├── wordlist.txt            # Password wordlist for simulation
├── security.log            # Security logs (generated at runtime)
├── requirements.txt        # Python dependencies (none for this project)
├── README.md               # This file
└── LICENSE                 # Apache 2.0 License
```

---

## ▶️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vision-dev1/bruteforce-login-simulator.git
   cd bruteforce-login-simulator
   ```

2. **Run the simulator:**
   ```bash
   python3 main.py
   ```

3. **Follow the interactive menu:**
   - Option 1: Run brute force simulation
   - Option 2: Test login manually
   - Option 3: View security information
   - Option 4: Exit

**Requirements:** Python 3.6+

---

## 📊 Sample Output

```
============================================================
🔐 BRUTE FORCE LOGIN SIMULATOR - EDUCATIONAL PURPOSES ONLY
============================================================
⚠️  DISCLAIMER: This tool is for educational purposes only.
   Do NOT use this tool on real systems without permission.
============================================================

----------------------------------------
MAIN MENU
----------------------------------------
1. Run Brute Force Simulation
2. Test Login Manually
3. View Security Information
4. Exit
----------------------------------------
Select an option (1-4): 1

🚀 Starting Brute Force Simulation...
----------------------------------------
🎯 Target Username: admin
🔍 Target Hashed Password: a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3

Loading wordlist...
📄 Loaded 709 passwords from wordlist

Starting brute force attack...

Attempt Password             Result
----------------------------------------
[  1] Trying: password           ❌ FAILED
[  2] Trying: 123456             ❌ FAILED
[  3] Trying: 123456789          ❌ FAILED
🔒 Account locked! Waiting for unlock...
[  4] Trying: qwerty             ❌ FAILED
[  5] Trying: abc123             ❌ FAILED
[  6] Trying: password123        ❌ FAILED
🔒 Account locked! Waiting for unlock...
[  7] Trying: admin              ❌ FAILED
[  8] Trying: letmein            ❌ FAILED
[  9] Trying: welcome            ❌ FAILED
🔒 Account locked! Waiting for unlock...
[ 10] Trying: monkey             ❌ FAILED
[ 11] Trying: dragon             ✅ SUCCESS

==================================================
📊 SIMULATION RESULTS
==================================================
✅ PASSWORD FOUND: dragon
🔢 ATTEMPTS MADE: 11
⏱️  TIME TAKEN: 5.23 seconds
==================================================
```

---

## ⚠️ Ethical Usage Warning

**DISCLAIMER: This project is for educational purposes only.**

Do NOT use this tool on real systems without explicit permission from the system owner. Unauthorized access to computer systems is illegal and unethical.

This simulator is designed to:
- Educate about cybersecurity concepts
- Demonstrate the importance of strong passwords
- Show how defensive mechanisms work
- Provide a safe learning environment

**Always practice ethical hacking and responsible disclosure.**

---

## 📄 License

Copyright © 2025 Vision KC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

See [LICENSE](LICENSE) file for details.

---

**Designed by Vision**  
[Github](https://github.com/vision-dev1)
[Portfolio](https://visionkc.com.np)
