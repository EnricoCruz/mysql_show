import connection
from connection import database

from time import time
import math

import tasksManager
##########################################

if  __name__ == "__main__" :
    cursor = database.cursor();
    SQL = input('Please, write a valid SQL request: ')
    ##SQL = 'SELECT * from actor'
    tick = time()
    cursor.execute(SQL)
    query = cursor.fetchall()

    for x in query:
        print('====================')
        for y in x:
            if type(y) == bytearray:
                string = ""
                for b in y:
                    string += str(b)
                print(string)
            else:
                print(str(y))
        print('====================')
    else:
        tock = time()

        execution_time = '%.5f'%(tock - tick);
        print(" ")
        print('*********************************')
        print('fetched total of ' + str(cursor.rowcount) + " rows in " + str(execution_time) + ' seconds.')
        print('Would you like to export the result as a file?')
        order = input('Type Yes/No: ')
        ##order = 'yes'
        tasksManager.handleTask(query, order)

else:
    print('invalid access of file.')
