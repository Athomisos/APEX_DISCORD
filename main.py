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

# Set custom status
@bot.event
async def on_ready(): 
    print(f'{bot.user} has connected to Discord!')
    activity = discord.Game(name="be in BETA", type=4)
    await bot.change_presence(activity=activity)

# MANAGE CMD
@bot.command(name='team', help="  !team @captain @player1 @player2 ")
async def register_team(ctx):
    await ctx.send("https://tenor.com/view/bug-fix-fixing-bugs-in-your-code-bugs-code-sinking-gif-17779185")


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


@bot.command(name='info', help="!info @someone")
async def info(ctx, user):
    user = user.replace("<@!", "")
    user = user.replace(">", "")
    if(not db.is_player_register(user)):
        data = db.show_player(user)
        await ctx.send("**Nickname :** `" + data[0] + "` \n**Highest rank : **`"+ data[1] + "`\n**Bio : **`" + data[2] + "`")
    else:
        await ctx.send("This player is not register")

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
            await ctx.send("**ERROR** Bad token")
    else:
        await ctx.send("You are not register")
# Run bot
bot.run(TOKEN)