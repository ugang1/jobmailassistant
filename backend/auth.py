from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import json

# Constants
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
BASE_DIR = os.path.dirname(__file__)
TOKEN_DIR = os.path.join(BASE_DIR, "tokens")
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

# Ensure token directory exists
os.makedirs(TOKEN_DIR, exist_ok=True)

def authenticate_multiple_users():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)

    while True:
        print("🌐 Opening browser to log in to a Gmail account...")
        creds = flow.run_local_server(port=0)

        # Use Gmail API to get user's email
        service = build('gmail', 'v1', credentials=creds)
        profile = service.users().getProfile(userId='me').execute()
        email_address = profile['emailAddress']

        # Save token file
        token_path = os.path.join(TOKEN_DIR, f"token_{email_address}.json")
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

        print(f"✅ Authenticated {email_address}. Token saved at {token_path}")

        next_user = input("Do you want to add another Gmail account? (y/n): ").strip().lower()
        if next_user != 'y':
            break
