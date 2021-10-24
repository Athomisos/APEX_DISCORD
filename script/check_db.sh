#!/bin/bash

#*******************************************************************************************#
#*----- Auteur :        Aubertin Emmanuel               | For: APEX_DISCORD             ****#
#*----- GitHub :        Athomisos                       | Twitter : @TheRealaTHO_       ****#
#*----- Description :   Ubuntu/Debian instaler of APEX_DISCORD                          ****#
#*******************************************************************************************#

PROGNAME=$(basename $0)
RELEASE="Revision 1.0"
AUTHOR="(c) 2021 Aubertin Emmanuel / Twitter : @TheRealaTHO_"
DEBUG=0


print_release() {
    echo "$RELEASE $AUTHOR"
}

if [ "$(dirname ${0})" == "." ]; then
    sql="../data/sql/init_db.sql"
    db="../data/sql/bot.db"
else
    sql="$(dirname ${0})/../data/sql/init_db.sql"
    db="$(dirname ${0})/../data/sql/bot.db"
fi

if [ ! -f $db ]; then
    echo "La database n'existe pas. Creation..."
    touch $db
    sqlite3 $db < $sql
else
    echo "We find a existing db"
fi

