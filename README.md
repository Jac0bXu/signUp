# Slack Sign-up Sheet Automation

A Python script that automatically posts weekly sign-up sheets to a Slack channel. Perfect for managing recurring events or schedules.

## Features

- Automated weekly posting
- Threaded messages for better organization
- Configurable scheduling
- Test mode for verification
- Detailed logging

## Prerequisites

- Python 3.6+
- Slack workspace with admin privileges
- Slack Bot Token with appropriate permissions

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/signup.git
   cd signup

2. Install required dependencies:
   pip install -r requirements.txt

3. Create a .env file in the project root with your Slack credentials:
   SLACK_USER_TOKEN=xoxb-your-token-here
   CHANNEL_ID=C0123456789

## Slack Setup

1. Create a Slack App at api.slack.com/apps
2. Add the following OAuth scopes:
   - chat:write
   - channels:read
3. Install the app to your workspace
4. Copy the Bot User OAuth Token to your .env file

## Usage

Running in Normal Mode:
python slackSignUp.py

Running in Test Mode:
python slackSignUp.py --test

Server Deployment:
1. Make the script executable:
   chmod +x slackSignUp.py

2. Create a systemd service file /etc/systemd/system/slack-signup.service:
   [Unit]
   Description=Slack Sign-up Sheet Automation
   After=network.target

   [Service]
   Type=simple
   User=yourusername
   WorkingDirectory=/path/to/signup
   Environment=PYTHONUNBUFFERED=1
   ExecStart=/usr/bin/python3 /path/to/signup/slackSignUp.py
   Restart=always

   [Install]
   WantedBy=multi-user.target

3. Start and enable the service:
   sudo systemctl start slack-signup
   sudo systemctl enable slack-signup

## Customization

You can modify the following in slackSignUp.py:
- Message content in regular_messages list
- Scheduling time (weekday, hour, minute)
- Message formatting and emojis

## Logging

Logs are written to:
- Console output
- slack_signup.log file in the project directory

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request