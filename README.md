# Slack Sign-up Sheet Automation

An automated scheduling system designed for managing recurring time slots in Slack channels. Specifically built for:
- Managing weekly volunteer schedules
- Coordinating recurring team meetings
- Organizing office hours or support slots
- Handling regular resource booking
- Automating attendance tracking

Features
- Posts weekly schedule templates automatically
- Customizable time slots for Thursday and Friday
- Thread-based response system for organization
- Emoji reaction-based sign-up system (✅)
- Automatic setup and cleanup slot assignment
- Persistent schedule tracking
- User-friendly interface

Setup
1. Install required packages:
   pip install -r requirements.txt

2. Create .env file with:
   SLACK_USER_TOKEN=xoxb-your-token
   CHANNEL_ID=your-channel-id

3. Configure schedule in slackSignUp.py:
   - Default slots: 11:00-14:00 in 30-minute intervals
   - Setup time: 10:30
   - Cleanup time: 14:00
   - Custom message formatting
   - Schedule posting timing

Usage
Run manually:
python3 slackSignUp.py

Run with test mode (posts test messages):
python3 slackSignUp.py --test

Auto-start (using systemd):
1. Create service file:
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

2. Enable and start:
   sudo systemctl enable slack-signup
   sudo systemctl start slack-signup

Logging
- Console output for immediate feedback
- slack_signup.log file for historical tracking
- Includes posting success/failure
- Tracks user interactions
- Records schedule changes

Schedule Format
- Thursday and Friday schedules
- 30-minute time slots
- Dedicated setup/cleanup slots
- Automatic @mentions for setup
- Clear visual formatting
- Emoji-based status indicators

License
MIT License