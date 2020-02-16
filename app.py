import os
import discord
import settings

SERVER_ID = '479131273537912846'
STREAM_ROLE_ID = '666132535650287626'

active_streamers = []

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_voice_state_update(member, before, after):
  print(member.display_name, after.self_stream)
  stream_role_ref = discord.utils.get(member.guild.roles, id = STREAM_ROLE_ID)
  print(stream_role_ref)

  if (after.self_stream == True):
    await member.add_roles(stream_role_ref)
    return
  if (after.self_stream == False):
    await member.remove_roles(stream_role_ref)

def check_fault_role():
  print('x')

client.run(os.getenv("DISCORD_TOKEN"))