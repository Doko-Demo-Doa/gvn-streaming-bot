import os
import discord
import settings
import asyncio

# ln -s $(which node) /usr/local/bin/node
from typing import List
from discord import utils, Client, Guild, Member, VoiceState, Role

SERVER_ID = 249438409024733184
STREAM_ROLE_ID = 652101620728856576

active_streamers = []

client: Client = Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

async def check_role(guild: Guild):
  stream_role = utils.get(guild.roles, id = STREAM_ROLE_ID)
  for streamer in active_streamers:
    try:
      if (streamer.voice.self_stream == False):
        await streamer.remove_roles(stream_role)
    except AttributeError:
      await streamer.remove_roles(stream_role)

async def check_voice(guild: Guild):
  stream_role = utils.get(guild.roles, id = STREAM_ROLE_ID)
  for voice_channel in guild.voice_channels:
    for voice_member in voice_channel.members:
      # If streaming
      if voice_member.voice.self_stream == True:
        for (role) in voice_member.roles:
          # If already set stream role.
          if role.id == STREAM_ROLE_ID:
            break
          await voice_member.add_roles(stream_role)
          if voice_member not in active_streamers:
            active_streamers.append(voice_member)

async def background_task():
  await client.wait_until_ready()
  guild = client.get_guild(SERVER_ID)
  print(guild)
  for member in guild.members:
    for role in member.roles:
      if role.id == STREAM_ROLE_ID:
        active_streamers.append(member)
        break
  while not client.is_closed():
    await check_role(guild)
    await check_voice(guild)

    await asyncio.sleep(30)

@client.event
async def on_voice_state_update(member: Member, before: VoiceState, after: VoiceState):
  stream_role_ref: Role = discord.utils.get(member.guild.roles, id = STREAM_ROLE_ID)

  if (after.self_stream == True):
    await member.add_roles(stream_role_ref)
    if member not in active_streamers:
      active_streamers.append(member)
    return
  if (after.self_stream == False):
    await member.remove_roles(stream_role_ref)
    if member in active_streamers:
      active_streamers.remove(member)
    return

client.loop.create_task(background_task())
client.run(os.getenv("DISCORD_TOKEN"))