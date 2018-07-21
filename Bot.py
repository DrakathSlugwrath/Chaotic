import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import os
client=Bot(description="Hi, i'm Chaos! My summoner is Drakath#3722, the following are my commands '", command_prefix="Chaos ", pm_help = False)
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------------------------------------')
    print('Successfully Summoned Chaos!')
    print('Long Live Chaos!')
    return await client.change_presence(game=discord.Game(name='Youtube with Drakath#3722'))
    
       
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return
 
 
   
 
@client.command()
async def Banhelp(*args):
	await client.say("Ban {@user}")




@client.command(pass_context = True)
async def ban(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members:
        await client.ban(member)
        embed=discord.Embed(title="User Banned!", description="The ancient ones have banned **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0xff00f6)
        await client.say(embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     


async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
    	
        await client.say('Ban list is empty.')
        return
    try:
        await client.unban(ctx.message.server, ban_list[-1])
        await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('unban failed.')
        return		      	 		 		  
  
  
@client.command(pass_context = True)
async def kick(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members:
        await client.kick(member)
        embed=discord.Embed(title="User Kicked!", description="The ancient ones have Kicked **{0}** #rules, to see the rules!)".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool!", color=0xff00f6)
        await client.say(embed=embed)
        
 
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)
    await client.delete_messages(mgs)      

      
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="The ancient ones have Muted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0xff00f6)
        await bot.say(embed=embed)
  
        
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="The ancient ones have Unmuted **{0}** #rules, to see the rules!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0xff00f6)
        await bot.say(embed=embed)
     
                                                                                               

client.run(os.getenv('NDY1OTM2MTEyNzg4MDQ1ODQ0.DiUxDQ.E0ieFhovwED1m7UeF3TGAO-V_Qw'))