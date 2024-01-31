# Email Manager

## Overview

The **Email Manager** is a Python project designed to facilitate the management and analysis of Gmail emails using the Gmail API and the OpenAI Language Model (LLM). 
It provides functionality to connect to a Gmail account, retrieve unread emails from the inbox, and filter important emails based on user-defined criteria.

## Features

- **Connect to Gmail Account:** The `Manager` class allows users to connect to their Gmail account using the Gmail API, ensuring secure and authorized access to email data.

- **Retrieve Unread Emails:** The `getEmails` method retrieves unread emails from the primary inbox and extracts relevant information such as sender, subject, and snippet.
  The extracted data is then stored in a Pandas DataFrame and exported to a CSV file named "Emails.csv."

- **Filter Important Emails:** The `filterEmail` method uses the OpenAI Language Model to filter important emails from the retrieved data.
  Users can specify keywords or topics related to important emails, and the method returns a Pandas DataFrame containing the filtered results.

## Prerequisites

- Python 3.x
- Google API client library: `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, `google-api-python-client`
- Python library: `pandasai`
- Pandas
- Emojis
- Environment variable: `openai` (containing OpenAI API key)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aymen-fkir/email-manager.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the necessary credentials:

   - Obtain credentials.json from the Google Cloud Console for Gmail API.
   - Set up the `openai` environment variable with your OpenAI API key.

## Usage

1. Run the `main.py` script:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions to authorize the Gmail API access.

3. Review the generated "Emails.csv" file containing the retrieved email data.

4. Optionally, use the `filterEmail` method to filter important emails based on specified criteria.

## Note

- Ensure that the required dependencies are installed before running the script.
- Securely manage and store sensitive information such as API keys and credentials.
- Review and adapt the OpenAI query in the `filterEmail` method based on your specific requirements.

## Contributors

- Aymen Fkir
