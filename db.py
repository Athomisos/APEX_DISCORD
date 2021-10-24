import sqlite3

PATH_TO_DB = 'data/sql/bot.db'


def get_conn():
    return(sqlite3.connect(PATH_TO_DB))



def not_register():
    """
        Need to be write
    """
    return True

def new_player(ctx, token, nickname, rank, bio):
    if(not_register()):
        conn = get_conn()
        print(f'\n-------\nREQEST : INSERT INTO player(id_discord,last_discord,token,psuedo,player_rank,bio) VALUES ("{ctx.author.id}","{ctx.author}","{token}","{nickname}","{rank}","{bio}");\n-------\n')
        conn.execute(f'INSERT INTO player(id_discord,last_discord,token,pseudo,player_rank,bio) VALUES ("{ctx.author.id}","{ctx.author}","{token}","{nickname}","{rank}","{bio}");')
    else:
        return False