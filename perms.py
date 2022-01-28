from discord.ext import commands

bot_owners = [900992402356043806]
owner_role = 912569937153892361
captain_role = 912569937116147777
staff_role = 921341867394740275

#Bot Owner
def is_owner_check(ctx):
    return ctx.message.author.id in bot_owners

def owner_id_check(_id):
    return _id in bot_owners

def owner():
    return commands.check(is_owner_check)
