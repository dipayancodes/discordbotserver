# Inside commands/utils/ban.py
async def ban_user(message, user, reason):
    guild = message.guild
    member = guild.get_member(user)
    if member:
        await member.ban(reason=reason)
        await message.reply(f"{member.name} has been banned for {reason}.")
    else:
        await message.reply("User not found.")