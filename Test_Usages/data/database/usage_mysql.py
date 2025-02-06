import os, sys
# point to path
lib_path = os.path.abspath('../../../Libraries/data/database')
sys.path.append(lib_path)

from mysql_lib import mysql_lib

import csv
from datetime import datetime


def show_table(tablename, connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM " + tablename

    try:
        cursor.execute(sql)  # Execute the SQL command
        results = cursor.fetchall()  # Fetch all the rows in a list of lists.

        for column in results:
            ip_hostname = column[0]
            port = column[1]
            key_words_found = column[2]
            possible_services_identified = column[3]
            exceptions_if_any = column[4]
            hash_of_page = column[5]
            print(
                "|ip_hostname=%s|port=%s|key_words_found=%s|possible_services_identified=%s|exceptions_if_any=%s|hash_of_page=%s|" % \
                (ip_hostname, port, key_words_found, possible_services_identified, exceptions_if_any, hash_of_page))
    except:
        print("Error: unable to fetch data")

    return

if __name__ == "__main__":
    id_mysql_lib = "Test Usage Agent <mysql_lib>"
    print ("=====[" + id_mysql_lib + " Start]===== \n")
    mysql_lib_object = mysql_lib(id_mysql_lib)

    trial_key = mysql_lib_object.get_trial_key()
    # print('trial_key for DB: ', trial_key)

    user_id, passcode = 'root', trial_key
    [connection, cursor] = mysql_lib_object.connect_mysql(user_id, passcode)
    # Prepare SQL query to INSERT a record into the DB.
    sql_statement = """SHOW DATABASES;"""

    mysql_lib_object.execute_sql_operations(sql_statement, connection)
    db_names = mysql_lib_object.get_all_db_names(connection)
    print("db_names: ", db_names)

    db_target_name = 'performance_schema'
    if (mysql_lib_object.if_db_exists(connection, db_target_name)):
        print(db_target_name, " exists.")
    else:
        print(db_target_name, " does not exist.")

    # create table
    print("create table")

    db_name = 'ayahuasca'
    table_name = 'Domain_event'

    journal_event_log = "I am 1 day stronger than the previous"  #

    # CREATE DATABASE 'ayahuasca'
    sql_statement = "USE " + db_name
    cursor.execute(sql_statement)

    flag_overwrite_table = False
    # CREATE TABLE
    # Drop table if it already exist using execute().
    if (flag_overwrite_table == True):
        sql_statement = "DROP TABLE IF EXISTS " + table_name
        cursor.execute(sql_statement)

    sql_statement = """CREATE TABLE """ + table_name + """ (
    	    EVENT VARCHAR(100) NOT NULL,
    	    DETAILS VARCHAR(40) NOT NULL,
    	    EVENT_TIME_STAMP TEXT NOT NULL,
    	    SCORE VARCHAR(1000) NOT NULL,
    	    LOG VARCHAR(500) NOT NULL )"""

    mysql_lib_object.execute_sql_operations(sql_statement, connection)

    # insert some data
    sql_statement = """INSERT INTO """ + table_name + """(EVENT,
                	    DETAILS, EVENT_TIME_STAMP, SCORE, LOG)
                	    VALUES (%s, %s, %s, %s, %s)"""

    args = ('Pneuma domain event', 'Holodeck 00', str(datetime.utcnow()), str(75), journal_event_log)
    mysql_lib_object.execute_sql_operations_with_args(sql_statement, args, connection)

    # CREATE TABLE
    table_name = 'SCAN_RESULTS'
    # Drop table if it already exist using execute().
    sql_statement = "DROP TABLE IF EXISTS " + table_name
    cursor.execute(sql_statement)

    sql_statement = """CREATE TABLE """ + table_name +  """ (
	    IP_HOSTNAME VARCHAR(100) NOT NULL,
	    PORT VARCHAR(40) NOT NULL,
	    KEY_WORDS_FOUND TEXT NOT NULL,
	    POSSIBLE_SERVICES_IDENTIFIED VARCHAR(200) NOT NULL,
	    EXCEPTIONS_IF_ANY VARCHAR(500) NOT NULL,
	    HASH_OF_CONTENT_PAGE_FILE VARCHAR(500) NOT NULL )"""

    mysql_lib_object.execute_sql_operations(sql_statement, connection)

    # insert some data
    sql_statement = """INSERT INTO """ + table_name + """(IP_HOSTNAME,
                	             PORT, KEY_WORDS_FOUND, POSSIBLE_SERVICES_IDENTIFIED, EXCEPTIONS_IF_ANY, HASH_OF_CONTENT_PAGE_FILE)
                	             VALUES (%s, %s, %s, %s, %s, %s)"""

    args = ('target_machine_01', 'port_00', 'key word: Vigil', 'service: cipher', 'EXCEPTIONS: Skip', 'hash: sha 256')
    mysql_lib_object.execute_sql_operations_with_args(sql_statement, args, connection)

    args = ('target_machine_02', 'port_00', 'key word: CVG', 'service: SWAT', 'EXCEPTIONS: 42', 'hash: sha 256')
    mysql_lib_object.execute_sql_operations_with_args(sql_statement, args, connection)

    # show_table(table_name, connection)
    mysql_lib_object.show_table(connection, table_name)

    row_index, column_index = 2, 5
    row_data = mysql_lib_object.get_row_of_table(row_index, table_name, connection)
    print("row_data: ", row_data)
    field_data = mysql_lib_object.get_column_of_given_row_of_table(row_index, column_index, table_name, connection)
    print("field_data: ", field_data)

    table_names = mysql_lib_object.get_all_table_names(connection)
    print("table_names: ", table_names)

    table_name = 'table 42'
    table_target_name = table_name.lower()

    if (mysql_lib_object.if_table_exists(connection, table_target_name)):
        print(table_target_name, " exists.")
    else:
        print(table_target_name, " does not exist.")

    current_db_in_use = mysql_lib_object.get_current_db_in_use(connection)
    print("current_db_in_use: ", current_db_in_use)

    table_name = 'Domain_event'
    data_table = mysql_lib_object.show_table(connection, table_name)
    print("data_table: ", data_table)

    row_size, column_size = mysql_lib_object.get_row_size_and_column_size_of_table (table_name, connection)
    print("row_size, column_size = ", row_size, ", ", column_size)

    database_name, table_name = 'ayahuasca', 'scan_results'
    column_field_names = mysql_lib_object.get_column_field_names(database_name, table_name, connection)
    print("column_field_names: ", column_field_names)

    # write to CSV
    data_table_for_csv_format = []
    for row_data in data_table: # format each row item for CSV format
        data_table_for_csv_format.append(str(row_data).lstrip('(').rstrip(')'))

    file_to_write_to = './data/out.csv'
    """
    query = "SELECT * FROM domain_event"

    cursor.execute(query)

    data = cursor.fetchall()
    list = []

    for row in data:
        value = str(row)
        list.append(value)
        file = open(file_to_write_to, 'w')
        data = csv.writer(file)
        data.writerow(list)

    file.close()
    """
    database_name, table_name = 'ayahuasca', 'Domain_event'
    column_field_names = mysql_lib_object.get_column_field_names(database_name, table_name, connection)
    #column_field_names = str(column_field_names).lstrip('[').rstrip(']')
    #print("column_field_names: ", column_field_names)
    f = csv.writer(open(file_to_write_to, "w", newline="\n", encoding="utf-8"), delimiter=' ',
                   escapechar=' ', quoting = csv.QUOTE_NONE)
    f.writerow([str(column_field_names).lstrip('[').rstrip(']')])   # write the field names

    for row_data in data_table_for_csv_format:
        f.writerow([str(row_data)])

    #f.close()

    data = [("first",), ("second",), ("Third",)]
    list = []

    file = open('./data/file.csv', 'w', newline="\n", encoding="utf-8")
    writer = csv.writer(file, delimiter=' ',
                   escapechar=' ', quoting = csv.QUOTE_NONE)
    for row in data:
        writer.writerow(row)
    #writer.close()

    mysql_lib_object.close_deactivate_DB(connection)



# INCOMPLETE: TO BE CONTINUED
"""
db_ursa_name, collection_name = 'ursa_db', 'events'

db = client[db_ursa_name] # create DB
collection = db[collection_name] # create collection
print("databases: ", client.database_names())

mysql_lib_object.if_db_exists(client, db_ursa_name)

from datetime import datetime

doc = {
    "event": "Pneuma domain event",
    "details": "Holodeck 00",
    "event_timestamp": datetime.utcnow(),
    "score": 75,
    "log": "I am 1 day stronger than the previous"   # journal event
}

doc_id = collection.insert_one(doc).inserted_id
print(doc_id)

# query by ObjectId
doc_obtained = collection.find_one({'_id': doc_id})
print(doc_obtained)


many_docs = collection.find().sort('DESCENDING') # empty query means "retrieve all"
for doc in many_docs:
    print(doc)

query = {
        'event': 'Pneuma domain event',
        "score": {
            "$gt": 50
        }
    }

# results = collection.remove(query)
results = collection.find(query)

print('===========================================')
counter = 0
for doc in results:
    counter = counter + 1
    print(counter, ": ", doc)


if (collection.count() == 0):  # Check if collection named [collection_name] is empty
    print("collection : " + collection_name + " is empty.")
else:
    print(db.collection_names())  # Return a list of collections in [ursa_db]
    print(collection_name in db.collection_names())  # Check if collection collection_name exists in db [ursa_db]
    print(collection.name, " has ", collection.count(), " records")

# collection.drop()  # Delete(drop) collection named [collection_name] from db, or db.collection.remove();

mysql_lib_object.if_db_exists(client, db_ursa_name)

"""
print("=====[" + id_mysql_lib + " End]===== \n")

# https://www.tutorialspoint.com/python3/python_database_access.htm
# https://github.com/PyMySQL/PyMySQL/blob/master/pymysql/connections.py
# http://o7planning.org/en/11463/connecting-mysql-database-in-python-using-pymysql