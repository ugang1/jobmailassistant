from backend.gmail_manager import GmailManager

manager = GmailManager()
emails = manager.fetch_all_emails(max_results=25)

print("\n📬 Filtered Job-Related Emails Across Accounts:\n")
for msg in emails:
    print(f"Account: {msg['account']}")
    print(f"From: {msg['from']}")
    print(f"Subject: {msg['subject']}")
    print(f"Snippet: {msg['snippet'][:100]}...\n")
    print("-" * 50)
