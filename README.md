🤖 LinkedIn Auto-Accept Agent
This is a simple Python automation agent built using Selenium that automatically logs into your LinkedIn account, navigates to the "My Network" → "Grow" tab, and accepts all pending connection requests.

📌 Features
🔐 Secure login using your LinkedIn credentials

🔄 Automatically navigates to the Grow section

✅ Clicks on all visible "Accept" buttons for connection invitations

♻️ Loops through all invites until none are left

📅 Can be scheduled to run daily via cron on macOS/Linux

📁 Folder Structure
bash
Copy
Edit
linkedin-auto-accept/
├── linkedin_auto_accept.py     # Main automation script
├── .env                        # (Optional) Hidden file to securely store credentials
└── README.md                   # This file
🧑‍💻 Requirements
Python 3.7+

Google Chrome installed

pip packages:

selenium

webdriver-manager

python-dotenv (optional for env-based secrets)

Install them using:

bash
Copy
Edit
pip install selenium webdriver-manager python-dotenv
🔧 Setup Instructions
1. Clone or Download the Repository
bash
Copy
Edit
git clone https://github.com/your-username/linkedin-auto-accept.git
cd linkedin-auto-accept
2. Update Credentials
Option 1: Hardcoded (not recommended for production)

Edit linkedin_auto_accept.py:

python
Copy
Edit
LINKEDIN_USERNAME = "your_email@example.com"
LINKEDIN_PASSWORD = "your_password"
Option 2: Environment File (recommended)

Create a .env file in the root directory:

env
Copy
Edit
LINKEDIN_USERNAME=your_email@example.com
LINKEDIN_PASSWORD=your_password
Update your script to read it:

python
Copy
Edit
from dotenv import load_dotenv
import os

load_dotenv()
LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
▶️ Run It Manually
bash
Copy
Edit
python3 linkedin_auto_accept.py
🕒 Automate with Cron (macOS/Linux)
To run the script daily at 10:00 AM, open Terminal:

bash
Copy
Edit
crontab -e
Add the following line (replace the path with yours):

bash
Copy
Edit
0 10 * * * /usr/bin/python3 /Users/your_username/path/to/linkedin_auto_accept.py
To check if it’s set:

bash
Copy
Edit
crontab -l
🛑 Known Limitations
LinkedIn may block or limit activity if automation is abused.

ChromeDriver version must match your installed Chrome version.

UI layout changes on LinkedIn could break the script.

🛡️ Safety Tips
Don’t share your credentials or .env file.

Use 2FA and app passwords if possible.

Monitor your account regularly for suspicious activity.

📌 Future Improvements
Dockerize the agent

Add support for headless browser

Turn into a tray/desktop app

Deploy to the cloud with GitHub Actions or AWS Lambda

🙌 Credits
Created by [Your Name]
Feel free to fork, star, or contribute!

