#!/bin/bash

#while true; do
#	name=tun0

#	IFACE=$(/usr/bin/ifconfig | grep $name | awk '{print $1}' | tr -d ":")

#	if [[ $IFACE == $name ]]; then
#		ip=$(ifconfig tun0 | grep -w inet | tail -1 | cut -d "t" -f2 | tr -d " ","ne")
#	else
#		ip=$(ifconfig | grep -w inet | tail -1 | cut -d "t" -f2 | tr -d " ","ne")
#	fi

#	echo $ip >~/.config/qtile/Complementos/ip.txt
#	sleep 60
#done

while true; do
	ip=$(ifconfig | grep -w inet | tail -1 | cut -d "t" -f2 | tr -d " ","ne")
	echo $ip >~/.config/qtile/Complementos/ip.txt
	sleep 60
done
