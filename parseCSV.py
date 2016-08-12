import csv
import dateutil
import models

session = models.get_session()



with open('devices.csv', 'r') as csvfile:
    delim = csv.reader(csvfile, delimiter=',')
    devices={}
    for rows in delim:
        user = models.User(device = rows[1])
        session.add(user)
        devices[int(rows[0])] = rows[1]
    print(devices)
    session.commit()



# t=[]
# x=[]
# y=[]
# z=[]
# with open('accel20.csv', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(float(row[1]))
#         y.append(float(row[2]))
#         z.append(float(row[3]))
#         t.append(dateutil.parser.parse(str(row[0])))
