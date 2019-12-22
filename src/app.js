const Discord = require('discord.js')
const _ = require('lodash')
const client = new Discord.Client()

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

const STREAMING_ROLE_ID = '652101620728856576'
client.on('voiceStateUpdate', (oldState, newState) => {
  const targetRole = newState.guild.roles.find(n => n.id === STREAMING_ROLE_ID)

  if (newState.member.displayName !== 'Doko') return
  if (!targetRole) return

  if (newState.streaming) {
    // Đang stream, set role.
    newState.member.edit({
      roles: _.concat(newState.member.roles.map(n => n.id), targetRole.id, n => n)
    }).then((r) => {
      // console.log(r)
    }).catch(_ => {
      // console.log(_)
    })
  } else {
    newState.member.edit({
      roles: newState.member.roles.filter(o => o.id !== STREAMING_ROLE_ID)
    }).then((r) => {
      // console.log(r)
    }).catch(_ => {
      // console.log(_)
    })
  }
})

client.login(process.env.DISCORD_TOKEN)
