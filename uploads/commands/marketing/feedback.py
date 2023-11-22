# commands/marketing/feedback.py

import discord
import json
from pathlib import Path

# File where feedback will be stored
FEEDBACK_FILE = Path('commands/marketing/feedback_record/feedback.json')

# Make sure the feedback directory exists
FEEDBACK_FILE.parent.mkdir(exist_ok=True)

def save_feedback(product_name, user, feedback_text):
    feedback_data = {}

    # Load existing feedback data if file exists
    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, 'r', encoding='utf-8') as file:
            feedback_data = json.load(file)

    # Append new feedback
    if product_name not in feedback_data:
        feedback_data[product_name] = []
    feedback_data[product_name].append({'user': user, 'feedback': feedback_text})

    # Save updated feedback data
    with open(FEEDBACK_FILE, 'w', encoding='utf-8') as file:
        json.dump(feedback_data, file, ensure_ascii=False, indent=4)

async def collect_feedback(message, product_name, feedback_text):
    try:
        # Save the feedback
        save_feedback(product_name, str(message.author), feedback_text)

        # Send confirmation message
        await message.reply(f"Feedback for {product_name} has been recorded.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

# Example usage
# await collect_feedback(message, 'shoes', 'It\'s very good.')
