import csv
import dateutil.parser
import models

session = models.get_session()

for userID in range(1,21):
    print("Processing keyboard%d.csv" % userID)
    user = session.query(models.User).filter(models.User.id==userID).first()
    if user is None:
        continue
    with open('keyboard%d.csv' % userID, 'r') as csvfile:#reads each file in consecutive order
        plots = csv.reader(csvfile, delimiter=',')


        for row in plots:
            k=(int(row[1]))
            t=(dateutil.parser.parse(str(row[0])))

            kb = models.Keyboard(timestamp = t, key_press = k, user = user)
            session.add(kb)
        session.commit()
