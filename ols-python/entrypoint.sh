#!/bin/bash

chown 999:999 /usr/local/lsws/conf -R
chown 999:1000 /usr/local/lsws/admin/conf -R

/usr/local/lsws/bin/lswsctrl start
$@
while true; 
do
	if [[ "$(./usr/local/lsws/bin/lswsctrl status)" == *"[ERROR]"* ]] 
    then
		break
	fi

	sleep 60
done



