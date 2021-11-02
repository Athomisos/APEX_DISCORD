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

print_usage() {
        echo ""
        echo "$PROGNAME"
        echo ""
        echo "Usage: $PROGNAME | [-h | --help] | [-v | --version] | [-d | --debug]"
        echo ""
        echo "          -h  Aide"
        echo "          -v  Version"
        echo "          -d  Debug"
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
        -d | --debug)
                DEBUG=1
                ;;
        *)  echo "Argument inconnu: $1"
            print_usage
            ;;
        esac
shift
done

if [ $UID -ne 0 ]; then
    echo -e "\e[1;31mError :\e[22m To install APEX_DISCORD you need root privileges\e[0m"
    exit 1
fi

function ask_yes_or_no() {
    echo -n "[yes/no] : "
    read -r YESNO
    if [[ $YESNO =~ [yY] ]]; then
        return 0
    fi
    return 1
}

if [ $# - ]
#Install python3 and lib
echo -e "\e[32m--------| \e[1;32mINSTALATION OF DEPENDENCIES\e[32m |--------\e[0m"
apt install -y python3-pip sqlite3 git

echo -e "\e[32m--------| \e[1;32mPYTHON3 LIB\e[32m |--------\e[0m"
pip3 install discord.py sqlitepy python-dotenv

## GIT CLONE
echo -e "\e[32m--------| \e[1;32mGIT CLONE\e[32m |--------\e[0m"
echo "git clone https://github.com/Athomisos/APEX_DISCORD.git"
