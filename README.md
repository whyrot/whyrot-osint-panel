# OSINT Tool – Usage & Requirements

This tool is designed to run on Linux and combines Sherlock, Nmap, and a phone number lookup API for basic OSINT tasks.

# Requirements

Make sure you have the following installed and set up:

Linux
Tested on Debian (other Debian-based distros should work fine)

Python 3

Sherlock (Python version)
⚠️ Do not use the apt package version — it will not work correctly

Nmap

Numverify API key (for phone number lookup)

# Installation Notes
Sherlock

Clone the official Sherlock repository (recommended):

git clone https://github.com/sherlock-project/sherlock.git


Make sure it runs with Python:

python3 sherlock.py --help

# Usage Guide

Below is a step-by-step guide to configure the script so everything works correctly on your system.

# Setting Up Sherlock

Open osint.py in any text editor or IDE (VS Code, nano, vim, etc.).

Locate line 8.

Replace the existing Sherlock directory path with the full path to your local Sherlock folder.

Example:
os.chdir("/home/yourusername/tools/sherlock")


⚠️ Paths are case-sensitive on Linux.

# Setting Up Phone Number Lookup (Numverify)

Go to https://numverify.com
 and create an account.

After logging in, open the Dashboard.

Copy your API key.

Open osint.py in your editor.

Locate line 19.

Replace:

YOUR_KEY_HERE


with your actual API key.

Example:
API_KEY = "abcdef1234567890"

# Screenshot
<img width="906" height="603" alt="2026-01-11_12-37" src="https://github.com/user-attachments/assets/9640a949-c7af-4c7e-a50c-a76a2a4a334b" />


# Final Notes

Make sure all dependencies are installed before running the script.

If something fails, double-check:

Directory paths

API key

Python version (python3 --version)

This tool is intended for educational and OSINT purposes only.
