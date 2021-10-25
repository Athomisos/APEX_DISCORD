import sqlite3

PATH_TO_DB = 'data/sql/bot.db'


def get_conn():
    return(sqlite3.connect(PATH_TO_DB))



def is_player_register(id_user):
    """
        Simple check if the player is already register or not
    """
    conn = get_conn()
    cur = conn.cursor()
    print(f"\n-------\nREQEST : SELECT * FROM player WHERE id_discord=\"{id_user}\";")
    cur.execute(f"SELECT * FROM player WHERE id_discord=\"{id_user}\";")
    rows = cur.fetchall()
    print(f"RESUTL = {rows}\n-------\n")
    if(len(rows) == 0):
        return True
    return False

def new_player(ctx, token, nickname, rank, bio):
    """
        Insert new player in the db
    """
    conn = get_conn()
    cur = conn.cursor()
    req = f'INSERT INTO player VALUES (null, "{ctx.author.id}","{ctx.author}","{token}","{nickname}","{rank}","{bio}");'
    print(f'\n-------\nREQEST :  {req}\n-------\n')
    cur.execute(req)
    conn.commit()
    print("-- DONE --")
    conn.close()