from keep_alive import keep_alive
keep_alive()
import discord
import os
import time 
import asyncio
from discord.ext import commands
from discord.ext import tasks
import urllib.request
import urllib.error
import discord, aiofiles
import choice
import random
from discord import Embed, TextChannel
from asyncio import sleep
import datetime
import re 
import json
from requests import get

intents = discord.Intents.default()
intents.members = True
      
client=commands.Bot(command_prefix='K.')
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in: ', client.user) # show on console 
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Prefix the bot with K. | Min chó rách , Makubé là thằng vô danh nào?'))


@client.command(pass_context=True)
async def report(ctx, *, text = None):
    if isinstance(ctx.channel, discord.DMChannel):
        if text is None:
            await ctx.author.send("```Usage: K.report [content]```")
        else:
            admin_channel = client.get_channel(1000669961250951258) # Channel ID
            await admin_channel.send("@everyone **{}**({}) : {}".format(ctx.author, ctx.author.id, text))
            await ctx.author.send("**INFO:** A message was sent to the server administrator.")
    else:
        await ctx.message.delete()
        await ctx.author.send("**ERROR:** The report command is only available on the DM channel.\nPlease re-enter the command here.\n**You Entered:**\n```!report {}```".format(text))

  
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name="Help everywhere is server , not commands for bot ! ")
    embed.add_field(name='Pick roles who ?',value='Pick roles at : [Roles](https://discord.com/channels/999466665337172008/999490557351035050/1000103099383419001)',inline=False)
    embed.add_field(name='Things you should know about the server :',value='Our server here : [Click me !](https://discord.com/channels/999466665337172008/999494996996657263/1000398232960118804)',inline=False)
    embed.add_field(name='Reading the rules server importan !',value='Rules? [Click me !](https://discord.com/channels/999466665337172008/999496443394003105/1000139451969843200)',inline=False)
    embed.add_field(name='You need help ?',value='Click for support [Click me !](https://discord.com/channels/999466665337172008/1000121020163821628/1000122014167728340)',inline=False)
    embed.add_field(name='Cant u with partner ?',value='Partner ? [Click me !](https://discord.com/channels/999466665337172008/999644184187252758/1000090636478849155)',inline=False)
    await ctx.author.send(embed=embed)
    await ctx.reply("I will dms you ,  check your dms ! <:loading:1000960051969798155>")

@client.command(pass_context=True)
async def nick(ctx, *, nickname):
    try:
        await ctx.message.delete()
        await ctx.author.edit(nick=nickname)
    except discord.errors.Forbidden:
        await ctx.author.send("**ERROR:** `I CANNOT CHANGE YOUR NAME`")
    else:
        await ctx.author.send("**INFO:** Your nickname has been changed.")
        time.sleep(7)


@client.command(pass_context=True)
async def ping(ctx):
    if round(client.latency * 1000) <= 50: 
      embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
      (ctx.message.author.mention) 
      time.sleep(7)
      
      embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0xffd000)
    elif round(client.latency * 1000) <= 200:
    
      
      embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!😂", color=0xff6600)
    else:
      
      embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!😂", color=0x990000)
    await ctx.send(embed=embed)
    (ctx.message.author.mention)
    time.sleep(7)
  
