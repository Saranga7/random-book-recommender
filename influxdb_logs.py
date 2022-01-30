from influxdb import InfluxDBClient
from datetime import datetime


client=InfluxDBClient(host='localhost', port=8086, database='mydb')


try:
    client.switch_database('mydb')

except:
    client.create_database('mydb')
    client.switch_database('mydb')


result=client.query('select * from books')
print(result)






