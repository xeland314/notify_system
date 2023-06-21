import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

print(my_email, my_password)