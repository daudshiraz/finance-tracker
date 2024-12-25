import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
client_id = os.getenv("PLAID_CLIENT_ID")
secret = os.getenv("PLAID_SECRET")
environment = os.getenv("PLAID_ENV")

print(f"PLAID_CLIENT_ID: {client_id}")
print(f"PLAID_SECRET: {secret}")
print(f"PLAID_ENV: {environment}")
