Minibian OS - Use ApplyPi Baker to copy image to SD card

On Mac iNet to find the ip address of the raspberry pi

SSH to raspberry pi

apt-get install raspi-config

Expand SD file system and enable GPIO

Reboot 

apt-get update

apt-get install python-dev

apt-get install python-virtualenv

Create a working directory called /var/working and create your virtual working env:
virtualenv venv

To activate the virtual environment from the working directory use:
. venv/bin/activate

To deactivate:
deactivate

Install RPi.GPIO in the active virtual env:
From the active virtual env type: 

Install sensor Hat - install various libs manually to run ok  in python 2 VE.

Install flask

Install uwsgi

Install nginx

Install SQLite3 and create database and tables for the sensor data

Develop python scripts to get sensor data from Sensor Hat and populate new SQLite3 db tables

Copy standard CSS files from web

Create template to display sensor data on web pages

Add 3, 6, 12 and 24 hour radio buttons to template

Add datepicker to template

Add google charts to template

