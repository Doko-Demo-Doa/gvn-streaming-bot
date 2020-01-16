import os
import discord
import settings

class GVNStream(discord.Client):
  async def on_ready(self):
    print('Logged in:', self.user)

  async def on_voice_state_update(x, member, before, after):
    print(member.display_name, after.self_stream)

client = GVNStream()
client.run(os.getenv("DISCORD_TOKEN"))