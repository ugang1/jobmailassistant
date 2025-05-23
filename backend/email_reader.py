import os
import json
from typing import List
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Keywords to filter job-related emails
KEYWORDS = ["interview", "job", "application", "resume", "hiring", "offer","Data Analyst","Business Analyst","Bi Developer" ,"opportunity"]

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
TOKEN_DIR = os.path.join(os.path.dirname(__file__), "tokens")

def load_token(email: str):
    token_path = os.path.join(TOKEN_DIR, f"token_{email}.json")
    if not os.path.exists(token_path):
        raise FileNotFoundError(f"No token found for {email}")
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    return creds

def fetch_job_emails(email: str) -> List[dict]:
    creds = load_token(email)
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', maxResults=25).execute()
    messages = results.get('messages', [])

    job_emails = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
        snippet = msg_data.get('snippet', '')

        # Keyword filter (subject or snippet)
        if any(kw.lower() in (subject + snippet).lower() for kw in KEYWORDS):
            job_emails.append({
                "subject": subject,
                "from": sender,
                "snippet": snippet,
                "source_email": email
            })

    return job_emails
