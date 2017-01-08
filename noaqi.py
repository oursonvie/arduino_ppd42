import serial
from influxdb import InfluxDBClient

client = InfluxDBClient('10.1.1.101', 8086, 'root', 'root', 'air')

UNO = '/dev/cu.usbmodem1421'
arduino = serial.Serial(UNO, 9600)

## arduino = serial.Serial('COM1', 115200, timeout=.1)

## the format are given by arduino in: PM10 count,PM2.5 count,PM10 conc,PM2.5 conc

while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
          json_body = [
            {
                "measurement": "air",
                "device": "PPD42",
                "location": "Home",
                "fields": {
                    "pm10_count": data.split(',')[0],
                    "pm2.5_count": data.split(',')[1],
                    "pm10": data.split(',')[2],
                    "pm2.5": data.split(',')[3],
                }
            }
        ]
        client.write_points(json_body)
