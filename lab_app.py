from flask import Flask, request, render_template 
import time
import datetime

app = Flask(__name__) 
app.debug = True # Make this False if you are no longer debugging 


@app.route("/") 
def hello(): 
    return "Welcome to David's new website!" 


@app.route("/lab_temp") 
def lab_temp(): 
	import sys 
	from sense_hat import SenseHat

	sense = SenseHat()

	temperature = sense.get_temperature()
	pressure = sense.get_pressure()
	humidity = sense.get_humidity()

	if temperature is not None and pressure is not None and humidity is not None: 
		return render_template("lab_temp.html",temp=temperature, pres=pressure, hum=int(humidity)) 
	else: 
		return render_template("no_sensor.html") 

@app.route("/lab_env_db", methods=['GET'])
def lab_env_db():
	temperatures, humidity, pressure, from_date_str, to_date_str = get_records()
	#return render_template("lab_env_db.html", temp=temperatures, hum=humidity, pres=pressure, temp_items=len(temperatures), hum_items=len(humidity), pres_items=len(pressure))
	return render_template(	"lab_env_db.html", 	temp 			= temperatures,
							hum 			= humidity,
							pres			= pressure,
							from_date 		= from_date_str, 
							to_date 		= to_date_str,
							temp_items 		= len(temperatures),
							hum_items 		= len(humidity),
							pres_items		= len(pressure))

def get_records():
	import datetime
	from_date_str	= request.args.get('from', time.strftime("%Y-%m-%d 00:00"))
	to_date_str	= request.args.get('to', time.strftime("%Y-%m-%d %H:%M"))
	range_h_form	= request.args.get('range_h','');  #This will return a string, if field range_h exists in the request

	range_h_int 	= "nan"  #initialise this variable with not a number

	try: 
		range_h_int	= int(range_h_form)
	except:
		print "range_h_form not a number"

	if not validate_date(from_date_str):
		from_date_str = time.strftime("%Y-%m-%d 00:00")
	if not validate_date(to_date_str):
		to_date_str 	= time.strftime("%Y-%m-%d %H:%M")
	
		# If range_h is defined, we don't need the from and to times
	if isinstance(range_h_int,int):	
		time_now		= datetime.datetime.now()
		time_from 		= time_now - datetime.timedelta(hours = range_h_int)
		time_to   		= time_now
		from_date_str   	= time_from.strftime("%Y-%m-%d %H:%M")
		to_date_str	    	= time_to.strftime("%Y-%m-%d %H:%M")

	import sqlite3
	conn=sqlite3.connect("/var/www/lab_app/lab_app.db")
	curs=conn.cursor()
	curs.execute("SELECT * FROM temperatures WHERE rDATEtime BETWEEN ? and ?", (from_date_str, to_date_str))
	temperatures = curs.fetchall()
	curs.execute("SELECT * FROM humidity WHERE rDATEtime BETWEEN ? and ?", (from_date_str, to_date_str))
	humidity = curs.fetchall()
        curs.execute("SELECT * FROM pressure WHERE rDATEtime BETWEEN ? and ?", (from_date_str, to_date_str))
	pressure = curs.fetchall()
	conn.close()
	return [temperatures, humidity, pressure, from_date_str, to_date_str]

def validate_date(d):
    try:
        datetime.datetime.strptime(d, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        return False

if __name__ == "__main__": 
	app.run(host='0.0.0.0', port=8080) 
