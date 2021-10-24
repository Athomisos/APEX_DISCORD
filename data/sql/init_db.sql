CREATE TABLE team ( id INT PRIMARY KEY, capitain TEXT, player_one TEXT, player_two TEXT, team_name INT, tag TEXT);
CREATE TABLE player ( id INT PRIMARY KEY, id_discord INT,last_discord TEXT, token TEXT, pseudo TEXT, player_rank TEXT, bio INT);
CREATE TABLE ban ( id INT PRIMARY KEY, id_discord TEXT,  TEXT, reason TEXT, admin INT);
CREATE TABLE kick ( id INT PRIMARY KEY, id_discord TEXT,  TEXT, reason TEXT, admin INT, end_of_ban DATE);
.exit