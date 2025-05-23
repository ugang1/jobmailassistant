import os
from backend.gmail_service import GmailService

class GmailManager:
    def __init__(self, token_dir='backend/tokens'):
        self.token_dir = token_dir
        self.accounts = self._load_accounts()

    def _load_accounts(self):
        accounts = {}
        for filename in os.listdir(self.token_dir):
            if filename.endswith(".json"):
                email = filename.replace("token_", "").replace(".json", "")
                token_path = os.path.join(self.token_dir, filename)
                accounts[email] = GmailService(token_path)
        return accounts

    def fetch_all_emails(self, max_results=25):
        all_emails = []
        for email, service in self.accounts.items():
            print(f"🔍 Fetching from {email}")
            messages = service.fetch_messages(max_results=max_results)
            for msg in messages:
                msg['account'] = email
                all_emails.append(msg)
        return all_emails
