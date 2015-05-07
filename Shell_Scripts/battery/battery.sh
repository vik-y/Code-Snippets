
echo "running" > /home/bobo/Desktop/dischargelog.txt
while true
	do
		charge=`cat /sys/class/power_supply/BAT0/status`
		#echo $charge
		if [ "$charge" == "Discharging" ];
			then
			notify-send "Discharging now, Connect to charger"
		fi
		sleep 10
	done
