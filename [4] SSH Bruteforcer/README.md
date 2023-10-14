# SSH Bruteforcer

SSH Bruteforcer is a Python script that attempts to perform SSH password cracking on a target SSH server using a list of potential passwords. It uses the Paramiko library for SSH connections and provides a simple command-line interface for users to specify the target IP address, SSH username, and a password file.

## Prerequisites

- Python 3.x
- Paramiko library (`pip install paramiko`)
- Termcolor library (`pip install termcolor`)

## Usage

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/cyph3rryx/R3D_H4T/ssh-bruteforcer.git
   ```

2. Change into the project directory:

   ```
   cd ssh-bruteforcer
   ```

3. Run the script:

   ```
   python script.py
   ```

4. Follow the prompts to input the target IP address, SSH username, and the filename of the password list.

5. The script will attempt to connect to the target SSH server using the provided password list. If a correct password is found, it will be displayed, and the script will terminate. If an incorrect password is tried, it will be displayed. If there is an issue with the IP or username, an appropriate message will be displayed.

## Features

- Password-based SSH brute force attack.
- Simple command-line interface.
- Color-coded output for easy readability.

## Best Practices

- Use a strong password list to increase the chances of finding the correct password.
- Implement a delay between connection attempts to avoid triggering intrusion detection mechanisms.
- Consider using it on systems you own or have explicit permission to test.
