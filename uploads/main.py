import discord
import os
from commands.utils import hello , ban , kick 
from commands.marketing import trend 
#from commands.marketing import feedback
from commands.marketing import keyword as keyword_module
# from keep_alive import keep_alive

token = os.getenv(token)


intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

PREFIX = "-"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
      return

  content = message.content.split()
  command = content[0]

  if command == f'{PREFIX}hello':
      await hello.say_hello(message)
  elif command == f'{PREFIX}ban':
      if len(content) < 3:
          await message.reply("Please provide a user and a reason.")
      else:
          user_id = content[1].strip('<@!>')  # Extract user ID from mention
          reason = ' '.join(content[2:])      # Combine the rest as reason
          await ban.ban_user(message, int(user_id), reason)
  elif command == f'{PREFIX}kick':
      if len(content) < 3:
        await message.reply("Please provide a user and a reason.")
      else:
        user_id = content[1].strip('<@!>')
        reason = ' '.join(content[2:])
        await kick.kick_member(message, int(user_id), reason)
  elif command == f'{PREFIX}trend':
      content = message.content.split()
      if len(content) < 2:
          await message.reply("Please provide a keyword.")
      else:
          keyword = ' '.join(content[1:])
          await trend.get_trends(message, keyword)

  elif command == f'{PREFIX}feedback':
    content = message.content.split(maxsplit=2)
    if len(content) < 3:
        await message.reply("Please provide a product/service name and feedback.")
    else:
        product_name = content[1]
        feedback_text = content[2]
        await feedback.collect_feedback(message, product_name, feedback_text)

  elif command == f'{PREFIX}keyword':
    args = message.content.split()
    if len(args) < 2:
        await message.reply("Please provide a keyword to search.")
    else:
        keyword_to_search = ' '.join(args[1:])
        await keyword_module.keyword_search(message, keyword_to_search)
        




# keep_alive()
# my_secret = os.environ['BOT_TOKEN']
client.run(token)
