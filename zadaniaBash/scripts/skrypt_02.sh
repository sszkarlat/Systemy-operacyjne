# przechwytywanie sygnalow

while ((1==1))
do
	if trap SIGINT; then
		echo "Przechwycono SIGINT"
		sleep 2
	elif trap SIGKILL || trap SIGQUIT || trap SIGTERM; then
		echo "Do widzenia"
	fi
done
