import os
import base64
import pickle
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If no valid credentials, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def fetch_recent_email_list(n=5):
    service = get_service()
    results = service.users().messages().list(userId='me', maxResults=n).execute()
    messages = results.get('messages', [])
    email_list = []

    for msg in messages:
        msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_detail.get('snippet', '')
        payload = msg_detail.get("payload", {})
        headers = payload.get("headers", [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        email_list.append({
            "id": msg['id'],
            "subject": subject,
            "snippet": snippet
        })
    return email_list

def fetch_email_by_id(msg_id):
    service = get_service()
    message = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    parts = message['payload'].get('parts', [])
    body = ""
    for part in parts:
        if part['mimeType'] == 'text/html':
            data = part['body']['data']
            html = base64.urlsafe_b64decode(data.encode('UTF-8')).decode('utf-8')
            body = BeautifulSoup(html, 'html.parser').get_text()
            break
        elif part['mimeType'] == 'text/plain':
            body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
            break
    return body
