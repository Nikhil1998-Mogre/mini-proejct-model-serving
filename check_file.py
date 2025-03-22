import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the value of DAGSHUB_PAT
dagshub_pat = os.getenv("DAGSHUB_PAT")

# Print the value (be cautious when printing secrets)
print(f"DAGSHUB_PAT: {dagshub_pat}")
