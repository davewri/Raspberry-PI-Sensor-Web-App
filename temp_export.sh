#!/bin/bash
if [ -f temperatures.csv ]; then
	rm temperatures.csv
	echo -e "temperatures.csv deleted\n"
else
	echo -e "temperatures.csv didnt exist\n"
fi

if [ -f humidity.csv ]; then
	rm humidity.csv
	echo -e "humidity.csv deleted\n"
else
	echo -e "humidity.csv didnt exist\n"
fi

if [ -f pressure.csv ]; then
        rm pressure.csv
        echo -e "pressure.csv deleted\n"
else 
        echo -e "pressure.csv didnt exist\n"
fi

sqlite3 -header -csv lab_app.db "SELECT rDatetime, round((temp),2) FROM temperatures WHERE rDatetime BETWEEN date('now') AND datetime($now);" > temperatures.csv
echo -e "new temperatures.csv created with export of temperatures\n"

sqlite3 -header -csv lab_app.db "SELECT rDatetime, round((hum),2) FROM humidity WHERE rDatetime BETWEEN date('now') AND datetime($now);" > humidity.csv
echo -e "new humidity.csv created with export of humidity\n"

sqlite3 -header -csv lab_app.db "SELECT rDatetime, round((pres),2) FROM pressure WHERE rDatetime BETWEEN date('now') AND datetime($now);" > pressure.csv
echo -e "new pressure.csv created with export of pressure\n"
