####################################
import sys

from pymysql import connect
from pymysql import MySQLError, ProgrammingError

class mysql_lib:
    """ Template model of Gaia """
    def __init__(self, id):
        self.id = id;
        self.max_server_selection_delay = 20 # Assume 20 ms maximum server selection delay
        print ("_gaia object [%s] is born\n" % self.id)

    def get_trial_key(self):
        path_to_trial_key = '../../../Construction_Facilities/secrets_crypt/trial_keys.txt'
        field_tag = 'key_DB:'
        data_field_holders = ['[', ']']
        DOES_NOT_EXIST = -1
        trial_key = None

        try:
            with open(path_to_trial_key) as fp:
                line = fp.readline()
                while line:
                    #print("Line {}: {}".format(cnt, line.strip()))

                    if (line.find(field_tag) != DOES_NOT_EXIST):     # found
                        line = line.lstrip(field_tag)

                        # remove boundary empty spaces
                        while (line[0] == ' ') | (line[0] == '\t'):
                            line = line.lstrip(' ').lstrip('\t')

                        while (line[-1] == ' ') | (line[-1] == '\t'):
                            line = line.rstrip(' ').rstrip('\t')

                        trial_key = line.lstrip(data_field_holders[0]).rstrip(data_field_holders[1])
                        break

                    line = fp.readline()    # read next line
        finally:
            fp.close()

        return trial_key

    def connect_mysql (self, user_id, passcode):

        trial_key = self.get_trial_key()
        # print('trial_key for DB: ', trial_key)

        # server must be turn on 1st
        try:
            # connect("localhost", "root", trial_key, "TESTDB")  # Open database connection
            connection = connect(host = 'localhost', port=3306, connect_timeout = self.max_server_selection_delay, ssl=None, user = user_id, passwd = passcode) # , db='mysql')
            print("Servers connected ... \n Server Details: ",
                  connection.get_server_info())  # force connection on a request as connect=True parameter of MongoClient seems to be useless here
            cursor = connection.cursor()
            # print(connection.database_names())  # Return a list of db, equal to: > show dbs
            print('===========================================')
        except (MySQLError, ProgrammingError) as err:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
            print(err)
            print("Server not available")
            print("Error %d: %s" % (err.args[0], err.args[1]))

            sys.exit()

        return [connection, cursor]

    def execute_sql_operations(self, sql_statement, connection):
        cursor = connection.cursor()
        respond_answer_list = []

        try:
            cursor.execute(sql_statement)  # Execute the SQL command
            connection.commit()  # Commit changes in the database

            respond_answer_counter = 0
            for respond_answer in cursor:
                respond_answer_counter = respond_answer_counter + 1
                print("respond_answer: ", respond_answer_counter, " : ", respond_answer)
                respond_answer_list.append(respond_answer)

        except (MySQLError, ProgrammingError) as err:
            connection.rollback()  # Rollback in case there is any error
            print(err)

        return respond_answer_list

    def execute_sql_operations_with_args(self, sql_statement, args, connection):
        cursor = connection.cursor()
        respond_answer_list = []

        print("data to be inserted: " + str(args));

        try:
            cursor.execute(sql_statement, args)  # Execute the SQL command
            connection.commit()  # Commit changes in the database
            print("data inserted: " + str(args));

            respond_answer_counter = 0
            for respond_answer in cursor:
                respond_answer_counter = respond_answer_counter + 1
                print("respond_answer: ", respond_answer_counter, " : ", respond_answer)
                respond_answer_list.append(respond_answer)
        except (MySQLError, ProgrammingError) as err:
            print("Data :" + str(args) + " NOT inserted.")
            connection.rollback()  # Rollback in case there is any error
            print(err)

        return

    def get_current_db_in_use (self, connection):
        sql_statement = """SELECT DATABASE() FROM DUAL;"""
        current_db_in_use = self.execute_sql_operations(sql_statement, connection)
        current_db_in_use = str(current_db_in_use).lstrip("'[(").rstrip(",)]'")

        return current_db_in_use

    def get_all_db_names (self, connection):
        sql_statement = """SHOW DATABASES;"""

        db_names = self.execute_sql_operations(sql_statement, connection)
        db_names_list = []

        for i in range(0, len(db_names)):
            db_names_list.append(str(db_names[i]).lstrip("'(").rstrip(",)'"))

        return db_names_list

    def if_db_exists (self, connection, db_target_name):  #
        db_names_list = self.get_all_db_names(connection)
        status_found = False

        if (db_target_name in db_names_list):
            print("Database [", db_target_name, "] exists.")
            status_found = True
        else:
            for db_name in db_names_list:
                print("Database [", db_name, "].")

        return status_found

    def get_all_table_names (self, connection):
        sql_statement = """SHOW TABLES;"""

        table_names = self.execute_sql_operations(sql_statement, connection)
        table_names_list = []

        for i in range(0, len(table_names)):
            table_names_list.append(str(table_names[i]).lstrip("'(").rstrip(",)'"))

        return table_names_list

    def if_table_exists (self, connection, table_target_name):  #
        table_names_list = self.get_all_table_names(connection)
        status_found = False

        if (table_target_name in table_names_list):
            print("Table [", table_target_name, "] exists.")
            status_found = True
        else:
            for table_name in table_names_list:
                print("Table [", table_name, "].")

        return status_found

    def show_table (self, connection, table_name):
        sql_statement = "SELECT * FROM " + table_name
        print('[SHOW TABLE]')
        row_data_list = self.execute_sql_operations(sql_statement, connection)

        return row_data_list

    def get_row_of_table(self, row_number, table_name, connection):
        cursor = connection.cursor()

        sql_statement = "SELECT * FROM " + table_name

        respond_result = ""
        try:
            cursor.execute(sql_statement)
            row_content = cursor.fetchall()

            row_counter = 0;  # Caveat: row_number = 0 is reserved for field description row
            # respond_answer_counter = 0
            for respond_answer in row_content:
                row_counter = row_counter + 1
                # respond_answer_counter = respond_answer_counter + 1
                # print("respond_answer: ", respond_answer_counter, " : ", respond_answer)
                if (row_counter == row_number):
                    respond_result = respond_answer
                    break


            """
            row_counter = 0;  # Caveat: row_number = 0 is reserved for field description row
            for column in row_content:
                ip_hostname = column[0]
                port = column[1]
                key_words_found = column[2]
                possible_services_identified = column[3]
                exceptions_if_any = column[4]
                hash_of_page = column[5]

                row_counter = row_counter + 1;

                if (row_counter == row_number):
                    # print ("|ip_hostname=%s|port=%s|key_words_found=%s|possible_services_identified=%s|exceptions_if_any=%s|hash_of_page=%s|" % \
                    #	(ip_hostname, port, key_words_found, possible_services_identified, exceptions_if_any, hash_of_page ))
                    results = "|ip_hostname=%s|port=%s|key_words_found=%s|possible_services_identified=%s|exceptions_if_any=%s|hash_of_page=%s|" % \
                              (ip_hostname, port, key_words_found, possible_services_identified, exceptions_if_any,
                               hash_of_page)
                    break;
                else:
                    pass;

            # cursor.close();
            print("> " + results)
            """
        except:
            print("Error: unable to fetch data")

        return respond_result

    def get_column_of_given_row_of_table(self, row_number, column_number, table_name, connection):
        row_data = self.get_row_of_table(row_number, table_name, connection)

        assert column_number < len(row_data), print ("Column index ", column_number, " is out of range.")

        respond_result = row_data[column_number] # caveat: index starts from 0

        return respond_result

    def get_row_size_and_column_size_of_table(self, table_name, connection):
        row_number = 1  # just use the 1st row to count the number of fields in the 1st row
        row_data = self.get_row_of_table(row_number, table_name, connection)

        column_size = len(row_data)
        row_data_list = self.show_table (connection, table_name)
        row_size = len(row_data_list)

        return row_size, column_size

    def get_column_field_names(self, database_name, table_name, connection):
        # SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='ayahuasca' AND `TABLE_NAME`='scan_results';
        column_field_names_list = []
        sql_statement = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='" + database_name + "' AND `TABLE_NAME`='" + table_name + "';"
        column_field_names = self.execute_sql_operations(sql_statement, connection)

        for i in range(0, len(column_field_names)):
            column_field_names_list.append(str(column_field_names[i]).lstrip("'(").rstrip(",)'"))

        return column_field_names_list

    def close_deactivate_DB(self, db):
        db.close()  # disconnect from server
        print("DB de-activated.");
        return

    def who_am_i(self):  #
        """ Introspection """
        print("My name is [", self.id, "].")

        return self.id

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <mysql_lib>"
    print ("=====[" + id + " Start]===== \n")
    mysql_lib_object = mysql_lib(id)
    mysql_lib_object.who_am_i()

    trial_key = mysql_lib_object.get_trial_key()
    print('trial_key for DB: ', trial_key)

    user_id, passcode = 'root', trial_key
    [connection, cursor] = mysql_lib_object.connect_mysql(user_id, passcode)
    # Prepare SQL query to INSERT a record into the DB.
    sql_statement = """SHOW DATABASES;"""

    mysql_lib_object.execute_sql_operations(sql_statement, connection)
    db_names = mysql_lib_object.get_all_db_names(connection)
    print("db_names: ", db_names)

    mysql_lib_object.close_deactivate_DB(connection)



    # import _Gaia._gaia
    # help(mysql_lib) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2017-12-08_1700hr_26sec

mysql> status;

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name))
        db.execute(ddl)
    except pymysql.InternalError as error:
        code, message = error.args
        print ">>>>>>>>>>>>>", code, message

Note: Smita@LAPTOP-EUDO2N32 /cygdrive/c/Users/Smita/Anaconda3/Scripts
/cygdrive/c/Users/Smita/Anaconda3/Scripts/conda.exe install -c anaconda pymysql
"""