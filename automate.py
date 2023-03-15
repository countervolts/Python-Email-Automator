import os
import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', credentials=creds)

with open('login.json', 'r') as f:
    lines = f.readlines()
    email = lines[0].strip()
    password = lines[1].strip()

try:
    service.users().messages().list(userId='me').execute()
except HttpError as error:
    print(f'An error occurred: {error}')
    exit()

with open('list.txt', 'r') as f:
    emails = [line.strip() for line in f.readlines()]

message = f"""\
From: {email}
To: {", ".join(emails)}
Subject: Test email
Hello,

This is a test email sent using the Gmail API.

Regards,
{email.split('@')[0]}
"""
message_bytes = message.encode('utf-8')
message_b64 = base64.urlsafe_b64encode(message_bytes).decode('utf-8')

try:
    message = service.users().messages().send(
        userId='me',
        body={'raw': message_b64}
    ).execute()
    print(f'The email was sent to {", ".join(emails)}')
except HttpError as error:
    print(f'An error occurred: {error}')
