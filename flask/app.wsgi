import os
from dotenv import load_dotenv
from app import app  

# Load environment variables
load_dotenv()

app = app

if __name__ == "__main__":
    application.run()
