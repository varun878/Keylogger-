Keylogger Project
Author: Varun Kumar

This is a Python-based keylogger developed for a college mini project. It records keystrokes, captures screenshots at regular intervals, and collects system information. All the gathered data is then securely emailed to a designated address.

Features
Keylogging: Captures and logs keystrokes to a text file.
Screenshot Capture: Periodically takes screenshots of the desktop.
System Information: Collects details like OS and user information.
Data Encryption: Ensures sensitive data is encrypted before sending.
Email Reporting: Sends logs and screenshots to a specified email.
Multi-Processing: Runs keylogger and screenshot capture simultaneously.
Libraries Used
smtplib: For sending emails via SMTP.
pynput: For monitoring and capturing keystrokes.
ImageGrab (Pillow): For capturing screenshots.
cryptography.fernet: For encrypting data before sending.
multiprocessing: To run multiple tasks concurrently.
Installation
Clone the repository to your local machine:

bash
Copy
git clone https://github.com/yourusername/keylogger.git
cd keylogger
Install the required packages:

bash
Copy
pip install -r requirements.txt
Usage
Open the Keylogger.py script in your preferred IDE or editor.

Configure your email credentials (email_address and app_password) and set the recipient's email (toaddr).

Run the script:

bash
Copy
python Keylogger.py
The keylogger will start running, logging keystrokes and capturing screenshots, then sending the data to the specified email.

Security Warning
This tool is intended for educational purposes only. Misuse of this project can be illegal and unethical. Always ensure you have proper authorization before using any keylogger tool.

License
