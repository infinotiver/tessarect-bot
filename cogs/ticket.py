  
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import json
import asyncio

class Tickets(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Tickets are ready!")

    @commands.command(aliases = ['createticket', 'ticketnew','ticket'])
    @cooldown(1, 10, BucketType.user)
    async def new(self, ctx, *, reason = None):

        em = discord.Embed(title = "Confirm New Ticket", color =  0x0098d2)
        #em.add_field(name = "Reason:", value = "We don't want people to spam!")
        em.add_field(name = "Next Step:", value = "Type `confirm` in the chat to confirm this ticket!")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_footer(text = "Be nice with the support Team")
        msg = await ctx.send(embed = em)

        def msg_check(m):
            return m.author == ctx.author and m.channel  == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout = 15.0, check= msg_check)
        except:
            em = discord.Embed(title = " New Ticket Failed!", color = 0x0098d2)
            em.add_field(name = "Reason:", value = "You took too long!")
            em.add_field(name = "Cooldown", value = "1 minute more!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        else:
            if msg.content != "confirm":
                em = discord.Embed(title = "New Ticket Failed!", color = 0x0098d2)
                em.add_field(name = "Reason:", value = "You did not want to create one!")
                em.add_field(name = "Cooldown", value = "1 minute more!")
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = em)

            else:
                channelname = "ticket-{}".format(ctx.author.name)
                for _channel in ctx.guild.channels:
                    if _channel.name == channelname:
                        return await ctx.channel.send(f"You already have a ticket! Please contact staff in {_channel.mention}!")

                warning = f"""{ctx.author.mention} it is always good to provide a reason for your inquiry with the Support Staff\nNext time try `[p]new <reason>`
                """
                tickets = await self.get_tickets()
                guild = ctx.guild
                author = ctx.author
                # Logic
                if str(ctx.guild.id) not in tickets or tickets[str(ctx.guild.id)]["ticketrole"] ==[]:
                    em = discord.Embed(title = "<:Red_Cross:988360177017311263> New Failed",color = 0x0098d2)
                    em.add_field(name = "Reason:", value = "Tickets are not setup!")
                    em.add_field(name ="Usage:", value = "Usage for an admin:\n```diff\n+ [p] addticketrole <@role> [reason]\n- [p] new [reason]\n```")
                    await ctx.send(embed = em)
                    return
                # Getting the role made!
                ticketrole = tickets[str(ctx.guild.id)]["ticketrole"]
                helper_role=[]
                #role_id = int(ticketrole)

                # Setting up the Channel
                channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.name}')
                # Creating the embed
                em = discord.Embed(title = f"<:sucess:935052640449077248> New ticket", color = 0x1a1110)
                
                
                em.add_field(name = "Description:", value = "Staff will be with your shortly")
                em.add_field(name = "Member:", value = f"{ctx.author.mention}")
                em.add_field(name = "Reason:", value = f"`{reason}`")
                em.set_footer(text="Recommended setting up all the stuff")
                # Perms
                # Make sure the author can type!
                await channel.set_permissions(ctx.author, read_messages = True, send_messages = True)
                # Make sure everyone else should not be able to see anything, cause it should be private
                await channel.set_permissions(ctx.guild.default_role, read_messages = False, send_messages = False)
                for xx in ticketrole:
                  x=ctx.guild.get_role(int(xx))
                  
                  await channel.set_permissions(x, read_messages = True, send_messages = True)
                staff=[]      
                for x in ticketrole:
                  staff.append(f'<@&{x}>')
                staff=''.join(staff)
                # Sending the embed
                await channel.send(content=staff,embed = em)
                if reason == None:
                    await channel.send(warning)
                await ctx.send(f"Created the ticket for {ctx.author.mention} , Check {channel.mention}")

                # send the mod log
                try:
                    channelId = int(tickets[str(ctx.guild.id)]["ticketchannel"])
                    for channel_ in ctx.guild.channels:
                        if channel_.id == channelId:
                            em = discord.Embed(title = "<:sucess:935052640449077248> Ticket Opened!", color = 0x0098d2)
                            em.add_field(name = "Member:", value = f"{ctx.author.mention}")
                            em.add_field(name ="Reason:", value = f"`{reason}`")
                            em.add_field(name= "Channel / Access Point", value = f'{channel.mention}')
                            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                            await channel_.send(embed = em)
                            break
                except:
                    pass

    @new.error
    async def new_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:Red_Cross:988360177017311263> New Error", color = 0x0098d2)
            em.add_field(name = "Reason:", value = "If your trying to spam the server then get off!")
            em.add_field(name = "Try again in:", value = "`{:.2f}s`".format(error.retry_after))
            em.set_footer(text="Lots of Spam can lead to a ban")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:Red_Cross:988360177017311263> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Guys huh we created uhhhhhhhhh yeahhhhhh")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command(aliases = ['setticketrole', 'ticketrole'])
    @commands.has_permissions(manage_guild = True)
    async def addticketrole(self, ctx, role : discord.Role = None, *,reason = None):
        if role == None:
            await ctx.send("You need to provide a valid role!")
            return

        tickets = await self.get_tickets()
        em = discord.Embed(title= "<:sucess:935052640449077248> Added ticketrole", color = 0x0098d2)
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        guild = ctx.guild
        author = ctx.author
        if str(ctx.guild.id) not in tickets:
            em.add_field(name = "Switch:", value = f"`None` <➡️940608259075764265> {role.mention}")
            tickets[str(guild.id)] = {}
            tickets[str(guild.id)]["ticketrole"]=[]
            tickets[str(guild.id)]["ticketrole"].append(int(role.id))
        else:
            role_id = tickets[str(guild.id)]["ticketrole"]
            tickets[str(guild.id)]["ticketrole"].append(int(role.id))
            em.add_field(name = "Role:", value = f"{role.mention}")
        em.add_field(name = "Features:", value = "Users can now type `[p] new <reason>`")
        em.add_field(name = "Reason:", value = f"`{reason}`")
        em.set_footer(text="Recommended setting up all the stuff")
        await ctx.send(embed = em)
        
        # send the mod log
        try:
            channelId = int(tickets[str(ctx.guild.id)]["ticketchannel"])
            for channel_ in ctx.guild.channels:
                if channel_.id == channelId:
                    em = discord.Embed(title = "<:sucess:935052640449077248> Ticket Role Set!", color = 0x0098d2)
                    em.add_field(name = "Staff Member:", value = f"{ctx.author.mention}")
                    em.add_field(name ="Reason:", value = f"`{reason}`")
                    em.add_field(name= "Ticket Role", value = f'{role.mention}')
                    em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                    em.set_thumbnail(url = ctx.author.avatar_url)
                    await channel_.send(embed = em)
                    break
        except:
            pass

        # Updating the database
        with open("data.json", "w") as f:
            json.dump(tickets, f)

    @commands.command(aliases = ['remticketrole', 'ticketroleremove'])
    @commands.has_permissions(manage_guild = True)
    async def removeticketrole(self, ctx, role : discord.Role = None, *,reason = None):
        if role == None:
            await ctx.send("You need to provide a valid role!")
            return

        tickets = await self.get_tickets()
        guild = ctx.guild
        author = ctx.author
        if str(ctx.guild.id) not in tickets:
            return await ctx.send(embed=discord.Embed(title="Failed",description="No record for this guild , setup tickets"))
          
        else:
            if role.id in tickets[str(guild.id)]["ticketrole"]:

              try:
                em = discord.Embed(title= "<:sucess:935052640449077248> Removed ticketrole", color = 0x0098d2)
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)              
                tickets[str(guild.id)]["ticketrole"].remove(role.id)
                # Updating the database
                with open("data.json", "w") as f:
                    json.dump(tickets, f)        
                        
                em.add_field(name = "Role:", value = f"{role.mention}")
                em.add_field(name = "Now:", value = f"People having {role} as their topmost role can't see tickets any more")
                em.add_field(name = "Reason:", value = f"`{reason}`")
                em.set_footer(text="Recommended setting up all the stuff")
                await ctx.send(embed = em)
                
              except Exception as e:
                await ctx.send(e)

    @addticketrole.error
    async def addticketrole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:Red_Cross:988360177017311263> Ticket Error", color = 0x0098d2)
            em.add_field(name = "Reason:", value = "You don't have the perms dont try to control me duh!")
            em.add_field(name = "Perms:", value = "`Manage Server permission missing!`")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            em.set_footer(text="Recommended setting up all the stuff")
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title=  "<:Red_Cross:988360177017311263> Ticket Error", color = 0x0098d2)
            em.add_field(name ="Reason:", value = f"{ctx.author.mention}, you need to provide a valid role!")
            em.add_field(name = "Usage:", value = '```diff\n+ [p] addticketrole <@role> [reason]\n- [p] addticketrole bruh\n```')
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            em.set_footer(text = "Read the docs, heheboi!")
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:Red_Cross:988360177017311263> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command(aliases = ['addticketlogs', 'atl', 'stl'])
    @commands.has_permissions(manage_guild = True)
    async def setticketlogs(self, ctx, channel : discord.TextChannel = None, *, reason = None):
        if channel is None:
            await ctx.send("You need to provide a valid channel!")            
        
        em = discord.Embed(title ="<:sucess:935052640449077248> Ticket Logs Set", color = 0x0098d2)
        em.add_field(name = "Staff Member:", value = f"{ctx.author.mention}")
        em.add_field(name = "Channel:", value = f"{channel.mention}")
        em.add_field(name = "Reason:", value = f"`{reason}`", inline = False)
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_footer(text = "Invite me with [p] invite ;)")
        await ctx.send(embed = em)

        tickets = await self.get_tickets()
        guild = ctx.guild

        if str(ctx.guild.id) not in tickets:
            tickets[str(guild.id)] = {}
            tickets[str(guild.id)]["ticketchannel"] = int(channel.id)
        else:
            tickets[str(guild.id)]["ticketchannel"] = int(channel.id)

        with open("data.json", "w") as f:
            json.dump(tickets, f)

    @setticketlogs.error
    async def setticketlogs_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = '<:Red_Cross:988360177017311263> Setticketlogs Failed', color = 0x0098d2)
            em.add_field(name = "Reason:", value = "`Manage Server permission is missing!`")
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_footer(text="Smh, imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = '<:Red_Cross:988360177017311263> Setticketlogs Failed', color = 0x0098d2)
            em.add_field(name = "Reason:", value = "Mention a channel properly, like {}".format(ctx.channel.mention))
            em.add_field(name= "Usage:", value = "```diff\n+ [p] setticketlogs #ticket-logs better ticket logs\n- [p] setticketlogs SniperXi199#2209 setting a member as logs\n```")
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_footer(text="Smh, imagine being that bad!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:Red_Cross:988360177017311263> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command(aliases = ['closeticket', "ticketclose"])
    @commands.has_permissions(manage_channels = True)
    async def close(self, ctx, *, reason = None):
        channel = ctx.channel
        name = channel.name
        tickets = await self.get_tickets()

        if name.startswith("ticket-"):
            # send mod log
          
            channelId = int(tickets[str(ctx.guild.id)]["ticketchannel"])
            print(channelId)
            for ticketChannel in ctx.guild.channels:
                # find channel
                if ticketChannel.id == channelId:
                    em = discord.Embed(title = "<:Red_Cross:988360177017311263> Ticket Closed!", color = 0x0098d2)
                    em.add_field(name = "Staff Member:", value = f"{ctx.author.mention}")
                    em.add_field(name ="Reason:", value = f"`{reason}`")
                    # get the name of member
                    ticket, name = name.split("-")
                    em.add_field(name = "Inquirer:", value = f"{name}")
                    em.set_thumbnail(url = ctx.author.avatar_url)
                    await ticketChannel.send(embed = em)
                    break
            
            messageEmbed = discord.Embed(title = "<:sucess:935052640449077248> Ticket Will Close!", color = 0x0098d2,
            description = "This ticket will close in ten seconds. Thanks for your time!")
            seconds = 10
            messageEmbed.add_field(name= "Time remaining:", value = f"`{seconds}`")
            messageEmbed.add_field(name = "Staff Member:", value = f"{ctx.author.mention}")
            messageEmbed.add_field(name = "Reason:", value = f"`{reason}`")
            messageEmbed.add_field(name = "Mod Logs:", value = "Sending logs in 5 seconds!")
            messageEmbed.set_footer(text = "Wanna invite me eh? `[p] invite`)")
            await ctx.send(embed = messageEmbed)
            # sleep and delete channel
            await asyncio.sleep(10)
            # now delete the channel
            await channel.delete()
        else:
            em = discord.Embed(title = "<:Red_Cross:988360177017311263> Closing Failed!", color= 0x0098d2)
            em.add_field(name = "Reason:", value = f'This channel ({ctx.channel.mention}) is not a ticket channel!')
            em.add_field(name = "Try again later!", value = "Only a channel which has been a ticket can be closed!")
            em.set_footer(text="Recommended setting up all the stuff")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @close.error
    async def close_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = '<:Red_Cross:988360177017311263> Close Failed', color = 0x0098d2)
            em.add_field(name = "Reason:", value = "`Manage Channels permission is missing!`")
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_footer(text="Smh, imagine thinking you have the perms!")
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:Red_Cross:988360177017311263> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    async def get_tickets(self):
        with open("data.json", "r") as f:
            data = json.load(f)        
        return data
    
    """
    @param guild : discord.Guild object!
    """
    async def get_logs(self, guild):
        guild_id = guild.id
        tickets = await self.get_tickets()

        if str(guild_id) not in tickets:
            return False
        return int(tickets[str(guild.id)]["ticketchannel"])
    
    """
    @param guild : discord.Guild object!
    """
    async def get_role(self, guild):
        guild_id = guild.id
        tickets = await self.get_tickets()

        if str(guild_id) not in tickets:
            return False
        return int(tickets[str(guild_id)]["ticketrole"])
    
    """
    @param guild : discord.Guild object!
    @param ticketrole : discord.Role object
    @param ticketchannel : discord.Channel object
    """
    async def open_guild(self, guild, ticketrole : discord.Role, ticketchannel: discord.TextChannel):
        tickets = await self.get_tickets()
        if not str(guild.id) in tickets:
            tickets[str(guild.id)] = {}
            tickets[str(guild.id)]["ticketchannel"] = int(ticketchannel.id)
            tickets[str(guild.id)]["ticketrole"] = int(ticketrole.id)
        else:
            tickets[str(guild.id)]["ticketchannel"] = int(ticketchannel.id)
            tickets[str(guild.id)]["ticketrole"] = int(ticketrole.id)
        
        with open("data.json", "w") as f:
            json.dump(tickets, f)
        
        return [self.get_logs(guild), self.get_role(guild)]

def setup(client):
    client.add_cog(Tickets(client))