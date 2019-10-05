import pandas as PD
from db import DB

DATABASE = DB(filename='logs.sqlite3', dbtype='sqlite')

#print(DATABASE.tables)

LOG_DF = DATABASE.tables.log.all()
#print(LOG_DF.tail())

LOG_DF['date'] = PD.to_datetime(LOG_DF['date'], format='%Y-%m-%d %H:%M:%S.%f')
#print(LOG_DF.dtypes)

LOG_DF.set_index(['date'], inplace=True)
#print(LOG_DF['2017'])
#print(LOG_DF['2017-01-03 10:47'])
print(LOG_DF['2017-01-03 10:47':'2017-01-03 10:51'])