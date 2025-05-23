from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class GmailService:
    def __init__(self, token_path):
        self.creds = Credentials.from_authorized_user_file(token_path)
        self.service = build("gmail", "v1", credentials=self.creds)

    def fetch_messages(self, user_id="me", max_results=25):
        messages = []
        results = self.service.users().messages().list(userId=user_id, maxResults=max_results).execute()

        for msg in results.get('messages', []):
            msg_data = self.service.users().messages().get(userId=user_id, id=msg['id'], format='full').execute()

            headers = msg_data['payload'].get('headers', [])
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")
            sender = next((h['value'] for h in headers if h['name'] == 'From'), "(Unknown Sender)")
            snippet = msg_data.get('snippet', '')

            messages.append({
                'id': msg['id'],
                'subject': subject,
                'from': sender,
                'snippet': snippet
            })

        return messages
