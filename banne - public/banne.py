import discord
import asyncio
client = discord.Client()
async def my_background_task():
    await client.wait_until_ready()
    counter = True
    channel = discord.Object(id='channel_id_here')
    while not client.is_closed:
        await client.change_presence(game=discord.Game(name="with -banne"),status=discord.Status.online, afk=False)
        await asyncio.sleep(10) # task runs every 60 seconds
@client.event
async def on_ready():
    print('Logged in as')
    print("THIS IS BANNE BOT PUBLIC")
    print(client.user.id)
    print('------')
@client.event
async def on_message(message):
    if message.content.startswith("-banne"):
        for member in message.server.members:    
            if member.mentioned_in(message):
                if member == message.author:
                    et_embed = discord.Embed(title="No.", type="rich", description="You can't banne:tm: yourself, silly.", color=discord.Color.dark_red())
                    et_embed.set_footer(text="banneTM bot was coded by lmgn", icon_url="https://i.imgur.com/3G99xcd.png")
                    et_embed.set_author(name="banneTM bot", url="https://thelmgn.com",icon_url="https://steamdb.info/static/img/banhammer.png")
                    await client.send_message(message.channel, embed=et_embed)
                elif member.id == 158311402677731328:
                    et_embed = discord.Embed(title="No.", type="rich", description="I refuse.", color=discord.Color.dark_red())
                    et_embed.set_footer(text="banneTM bot was coded by lmgn", icon_url="https://i.imgur.com/3G99xcd.png")
                    et_embed.set_author(name="banneTM bot", url="https://thelmgn.com",icon_url="https://steamdb.info/static/img/banhammer.png")
                    await client.send_message(message.channel, embed=et_embed)
                else:
                    try:
                        if message.channel.permissions_for(message.author).ban_members:
                           await client.ban(member)
                           et_embed = discord.Embed(title="Banne:tm:", type="rich", description=member.name + " has been banne:tm:", color=discord.Color.red())
                           et_embed.set_footer(text="banneTM bot was coded by lmgn", icon_url="https://i.imgur.com/3G99xcd.png")
                           et_embed.set_author(name="banneTM bot", url="https://thelmgn.com",icon_url="https://steamdb.info/static/img/banhammer.png")
                           await client.send_message(message.channel, embed=et_embed)
                        else:
                            et_embed = discord.Embed(title="Permissions Error", type="rich", description="You do not have the ban_members permission.", color=discord.Color.dark_red())
                            et_embed.set_footer(text="banneTM bot was coded by lmgn", icon_url="https://i.imgur.com/3G99xcd.png")
                            et_embed.set_author(name="banneTM bot", url="https://thelmgn.com",icon_url="https://steamdb.info/static/img/banhammer.png")
                            await client.send_message(message.channel, embed=et_embed)
                    except:
                        et_embed = discord.Embed(title="Banne:tm: Failed", type="rich", description=member.name + " couldn't be banne:tm:'", color=discord.Color.red())
                        et_embed.set_footer(text="made by lmgn", icon_url="https://i.imgur.com/3G99xcd.png")
                        et_embed.set_author(name="banneTM bot", url="https://thelmgn.com",icon_url="https://steamdb.info/static/img/banhammer.png")
                        await client.send_message(message.channel, embed=et_embed)
client.loop.create_task(my_background_task())
client.run('MjYwMDY2OTk1OTEzODgzNjQ4.Czg9yA.EPIo4ukgv0iqisQ7k3lNj3exSqc')