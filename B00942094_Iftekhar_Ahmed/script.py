from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def run():
    return f"username:{USERNAME}\npassword:{PASSWORD}"

print(run())

