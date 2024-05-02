#!/bin/bash

while true; do
	name=tun0

	IFACE=$(/usr/bin/ifconfig | grep $name | awk '{print $1}' | tr -d ":")

	if [[ $IFACE == $name ]]; then
		ip=$(ifconfig tun0 | grep -w inet | tail -1 | cut -d "t" -f2 | tr -d " ","ne")
	else
		ip="Disconnect"
	fi
	echo $ip >~/.config/qtile/Complementos/vpn.txt
	sleep 60
done
