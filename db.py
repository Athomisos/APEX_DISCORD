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
    conn.close()
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
    conn.close()
    if(len(rows) == 0):
        return True
    return False

async def new_player(ctx, token, nickname, rank, bio):
    """
        Insert new player in the db
    """
    query = f'INSERT INTO player VALUES (null, "{ctx.author.id}","{ctx.author}","{token}","{nickname}","{rank}","{bio}");'
    print(f'\n-------\nREQEST :  {query}\n-------\n')
    commit_query(query)

async def update_player(ctx, new_token, nickname, rank, bio):
    query = f"UPDATE player\
                SET id_discord=\"{ctx.author.id}\",last_discord=\"{ctx.author}\", token=\"{new_token}\", pseudo=\"{nickname}\", player_rank=\"{rank}\", bio=\"{bio}\"\
                WHERE id_discord={ctx.author.id};"
    return commit_query(query)

def show_player(discord_id):
    """
        Give an list with the info of a player
    """
    query = f'SELECT pseudo,player_rank,bio FROM player WHERE id_discord="{discord_id}"'
    return fetchone_query(query)

def show_token(discord_id):
    query = f'SELECT token FROM player WHERE id_discord="{discord_id}"'
    return fetchone_query(query)

def fetchall_query(query):
    conn = sqlite3.connect(PATH_TO_DB)
    return conn.cursor().execute(query).fetchall()

def fetchone_query(query):
    conn = sqlite3.connect(PATH_TO_DB)
    return conn.cursor().execute(query).fetchone()

def commit_query(query):
    conn = sqlite3.connect(PATH_TO_DB)
    conn.execute(query)
    return conn.commit()



"""
UPDATE player
SET id_discord={ctx.author.id},last_discord={ctx.author}, token={new_token}, pseudo={nickname}, player_rank={rank}, bio={bio}
WHERE id_discord={ctx.author.id};
"""