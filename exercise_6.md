# Exercise 6: SQL!

```
      (`-,-,
      ('(_,( )
       _   `_'
    __|_|__|_|_
  _|___________|__
 |o o o o o o o o/   
~'`~'`~'`~'`~'`~'`~
```

Write some SQL related to container shipping.

```python
import sqlite3

db = sqlite3.connect(':memory:') # Using an in-memory database
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS bookings (
  booking_number TEXT NOT NULL,
  group_id TEXT NOT NULL,
  departure_id TEXT NOT NULL,
  freesale_ffe FLOAT NOT NULL,
  price_id TEXT NOT NULL,  
  PRIMARY KEY(booking_number) )''')

cur.execute('''INSERT INTO bookings VALUES ('1', 'CNSHG-NLROT', '201205', 10, 'P1');''')
cur.execute('''INSERT INTO bookings VALUES ('2', 'CNSHG-NLROT', '201205', 5, 'P1');''')
cur.execute('''INSERT INTO bookings VALUES ('3', 'CNSHG-NLROT', '201205', 5, 'P2');''')
cur.execute('''INSERT INTO bookings VALUES ('4', 'CNSHG-NLROT', '201204', 10, 'P3');''')
cur.execute('''INSERT INTO bookings VALUES ('5', 'CNSHG-DEBRV', '201205', 1, 'P4');''')
cur.execute('''INSERT INTO bookings VALUES ('6', 'CNSHG-DEBRV', '201205', 5, 'P5');''')

cur.execute('''CREATE TABLE IF NOT EXISTS prices (
  price_id TEXT NOT NULL,
  group_id TEXT NOT NULL,
  departure_id TEXT NOT NULL,
  published_ts TIMESTAMP NOT NULL,
  PRIMARY KEY(price_id) )''')

cur.execute('''INSERT INTO prices VALUES ('P1', 'CNSHG-NLROT', '201205', '2012-01-05T12:43:00');''')
cur.execute('''INSERT INTO prices VALUES ('P2', 'CNSHG-NLROT', '201205', '2012-01-04T07:43:00');''')
cur.execute('''INSERT INTO prices VALUES ('P3', 'CNSHG-NLROT', '201204', '2012-01-03T05:43:00');''')
cur.execute('''INSERT INTO prices VALUES ('P4', 'CNSHG-DEBRV', '201205', '2012-01-03T14:43:00');''')
cur.execute('''INSERT INTO prices VALUES ('P5', 'CNSHG-DEBRV', '201205','2012-01-02T08:43:00');''')

# Q1: What is the total volume booked on CNSHG-NLROT for departure week 201205?
# Q2: What is the total volume booked on each price on CNSHG-NLROT for departure week 201205?
# Q3: What is the total volume booked for each group_id and departure_id week on all latest prices published only?

# Use the following to execute your queries:
# cur.execute(''' SQL STATEMENT ''')
# cur.fetchall()
```

Post your answer on [Github Gist](https://gist.github.com/) or [paste bin](https://paste.ubuntu.com/).
