import sqlite3, asyncio

PATH_TO_DB = 'data/sql/bot.db'


def is_player_register(id_user):
    """
        Simple check if the player is already register or not
    """
    query = (f"SELECT * FROM player WHERE id_discord=\"{id_user}\";")
    if(len(fetchall_query(query)) == 0):
        return True
    return False

def get_team_name(id):
    """
        Get team of a player
    """
    query = f'SELECT team_name FROM team WHERE capitain=\"{id}\" OR player_one=\"{id}\" OR player_two=\"{id}\"'
    return fetchall_query(query)

async def new_player(ctx, token, nickname, rank, bio):
    """
        Insert new player in the db
    """
    query = f'INSERT INTO player VALUES (null, "{ctx.author.id}","{ctx.author}","{token}","{nickname}","{rank}","{bio}");'
    commit_query(query)

async def update_player(ctx, new_token, nickname, rank, bio):
    """
        Update of player data
    """
    query = f"UPDATE player\
                SET id_discord=\"{ctx.author.id}\",last_discord=\"{ctx.author}\", token=\"{new_token}\", pseudo=\"{nickname}\", player_rank=\"{rank}\", bio=\"{bio}\"\
                WHERE id_discord={ctx.author.id};"
    return commit_query(query)

async def insert_team(ctx, player1, player2, Name, tag, about):
    """
        Create new team !
    """
    query = f"INSERT INTO team VALUES (null, {ctx.author.id}, {player1}, {player2}, \"{Name}\", \"{tag}\", \"{about}\");"
    return commit_query(query)

def show_player(discord_id):
    """
        Give an list with the info of a player
    """
    query = f'SELECT pseudo,player_rank,bio FROM player WHERE id_discord="{discord_id}"'
    return fetchone_query(query)

def show_token(discord_id):
    """
        Get player token
    """
    query = f'SELECT token FROM player WHERE id_discord="{discord_id}"'
    return fetchone_query(query)


"""
    EXECUTE SQL RESQUEST :
"""
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