import csv
import dateutil.parser
import models

session = models.get_session()

for userID in range(1,21):
    user = session.query(models.User).filter(models.User.id==userID).first()
    if user is None:
        continue
    with open('accel%d.csv' % userID, 'r') as csvfile:#reads each file in consecutive order
        delim = csv.reader(csvfile, delimiter=',')
        accel={}

        for row in delim:
            x=(float(row[1]))
            y=(float(row[2]))
            z=(float(row[3]))
            t=(dateutil.parser.parse(str(row[0])))#parses date and timestamps 

            ax = models.Accelerometer(timestamp = t, accel_x = x, accel_y = y, accel_z = z, user = user)
            session.add(ax)

            keys=["X", "Y", "Z", "DateTime"]
            accel[keys[0]] = x
            accel[keys[1]] = y
            accel[keys[2]] = z
            accel[keys[3]] = t
        session.commit()
