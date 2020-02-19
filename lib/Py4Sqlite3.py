#functions by soiqualang

import sqlite3

def insert_table(table,field,value,conn):
    with conn:
        cur = conn.cursor()
        strfield=""
        strvalue=""
        for i in range(0,len(field)):
            strfield+=field[i]+", "
            strvalue+="'"+value[i]+"', "
        strfield+=field[i]
        strvalue+="'"+value[i]+"'"
        sql_add_news="INSERT INTO "+table+"("+strfield+") VALUES ("+strvalue+")"
        #print(sql_add_news)
        cur.execute(sql_add_news)
        cur.close()

def insert_table_by_dict (table,fieldsValues,conn):
    with conn:
        cur = conn.cursor()
        fieldState =str()
        valueState =str()
        for field, value in fieldsValues.items():
            fieldState = fieldState + "\"%s\", "%(field)
            valueState = valueState + "'%s', "%(value)
        state = "INSERT INTO " + table + ' (' + fieldState[0:-2] + ') VALUES (' + valueState[0:-2] + ')'

        print (state)
        cur.execute(state)
        cur.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
        
def getElement(tbl_table,element,where,id,conn):
    with conn:
        cur = conn.cursor()
        id=str(id)
        #sql='SELECT SQLITE_VERSION()'
        sql="Select "+element+" from "+tbl_table+" where "+where+"='"+id+"'"
        #print(sql)
        cur.execute(sql)
        data = cur.fetchone()
        #data=cur.fetchall()
        return data[element]
        cur.close()

def table_to_array1(table,conn):
    with conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        sql="SELECT * from "+table
        #print(sql)
        cur.execute(sql)
        rows = cur.fetchall()        
        '''
        for row in rows:
            print ("%s %s %s" % (row["id"], row["ques"], row["ans"]))
        '''
        return rows
        cur.close()

def truncate_tbl(table,conn):
    with conn:
        cur = conn.cursor()
        sql="DELETE FROM "+table
        #print(sql)
        cur.execute(sql)
        cur.close()