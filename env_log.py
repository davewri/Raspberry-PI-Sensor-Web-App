import sqlite3
import sys
from sense_hat import SenseHat

def log_values(sensor_id, temp, pres, hum):
	conn=sqlite3.connect('/var/www/lab_app/lab_app.db')

	curs=conn.cursor()
	curs.execute("""INSERT INTO temperatures values(datetime('now'), (?), (?))""", (sensor_id,temp))
	curs.execute("""INSERT INTO pressure values(datetime('now'), (?), (?))""", (sensor_id,pres))
	curs.execute("""INSERT INTO humidity values(datetime('now'), (?), (?))""", (sensor_id,hum))
	conn.commit()
	conn.close()

sense = SenseHat()

temperature = sense.get_temperature()
pressure = sense.get_pressure()
humidity = sense.get_humidity()

if temperature is not None and humidity is not None and pressure is not None:
	log_values("1", temperature, pressure, int(humidity))
else:
	log_values("1", -999, -999)

