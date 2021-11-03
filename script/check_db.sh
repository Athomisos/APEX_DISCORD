#!/bin/bash

#*******************************************************************************************#
#*----- Auteur :        Aubertin Emmanuel               | For: APEX_DISCORD             ****#
#*----- GitHub :        Athomisos                       | Twitter : @TheRealaTHO_       ****#
#*----- Description :   Check if an sqllite DB already exist                            ****#
#*******************************************************************************************#

PROGNAME=$(basename $0)
RELEASE="Revision 1.0"
AUTHOR="(c) 2021 Aubertin Emmanuel / Twitter : @TheRealaTHO_"
DEBUG=0

print_release() {
    echo "$RELEASE $AUTHOR"
}

print_usage() {
        echo ""
        echo "$PROGNAME"
        echo ""
        echo "Usage: $PROGNAME | [-h | --help] | [-v | --version]"
        echo ""
        echo "          -h  Aide"
        echo "          -v  Version"
        echo ""
}

print_help() {
        print_release $PROGNAME $RELEASE
        echo ""
        print_usage
        echo ""
        echo ""
                exit 0
}

while [ $# -gt 0 ]; do
    case "$1" in
        -h | --help)
            print_help
            exit 
            ;;
        -v | --version)
                print_release
                exit 
                ;;
        *)  echo "Argument inconnu: $1"
            print_usage
            ;;
        esac
shift
done


if [ "$(dirname ${0})" == "." ]; then
    sql="../data/sql/init_db.sql"
    db="../data/sql/bot.db"
else
    sql="$(dirname ${0})/../data/sql/init_db.sql"
    db="$(dirname ${0})/../data/sql/bot.db"
fi

if [ ! -f $db ]; then
    echo "We don't find an existing db. Creation of a new db..."
    touch $db
    sqlite3 $db < $sql
    echo -e "\e[1;32DONE\e[0m"
else
    echo "We find a existing db"
fi

