import ssl
import socket
import requests
import json
import os
from datetime import datetime

# Read domains and Slack webhook from environment variables
DOMAINS = os.getenv("DOMAINS", "").split(",")  # Read as a list
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
DAYS_LEFT_LIST = list(map(int, os.getenv("DAYS_LEFT", "").split(",")))  # Read as a list of integers
print(DAYS_LEFT_LIST)

# Function to check SSL expiry
def check_cert_expiry(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            days_left = (expiry_date - datetime.now()).days
            return days_left, expiry_date

# Check each domain and prepare alerts
expiring_domains = []
for domain in DOMAINS:
    domain = domain.strip()  # Clean up whitespace
    if not domain:
        continue  # Skip empty entries

    try:
        days_left, expiry_date = check_cert_expiry(domain)
        print(f"{domain} expires in {days_left} days on {expiry_date}")

        if days_left in DAYS_LEFT_LIST:
            expiring_domains.append(f"*{domain}* expires in `{days_left} days` on `{expiry_date}`")
    except Exception as e:
        print(f"Error checking {domain}: {e}")

# Send Slack notification if any certificates are expiring
if expiring_domains and SLACK_WEBHOOK_URL:
    slack_message = {
        "text": ":warning: *SSL Certificate Expiry Alert* :warning:\n\n" + "\n".join(expiring_domains),
        "username": "SSL Monitor",
        "icon_emoji": ":lock:",
    }
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(slack_message), headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        print("Slack notification sent successfully.")
    else:
        print(f"Failed to send Slack notification: {response.text}")