@client.command(alaises=['Kick'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'''<:users:1001022609284145192> `{member}`\n<:arrow:1001022518888497172> **User has been kicked !** <:kicked:1001029295956836442> \n<:moderators:1000965404375654430> Moderators : **{ctx.author}**\n <:arrow:1001022518888497172> <:reason:1001030794761998346> Reason : {reason}\n<:done:1000941947613102160>  All user Successfully kicked ! ''')
    await ctx.message.delete()
    time.sleep(5)
    
{}
@client.command(alaises=['Ban'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, *, member_id: int):
    """ command to ban user. check K.ban to ban """
    await ctx.guild.unban(discord.Object(id=member_id))
    await User.ban(reason=reason)
    await ctx.send(f'''<:users:1001022609284145192> `{user}`\n<:arrow:1001022518888497172> `User has been banned !`<:target:1001023664449400872>\n<:moderators:1000965404375654430> Moderators :  **{ctx.author}**\n<:right:1000941861625667675> <:reason:1001030794761998346> Reason : {reason}\n<:done:1000941947613102160> **All user Successfully banned !** <:target:1001023664449400872> ''')
    await ctx.message.delete()


@client.command(name="unban", help="command to unban user")
@commands.has_permissions(ban_members=True)
async def _unban(ctx, *, member_id: int):
    """ command to unban user. check K.help unban """
    await ctx.guild.unban(discord.Object(id=member_id))
    await ctx.reply(f"<:done:1000941947613102160> `Successfully unban :`\n<:users:1001022609284145192> `USER ID :` **{member_id}**")


@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False,
                                          read_message_history=False,
                                          read_messages=False)
    embed = discord.Embed(
        title=" <:target:1001023664449400872> `USER  HAS BEEN TIME OUT !!`",
        description=f"**{member}**' `You have been muted!` <:muted:1001022388537925653>  ",
        colour=discord.Colour.light_gray())
    embed.add_field(name=" ☣️ Reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(
        f" <:target:1001023664449400872> **You have been muted from:** {guild.name} <:right:1000941861625667675> `Reason:` <:right:1000941861625667675> {reason}")
    time.sleep(7)


@client.command()
async def warn(ctx, member: discord.Member=None):
  if member == None:
    await ctx.send('Mention a member')
    return
  try:
    for a in range(1):
      await member.send("<:arrow:1001022518888497172> `You has been warned ! You need reading rules so as not to be warned anymore !!`")

  except commands.CommandInvokeError:
      await ctx.reply("Couldn't send message to user") 


  except commands.CommandInvokeError:
      await ctx.reply("Couldn't send message warn to user")

  except commands.CommandInvokeError:
      await ctx.send("Couldn't send message to user")
      await ctx.message.delete()

@client.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f"{text}")
    await ctx.message.delete()

@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, amount):        
    try:
        await ctx.message.delete()
        await ctx.channel.edit(reason='Bot Slowmode Command', slowmode_delay=int(amount))
    except discord.Errors.Forbidden:
        await ctx.reply('I do not have the permission to do this, please try again <:unsuccessful:1000942453932703886>')
        

@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, limit=500, member: discord.Member=None):
    await ctx.message.delete()
    msg = []
    try:
        limit = int(limit)
    except:
        return await ctx.send("Please pass in an integer as limit <:unsuccessful:1000942453932703886>")
    if not member:
        await ctx.channel.purge(limit=limit)
        return await ctx.send(f"<:arrow:1001022518888497172> `Purged {limit} messages successfully !`  <:done:1000941947613102160>", delete_after=3)
    async for m in ctx.channel.history():
        if len(msg) == limit:
            break
        if m.author == member:
            msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=3)
    await ctx.message.delete()
    time.sleep(5)


@client.command(brief='Allows you to steal an emoji', description='Will return the image file for a requested emoji', usage='[emoji](can be from anywhere and animated if you have nitro)')
@commands.has_permissions(administrator=True)
async def steal(ctx, emoji: discord.PartialEmoji):
       await ctx.send(emoji.url)

          
@client.event
async def on_message_delete(message):
    if len(message.mentions) == 0:
        return
    else:
        print(message.author.name)
        ghostping = discord.Embed(title=f'**Detect ghost ping**<:ping:1000960180609089546>', color=0x50E9FF, timestamp=message.created_at)
        ghostping.add_field(name=' <:target:1001023664449400872> **Name:**', value=f'{message.author} ({message.author.id})')
        ghostping.add_field(name=' <:target:1001023664449400872> **Message:**', value=f'{message.content}')
        ghostping.set_thumbnail(
            url='https://media.discordapp.net/attachments/999525220866072616/1000699650564689950/Koaede-Inazumi-Acr8X4jB4C2BsUQqMD13mG.html.png')
        try:
            await message.channel.send(embed=ghostping)
        except discord.Forbidden:
            try:
                await message.author.send(embed=ghostping)
            except discord.Forbidden:
                return

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")


