import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# retrieving keys and adding them to the project
# from the .env file through their key names
SECRET_KEY = os.getenv("SECRET_KEY")
DOMAIN = os.getenv("DOMAIN")
EMAIL = os.getenv("EMAIL")

print(f"{SECRET_KEY = }")
print(f"{DOMAIN = }")
print(f"{EMAIL = }")
