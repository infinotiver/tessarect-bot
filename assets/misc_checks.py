import json


def check_muted_role(ctx):
    with open(f'./configs/guild{ctx.guild.id}.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    muted_role = data.get('mute_role')
    if muted_role is None:
        muted_role = 'muted'  # check for muted role in the guild's config, failsafe: "muted"

    x = ctx.guild.roles
    is_present = False
    for y in x:  # iterate over roles and find muted role
        if y.name == muted_role:
            is_present = True
            break
    return is_present


def is_author(ctx, user):
    if ctx.author.id == user.id:
        return True
    else:
        return False


def is_client(client, user):
    if client.user.id == user.id:
        return True
    else:
        return False