#Building a Labeled Data Set for Accelerometry Detection of Messaging

##Data Structure

models.py contains the classes use to create the three tables, User, Accelerometer, and Keyboard.

###User
User has two columns: <code>id</code> and <code>device</code> which describes the device used.
The tables Accelerometer and Keyboard are connected to the User table through foreign keys.

###Accelerometer
Accelerometer has five columns: <code>id</code> (primary key), <code>timestamp</code>, <code>accel_x</code>, <code>accel_y</code>, <code>accel_z</code>

###Keyboard
Keyboard has three columns: <codes>id</code> (primary key), <code>timestamp</code>, <code>key_press</code>
If the keypress is -4 that means the user sent the message, when it is at 0 the user was writing the message.

###Parsing Scripts
parseCSVdevice.py is used to create the User table. It parses through one csv which has all the device each user used in the study.

parseCSVaccel.py is used to create the Accelerometer table. There are 20 csv files names accel%d which contains the accelerometer data from each user. In table there three axes and a timestamp. Each axis is in m/s<sup>2</sup>.

parseCSVkeyboard is use to create the Keyboard table. There are 20 csv files names keyboard%d which contains the keypress from each user.

##Working With the Data
SQLAlchemy models are provide in models.py to work with the data easily in python. To install the required libraries, run the following:

```bash
pip install -r requirements.txt
```
