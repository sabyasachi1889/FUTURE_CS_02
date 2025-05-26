"""
Phishing Attack Simulation Program
----------------------------------

This script simulates phishing attacks by sending customizable phishing emails to a list of employee emails.
It is intended for security awareness training and testing employee vigilance in a controlled and ethical manner.

Instructions:
- Configure SMTP server details and sender email.
- Provide recipient email addresses.
- Customize the phishing email subject and body.
- Run the script to send simulated phishing emails.
- Monitor the console to track sent emails.

IMPORTANT:
- Use only for authorized internal testing within your organization.
- Do not use to harm or deceive outside users.

Author: BLACKBOXAI
Date: 2024
"""

import smtplib
from email.message import EmailMessage
import ssl
import random
import time

class PhishingSimulator:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password, use_tls=True):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.use_tls = use_tls
        self.context = ssl.create_default_context()

    def send_email(self, recipient_email, subject, body):
        msg = EmailMessage()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.set_content(body)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls(context=self.context)
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            print(f"[+] Phishing email sent to: {recipient_email}")
            return True
        except Exception as e:
            print(f"[!] Failed to send email to {recipient_email}: {e}")
            return False

def generate_phishing_email_content(name):
    phishing_subjects = [
        "URGENT: Password Expiration Notice",
        "Security Alert: Suspicious Login Detected",
        "Action Required: Update Your Account Information",
        "Your Invoice is Ready - Please Review",
        "Important: Verify Your Email Address"
    ]

    phishing_bodies = [
        f"Dear {name},\n\nWe detected an unusual login attempt on your account. Please click the link below to verify your identity and secure your account immediately:\n\nhttp://example.com/verify\n\nThank you,\nIT Security Team",
        f"Hello {name},\n\nYour password is about to expire. To avoid any interruption of service, please update your password at your earliest convenience:\n\nhttp://example.com/update-password\n\nBest regards,\nIT Department",
        f"Dear {name},\n\nThis is a notification regarding your overdue invoice. Please review and pay promptly by clicking the secure link below:\n\nhttp://example.com/invoice\n\nThank you,\nFinance Team",
        f"Hi {name},\n\nWe are updating our records. Please verify your email by clicking the link below within 24 hours to avoid service disruption:\n\nhttp://example.com/verify-email\n\nSincerely,\nCustomer Service",
        f"Hello {name},\n\nDue to recent security updates, you must confirm your account details. Please follow the secure link:\n\nhttp://example.com/confirm\n\nRegards,\nSecurity Team"
    ]

    subject = random.choice(phishing_subjects)
    body = random.choice(phishing_bodies)

    return subject, body

def load_employee_list():
    # Sample employee list; replace with actual list or load from file
    return [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Carol", "email": "carol@example.com"},
        {"name": "Dave", "email": "dave@example.com"}
    ]

def main():
    print("=== Phishing Attack Simulation Started ===\n")

    # Configure your SMTP server details here
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587  # common port for TLS
    SENDER_EMAIL = "your-email@example.com"
    SENDER_PASSWORD = "your-password"
    USE_TLS = True

    simulator = PhishingSimulator(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, USE_TLS)

    employees = load_employee_list()
    print(f"Loaded {len(employees)} employees to receive simulated phishing emails.\n")

    for employee in employees:
        subject, body = generate_phishing_email_content(employee['name'])
        print(f"Sending to {employee['email']} | Subject: {subject}")
        success = simulator.send_email(employee['email'], subject, body)
        
        # Random delay between emails to simulate real emailing patterns
        time.sleep(random.uniform(1, 3))

    print("\n=== Phishing Attack Simulation Completed ===")
    print("Reminder: Review employee responses and plan security training accordingly.\n")

if __name__ == "__main__":
    main()
