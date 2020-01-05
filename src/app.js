const Discord = require('discord.js')
const _ = require('lodash')
const client = new Discord.Client()

const { concat, uniq } = _

client.on('ready', (a) => {
  console.log(`Logged in as ${client.user.tag}!`)
  client.user.setActivity('Pin, Bet, Streaming notification bot')
})

const STREAMING_ROLE_ID = '652101620728856576'
client.on('voiceStateUpdate', (oldState, newState) => {
  const targetRole = newState.guild.roles.find(n => n.id === STREAMING_ROLE_ID)
  // targetRole.members.forEach(n => {
  //   if (!n.voice.streaming) {
  //     n.edit.edit({
  //       roles: n.roles.filter(o => o.id !== STREAMING_ROLE_ID).map(n => n.id)
  //     })
  //   }
  // })

  if (!targetRole) return

  if (newState.streaming) {
    // Đang stream, set role.
    newState.member.edit({
      roles: uniq(concat(newState.member.roles.map(n => n.id), targetRole.id))
    }).then((r) => {
      // console.log(r)
    }).catch(_ => {
      // console.log(_)
    })
  } else {
    newState.member.edit({
      roles: newState.member.roles.filter(o => o.id !== STREAMING_ROLE_ID).map(n => n.id)
    }).then((r) => {
      // console.log(r)
    }).catch(_ => {
      // console.log(_)
    })
  }
})

client.login(process.env.DISCORD_TOKEN)
