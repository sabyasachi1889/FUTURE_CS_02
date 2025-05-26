# Phishing Attack Simulation Program

## Overview

This Python script simulates phishing attacks by sending customizable phishing emails to a list of employee email addresses.  
It is designed to test employee awareness regarding phishing threats and to help improve security training programs in a safe, ethical, and controlled manner.

## Features

- Sends simulated phishing emails with varied realistic phishing themes  
- Customizable SMTP server and sender credentials  
- Loads a list of employees with names and email addresses  
- Logs status of sent emails  
- Includes randomized email subjects and bodies to mimic real phishing attempts  
- Simple and easy to extend for organization-specific scenarios

## Requirements

- Python 3.x  
- Access to an SMTP server for sending emails (e.g. company mail server, Gmail SMTP)  

Python packages used (standard library):  
- `smtplib`  
- `email`  
- `ssl`  
- `random`  
- `time`  

No external packages required.

## Setup and Usage

1. Clone or download this repository.  
2. Open `phishing_simulation.py` in a text editor.  
3. Configure SMTP settings:
   - `SMTP_SERVER` - your SMTP server address  
   - `SMTP_PORT` - your SMTP server port (e.g. 587 for TLS)  
   - `SENDER_EMAIL` - your sender email address  
   - `SENDER_PASSWORD` - the password for your sender email  
   - `USE_TLS` - set to `True` if your server requires TLS  
4. Modify the employee list in `load_employee_list()` or replace it to load from a file/database.  
5. Run the script:
   6. Monitor the console output to check which emails were sent successfully.

## Important Notes and Ethics

- This script is intended for authorized internal use only for employee security awareness testing.  
- Always obtain proper permissions before conducting phishing simulations.  
- Do NOT use this script to harm, deceive, or send unsolicited phishing emails to anyone outside your organization.  
- Use the simulation results to guide security training and improve employee defenses against phishing attacks.  

## Customization

- You can extend or replace phishing email templates in the `generate_phishing_email_content()` function to match your organization's context.  
- For real tracking of user clicks, integrate with a web tracking solution or phishing simulation service that supports link tracking.

## License

This project is provided as-is for educational and internal training purposes.

---

Created by SABYASACHI, 2024  
Feel free to enhance and adapt to your organization's needs.
