import pyowm
import pyodbc
import time
from xmlrpclib import datetime
from datetime import timedelta


owm = pyowm.OWM('YOIUR_VALID_KEY')  # You MUST provide a valid API key

observation = owm.weather_at_place('la quinta,us')
w = observation.get_weather()
temp=w.get_temperature('fahrenheit')
temp_value= str(str(temp).split(",")[2]).split(":")[1]

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=YOUR_DATABASE_SERVER;DATABASE=Weather;UID=user;PWD=password')
cursor = cnxn.cursor()
dateQuery= datetime.date.today() - timedelta(5)
            
try:
   
    sql= "INSERT INTO [dbo].[laquinta_temp] ([temp],[reported_date]) VALUES('" + temp_value + "','" + str(dateQuery) + "')"
    cursor.execute(sql)
    cursor.commit()
except :
    cnxn.rollback()


print "Done!"