import csv
import dateutil
import models

session = models.get_session()#initiates connection to database 



with open('devices.csv', 'r') as csvfile:
    delim = csv.reader(csvfile, delimiter=',')
    devices={}
    for rows in delim:
        user = models.User(device = rows[1])
        session.add(user)
        devices[int(rows[0])] = rows[1]
    print(devices)
    session.commit() #adds all the data into the table
