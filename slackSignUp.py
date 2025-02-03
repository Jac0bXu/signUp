import time
from slack_sdk import WebClient
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import argparse
import logging

# Load environment variables
load_dotenv()

def send_weekly_messages(token, channel_id, messages, weekday, hour, minute, test_mode=False):
    """
    Send messages to Slack channel at a specific time each week, with replies in thread
    
    Args:
        token (str): User's Slack OAuth token
        channel_id (str): Target channel ID
        messages (list): List of messages to send (first message is parent, rest are replies)
        weekday (int): Day of week (0=Monday, 6=Sunday)
        hour (int): Hour to send (24-hour format)
        minute (int): Minute to send
        test_mode (bool): If True, sends messages immediately
    """
    client = WebClient(token=token)
    
    def get_next_run_time():
        now = datetime.now()
        target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        
        # Calculate days until target weekday
        days_ahead = weekday - now.weekday()
        
        # If we've already passed the target time today, start counting from tomorrow
        # if now.weekday() == weekday and now >= target_time:
        #     days_ahead += 7
        # # If we've passed the target weekday this week, wait for next week
        # elif days_ahead <= 0:
        #     days_ahead += 7
            
        next_run = target_time + timedelta(days=days_ahead)
        print(f"Current time: {now}")
        print(f"Target weekday: {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][weekday]}")
        print(f"Target time: {hour:02d}:{minute:02d}")
        print(f"Next scheduled run: {next_run}")
        
        return next_run
    
    while True:
        if test_mode:
            send_time = datetime.now()
        else:
            send_time = get_next_run_time()
            print(f"Next message scheduled for: {send_time}")
            
            # Wait until scheduled time
            while datetime.now() < send_time:
                time.sleep(30)
        
        try:
            # Send the parent message first
            parent_response = client.chat_postMessage(
                channel=channel_id,
                text=messages[0]
            )
            print(f"Parent message sent at {datetime.now()}: {messages[0]}")
            
            # Get the timestamp of the parent message for threading
            thread_ts = parent_response['ts']
            
            # Send the rest of the messages as replies
            for message in messages[1:]:
                time.sleep(1)  # Small delay between messages
                response = client.chat_postMessage(
                    channel=channel_id,
                    thread_ts=thread_ts,  # This makes it a reply
                    text=message
                )
                print(f"Reply sent at {datetime.now()}: {message}")
                
        except Exception as e:
            print(f"Error sending message: {str(e)}")
            print(f"Channel ID used: {channel_id}")
            print(f"Token type: {token[:4]}...")
        
        if test_mode:
            break
            
        # Wait for next week
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('slack_signup.log'),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)

    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Slack Sign-up Sheet Automation')
    parser.add_argument('--test', action='store_true', help='Run in test mode')
    args = parser.parse_args()

    # Load environment variables
    USER_TOKEN = os.environ.get('SLACK_USER_TOKEN')
    CHANNEL_ID = os.environ.get('CHANNEL_ID')
    
    if not USER_TOKEN or not CHANNEL_ID:
        logger.error("Please set SLACK_USER_TOKEN and CHANNEL_ID in .env file")
        raise ValueError("Please set SLACK_USER_TOKEN and CHANNEL_ID in .env file")
    
    # Test messages
    test_messages = [
<<<<<<< HEAD
        "🧪 Weekly Update Test (Parent Message)::::",
=======
        "🧪 <!channel> Weekly Update Test (Parent Message)",
>>>>>>> 47e8daf5bf735f57864b3a099024eac4d0a701d4
        "🧪 First reply in thread",
        "🧪 Second reply in thread",
        "• 11：00-11：30",
        "🧪 Final reply in thread"
    ]
    
    # Regular messages
    regular_messages = [
        "📅 <!channel> Thursday and Friday Sign-up Sheet",
        "🗓️ *Thursday Schedule:*",
        "• 10:30 - Setup @bechtel",
        "• 11:00-11:30",
<<<<<<< HEAD
        "• 11:30-12:00",
=======
        "• 11:30-12:00", 
>>>>>>> 47e8daf5bf735f57864b3a099024eac4d0a701d4
        "• 12:00-12:30",
        "• 12:30-1:00",
        "• 1:00-1:30",
        "• 1:30-2:00",
        "• 2:00 - Clean up",
        "🗓️ *Friday Schedule:*",
        "• 10:30 - Setup @bechtel",
        "• 11:00-11:30",
        "• 11:30-12:00",
<<<<<<< HEAD
        "• 12:00-12:30",
=======
        "• 12:00-12:30", 
>>>>>>> 47e8daf5bf735f57864b3a099024eac4d0a701d4
        "• 12:30-1:00",
        "• 1:00-1:30",
        "• 1:30-2:00",
        "• 2:00 - Clean up",
        "Please react with ✅ to sign up for your preferred time slots!"
    ]
    
    if args.test:
        logger.info("Running in test mode - messages will be sent immediately")
        send_weekly_messages(
            token=USER_TOKEN,
            channel_id=CHANNEL_ID,
            messages=test_messages,
            weekday=0,  # Monday

            hour=10,    # 10 AM
            minute=0,   # 0 minutes
            test_mode=True
        )
    else:
        logger.info("Running in scheduled mode - messages will be sent every Monday at 10:00 AM")
        send_weekly_messages(
            token=USER_TOKEN,
            channel_id=CHANNEL_ID,
            messages=regular_messages,
<<<<<<< HEAD
            weekday=0,  # Monday
            hour=20,    # 10 AM
            minute=1,   # 0 minutes
=======
            weekday=1,  # Monday
            hour=21,    # 10 AM
            minute=49,   # 0 minutes
>>>>>>> 47e8daf5bf735f57864b3a099024eac4d0a701d4
            test_mode=False
        )