@client.command()
@commands.has_permissions(manage_messages=True)
async def react(ctx,emoji,message_id):
  channel = ctx.channel
  msg = await channel.fetch_message(message_id)
  await msg.add_reaction('<:done:1000941947613102160>','<:unsuccessful:1000942453932703886>')

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"<:users:1001022609284145192> `User Info` : {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f" ✅️ Requested by {ctx.author}")

    embed.add_field(name="<:user:1000967252457308211> `USER ID:`", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name=" <:user:1000967252457308211> `Created Account On:`", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name=" <:user_invites:1001020217503252490> `Joined Server On:`", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=" <:roles:1001020695460986980> `Roles:`", value="".join([role.mention for role in roles]))
    embed.add_field(name=" <:roles_dangerous:1001021902652981248> `Highest Role:`", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


hug_gifs = ['https://c.tenor.com/nHkiUCkS04gAAAAC/anime-hug-hearts.gif','https://gifer.com/en/2QEa','https://gifer.com/en/WDf','https://gifer.com/en/SKwW','https://gifer.com/en/79o1']
hug_names = ['Hugs you!','Love you !','hug !','so you cute !'] 


@client.command()
async def hug(ctx):
    embed = discord.Embed (
        colour=(discord.Colour.red()),
        description = f"{ctx.author.mention} {(random.choice(hug_names))}"
    )
    embed.set_image(url=(random.choice(hug_gifs)))


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f'''<:right:1000941861625667675> `Successfully lockdown channels`  <:done:1000941947613102160> ''')
 
   
@lock.error
async def lock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.reply(f'''<:unsuccessful:1000942453932703886> `YOU DO NOT PERMISSIONS TO USE COMMAND !`''')

@client.command()
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'<:arrow:1001022518888497172> `Successfully create role`\n<:right:1000941861625667675> `Role name :` {name}\n<:done:1000941947613102160> `All roles has been successfully create !`')

@client.command()
@commands.has_permissions(manage_channels=True)
async def channel(ctx, channel_name):
    await ctx.guild.create_text_channel(channel_name)
    await ctx.reply(f'''<:right:1000941861625667675> `Successfully create channel !` \n<:arrow:1001022518888497172> `Channel name :` **{channel_name}**\n<:done:1000941947613102160> `All channels was create successfully !`''')


@client.command()
@commands.has_permissions(manage_channels=True)
async def delvoice(ctx, *, channel_id: int):
    channel = client.get_channel(channel_id)
    await channel.delete()
    await ctx.message.delete()
    await ctx.send("<:check:1000938462905630750> `Successfully deleted the channel!`")
     

@client.command()
@commands.has_permissions(manage_channels=True)
async def delchannel(ctx, channel: discord.TextChannel):
    await ctx.message.delete()
    await channel.delete()
    await ctx.send("<:check:1000938462905630750> `Successfully deleted the channel!`")

@client.command()
async def avatar(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.reply(userAvatar)


client.sniped_messages = {}
@client.event
async def on_message_delete(message):
    if message.attachments:
        bob = message.attachments[0]
        client.sniped_messages[message.guild.id] = (bob.proxy_url, message.content, message.author, message.channel.name, message.created_at)
    else:
        client.sniped_messages[message.guild.id] = (message.content,message.author, message.channel.name, message.created_at)

@client.command()
async def snipe(ctx):
    try:
        bob_proxy_url, contents,author, channel_name, time = client.sniped_messages[ctx.guild.id]
    except:
        contents,author, channel_name, time = client.sniped_messages[ctx.guild.id]
    try:
        embed = discord.Embed(description=contents , color=discord.Color.blue(), timestamp=time)
        embed.set_image(url=bob_proxy_url)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Messages Deleted In : {channel_name}")
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(description=contents , color=discord.Color.blue(), timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Messages Deleted In : {channel_name}")
        await ctx.channel.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def hackban(ctx, *, member_id: int):
    """ command to ban user. check K.help ban """
    await ctx.guild.ban(discord.Object(id=member_id))
    await ctx.reply(f"<:done:1000941947613102160> `Successfully banned :`\n<:users:1001022609284145192> `USER :` **{member_id}**\n<:right:1000941861625667675> `All user has been banned successfully !` <:done:1000941947613102160> ")

#meme xam cac
@client.command()
async def meme(ctx):
    data = get("https://meme-api.herokuapp.com/gimme").json()
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)


@client.event
async def on_member_join(member):
	channel = client.get_channel(999466666238939239) #channel_id of the channel you want the message to be displayed

	embed = discord.Embed(title= f"WELCOME TO **{member.guild.name}**", description= f"WELCOME TO OUR SERVER {member.mention}! HOPE YOU ENJOY HERE!", colour = discord.Colour.blue())
	embed.add_field(name = f"READ ALL THE RULES FROM :", value = f"<#999496443394003105>", inline = False)
	embed.add_field(name = f"TO GET TO KNOW ABOUT THE SERVER :", value = f"<#999494996996657263>", inline = False)
	embed.set_footer(text = "<guild_name> OFFICIAL BOT")
	embed.set_thumbnail(url = member.avatar_url)#any sort of embeds can be used, I use this one

	await channel.send(embed = embed)


keep_alive()
client.run(os.getenv('token'))