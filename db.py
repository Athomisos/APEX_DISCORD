import sqlite3, asyncio

PATH_TO_DB = 'data/sql/bot.db'


def is_player_register(id_user):
    """
        Simple check if the player is already register or not
    """
    conn = sqlite3.connect(PATH_TO_DB)
    cur = conn.cursor()
    print(f"\n-------\nREQEST : SELECT * FROM player WHERE id_discord=\"{id_user}\";")
    cur.execute(f"SELECT * FROM player WHERE id_discord=\"{id_user}\";")
    rows = cur.fetchall()
    print(f"RESUTL = {rows}\n-------\n")
    if(len(rows) == 0):
        return True
    return False

def is_player_register_nm(name_user):
    """
        Simple check if the player is already register or not
    """
    conn = sqlite3.connect(PATH_TO_DB)
    cur = conn.cursor()
    print(f"\n-------\nREQEST : SELECT * FROM player WHERE last_discord=\"{name_user}\";")
    cur.execute(f"SELECT * FROM player WHERE last_discord=\"{name_user}\";")
    rows = cur.fetchall()
    print(f"RESUTL = {rows}\n-------\n")
    if(len(rows) == 0):
        return True
    return False

async def new_player(ctx, token, nickname, rank, bio):
    """
        Insert new player in the db
    """
    query = f'INSERT INTO player VALUES (null, "{ctx.author.id}","{ctx.author}","{token}","{nickname}","{rank}","{bio}");'
    print(f'\n-------\nREQEST :  {query}\n-------\n')
    await commit_async(query)
    print("-- DONE --")

async def show_player(discord_name):
    """
        Give an list with the info of a player
    """
    query = f'SELECT pseudo,player_rank,bio FROM player WHERE id_discord="{discord_name}"'
    return await fetchone_async(query)

async def fetchall_async(query):
    conn = sqlite3.connect(PATH_TO_DB)
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None, lambda: conn.cursor().execute(query).fetchall().close())

async def fetchone_async(query):
    conn = sqlite3.connect(PATH_TO_DB)
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None, lambda: conn.cursor().execute(query).fetchone().close())

async def commit_async(query):
    conn = sqlite3.connect(PATH_TO_DB)
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None, lambda: conn.cursor().execute(query).commit().close())