import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        'backend/credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    print("✅ Auth successful.")
    email = input("Enter the Gmail address you just authenticated: ").strip().lower()
    os.makedirs('backend/tokens', exist_ok=True)
    with open(f'backend/tokens/token_{email}.json', 'w') as token_file:
        token_file.write(creds.to_json())
    print(f"✅ Token saved for: {email}")

if __name__ == '__main__':
    authenticate()
