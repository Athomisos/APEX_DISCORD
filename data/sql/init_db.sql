CREATE TABLE team ( id INTEGER PRIMARY KEY AUTOINCREMENT, capitain TEXT, player_one TEXT, player_two TEXT, team_name INT, tag TEXT);
CREATE TABLE player ( id INTEGER PRIMARY KEY AUTOINCREMENT, id_discord INT,last_discord TEXT, token TEXT, pseudo TEXT, player_rank TEXT, bio TEXT);
CREATE TABLE ban ( id INTEGER PRIMARY KEY AUTOINCREMENT, id_discord TEXT,  TEXT, reason TEXT, admin INT);
CREATE TABLE kick ( id INTEGER PRIMARY KEY AUTOINCREMENT, id_discord TEXT,  TEXT, reason TEXT, admin INT, end_of_ban DATE);
.exit