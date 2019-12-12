const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on('voiceStateUpdate', (oldState, newState) => {
  console.log(newState.client.user)
  console.log(newState.streaming)
})

client.login(process.env.DISCORD_TOKEN)
