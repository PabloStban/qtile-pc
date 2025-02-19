#!/bin/sh
#Ejecuta al inicial sesion

#Configuracion teclado
#setxkbmap es &

# resolucion virtual box se puede instalar los complementos arch linux guess para corregir esto
#xrandr --output Virtual-1 --primary --mode 1600x900 --pos 0x0 --rotate normal --output Virtual-2 --off --output Virtual-3 --off --output Virtual-4 --off --output Virtual-5 --off --output Virtual-6 --off --output Virtual-7 --off --output Virtual-8 --off

#xrandr --newmode "1600x900_60.00"  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync
#xrandr --addmode Virtual-1 1600x900_60.00
#xrandr --output Virtual-1 --mode 1600x900_60.00

# iconos del sistema

sed -i "s/corner-radius = 15/corner-radius = 8/" /home/pablo/.config/picom.conf
qtile cmd-obj -o cmd -f hide_show_bar
udiskie -t &
nm-applet &
volumeicon &
feh --bg-fill $HOME/Pictures/xenotrip.jpg
picom &
/home/pablo/.config/qtile/initial-clipboard.sh
