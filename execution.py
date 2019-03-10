import connection
from connection import database

from time import time
import math
##########################################

if __name__ == __main__ :
    main():




SQL = "Select * from actor"

cursor = database.cursor();
tick = time()
cursor.execute(SQL)



for x in cursor.fetchall():
    print('====================')
    for y in x:
        print('| '+ str(y) )
    print('====================')
else:
    tock = time()

    execution_time = '%.5f'%(tock - tick);
    print(" ")
    print('*********************************')
    print('fetched total of ' + str(cursor.rowcount) + " rows in " + str(execution_time) + ' seconds.')
    print('Would you like to export the result as a file?')
    print('Type Yes/No')
    print('*********************************')

def main():
    SQL = input('Please, write a valid SQL request')
