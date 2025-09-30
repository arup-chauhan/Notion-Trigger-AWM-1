import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()  # load variables from .env

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

today = datetime.date.today().isoformat()

data = {
    "parent": {"database_id": DATABASE_ID},
    "properties": {


        # Date
        "Date": {"date": {"start": today}},

        # Number fields
        "Cash In": {"number": 0},
        "Cash Out": {"number": 0},

        # Text fields
        "Purpose of Out": {"rich_text": [{"text": {"content": "N/A"}}]},
        "Purpose of In": {"rich_text": [{"text": {"content": "N/A"}}]},

        # Account info
        "Account From": {"rich_text": [{"text": {"content": "N/A"}}]},
        "Account To": {"rich_text": [{"text": {"content": "N/A"}}]},

        # Title field
        "Transaction Type": {
            "title": [{"text": {"content": f"Daily Cash Flow – {today}"}}]
        },

    }
}

res = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
print(res.status_code, res.text)
