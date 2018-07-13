#!/bin/bash

PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

/home/lucas.rodesguirao/anaconda3/bin/python /home/lucas.rodesguirao/repos/natgeo-wallpaper/wallpaper.py
date="$(date +%F)"
cp /home/lucas.rodesguirao/repos/natgeo-wallpaper/pics/wallpaper_${date}.jpg /home/lucas.rodesguirao/repos/natgeo-wallpaper/pics/wallpaper.jpg


#gsettings set org.gnome.desktop.background picture-uri "file:///home/pol.naranjo/Pictures/wallpaper.jpg"
