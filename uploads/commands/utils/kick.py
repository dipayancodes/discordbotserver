# Inside commands/utils/kick.py
async def kick_member(message, user, reason):
    guild = message.guild
    member = guild.get_member(user)
    if member:
        await member.kick(reason=reason)
        await message.channel.send(f"{member.name} has been kicked for {reason}.")
    else:
        await message.channel.send("User not found.")
