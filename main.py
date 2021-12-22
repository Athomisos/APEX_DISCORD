import os, asyncio, discord, random, string, db
from discord.ext import commands
from dotenv import load_dotenv


# Get .env variable
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Check db
os.system("./script/check_db.sh")


# Setup cmd Prefix

bot = commands.Bot(command_prefix='!')

def get_token():
    return ''.join(random.choice(string.ascii_letters) for x in range(32))

def get_id_from_ping(user):
    user = user.replace("<@!", "")
    return(user.replace(">", ""))

# Set custom status
@bot.event
async def on_ready(): 
    print(f'{bot.user} has connected to Discord!')
    activity = discord.Game(name="be in BETA", type=4)
    await bot.change_presence(activity=activity)

"""
    CMD : !profile
    USAGE : !profile IG_nickname highest_rank "Your bio"
    DESCRIPTION : Register your self on our system
"""
@bot.command(name='profile', help="!profile IG_nickname highest_rank \"Your bio\" Create your profile")
async def profile(ctx, nickname, rank, bio):
    if(db.is_player_register(ctx.author.id)):
        token = get_token()
        await db.new_player(ctx, token, nickname, rank, bio)
        await ctx.send(f"Welcome aboard :smile:, here is a recap of your identity. if there is an error you can use `!update`\n**Nickname :** `{nickname}`\n**Highest rank : **`{rank}`\n**Bio : **`{bio}`")
        await ctx.author.create_dm()
        await ctx.author.dm_channel.send(
            f'Hey {ctx.author.name}, here is your recovery token account keep it private :smile:\n**TOKEN: **`{token}`')
    else:
        await ctx.send("You are already register, please do !update :smile:")


"""
    CMD : !info
    USAGE : !info @someone
    DESCRIPTION : Get player information
"""
@bot.command(name='info', help="!info @someone")
async def info(ctx, user):
    user = get_id_from_ping(user)
    if(not db.is_player_register(user)):
        data = db.show_player(user)
        team = db.get_team(user)
        await ctx.send("**Nickname :** `" + data[0] + "` \n**Highest rank : **`"+ data[1] + "`\n**Bio : **`" + data[2] + "`\n**Team :** `"+ team[4] + "`")
    else:
        await ctx.send("This player is not register")


"""
    CMD : !update
    USAGE : !update token IG_nickname highest_rank "Your bio"
    DESCRIPTION : Update your player profile
"""
@bot.command(name='update', help="!update token IG_nickname highest_rank \"Your bio\" Update your profile")
async def update_profile(ctx, token, nickname, rank, bio ): #
    if(not db.is_player_register(ctx.author.id)):
        new_token = get_token()
        db_token = db.show_token(ctx.author.id)
        if(db_token[0] == token):
            await db.update_player(ctx, new_token, nickname, rank, bio)
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(
            f'Hey {ctx.author.name}, here is your recovery token account keep it private :smile:\n**TOKEN: **`{new_token}`')
            await ctx.send(f"Done :smile:\n**Nickname :** `{nickname}`\n**Highest rank : **`{rank}`\n**Bio : **`{bio}`\nYou can check with !info @{ctx.author} !")
        else:
            await ctx.send("**ERROR**: Bad token")
    else:
        await ctx.send("You are not register")


# MANAGE CMD
"""
    CMD : !team
    USAGE : !team @player1 @player2 "Name" tag "about your team"
    DESCRIPTION : a new team in the DB
"""
@bot.command(name='team', help="  !team @player1 @player2 ")
async def register_team(ctx, player1, player2, Name, tag, about):
    # Check tag
    if(len(tag) > 6):
        await ctx.send("Your tag need btw 1 and 5 !")
        return 0
    player1 = get_id_from_ping(player1)
    player2 = get_id_from_ping(player2)
    # Check roster
    """
    if(player1 == player2 or ctx.author.id == player2 or player1 == ctx.author.id ):
        await ctx.send("Same player !")
        return"""
    print(f"C={ctx.author.id},\nP1={player1}\nP2={player2}\nNAME={Name}\ntag={tag}\nabout={about}")
    if(not db.is_player_register(player1) and not db.is_player_register(ctx.author.id) and not db.is_player_register(player2)):
        await db.insert_team(ctx, player1, player2, Name, tag, about)
        await ctx.send(f"**RECAP OF TEAM {Name}:**\n Roster = {ctx.author.id}, {player1}, {player2}\nTag = {tag}\nabout = {about}")
    
    
#await ctx.send("https://tenor.com/view/bug-fix-fixing-bugs-in-your-code-bugs-code-sinking-gif-17779185")

@bot.command(name='teamof', help="  !teamof @someone")
async def register_team(ctx, user):
    user = get_id_from_ping(user)
    teams = db.get_team_name(user)
    print(teams)
    out = f"Team of "+ db.show_player(user)[0] + " are "
    for team in teams:
        out += "`" + team[0] + "` " 
    await ctx.send(out)


# Run bot
bot.run(TOKEN)