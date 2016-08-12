models.py contains the classes use to create the three tables, User, Accelerometer, and Keyboard.

parseCSVdevice.py is used to create the User table. It parses through one csv which has all the device each user used in the study.

parseCSVaccel.py is used to create the Accelerometer table. There are 20 csv files names accel%d which contains the accelerometer data from each user. In table there three axes and a timestamp. Each axis is in m/s^2.

parseCSVkeyboard is use to create the Keyboard table. There are 20 csv files names keyboard%d which contains the keypress from each user.
If the keypress is -4 that means the user sent the message, when it is at 0 the user was writing the message.

The tables Accelerometer and Keyboard are connected to the User table through foreign keys. 
