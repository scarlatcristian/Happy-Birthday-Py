# Happy-Birthday-Py

This Python script sends birthday wishes to people listed in a CSV file containing their birthdays. It reads the birthdays from the file, checks if any of them match the current date, and sends personalized emails with birthday greetings.

## Features

- Reads birthdays from a CSV file.
- Sends personalized birthday emails using Gmail SMTP.
- Supports multiple letter templates for variety.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3 installed on your local machine.
- Gmail account credentials (email address and password) for sending emails.
- Letter templates in text files (`letter1.txt`, `letter2.txt`, etc.).

## Installation

1. Clone or download this repository to your local machine.

2. Install the required dependencies using pip:

   ```bash
   pip install pandas
   
## Configure your email credentials:

1. Replace 'your_email_address' with your Gmail email address.
2. Replace 'your_google_apps_password' with your Google Apps password (or app-specific password).
3. Optionally, set a custom username in the USER_NAME variable.

## Prepare your CSV file:

1. Create a CSV file named birthdays.csv containing the following columns: name, email, day, and month.
2. List the names, email addresses, and birthdays (day and month) of the people you want to send birthday wishes to.

## Usage
To use the script:

Run the script:

   ```bash
   python birthday_wisher.py

The script will read the CSV file, check for birthdays matching the current date, and send personalized emails to the recipients.

Sit back and let the script handle the birthday wishes for you!
