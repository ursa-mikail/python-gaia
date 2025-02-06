####################################
import sys

from pymongo import MongoClient
from pymongo import errors

class mongodb_lib:
    """ Template model of Gaia """
    def __init__(self, id):
        self.id = id;
        self.max_server_selection_delay = 20 # Assume 20 ms maximum server selection delay
        print ("_gaia object [%s] is born\n" % self.id);

    def connect_mongodb (self, user_id, passcode):
        # server must be turn on 1st
        try:
            # connection = MongoClient()    # mongod  # no mandate of password for access
            connection = MongoClient('mongodb://' + user_id + ':' + passcode + '@localhost:27017/',
                                 serverSelectionTimeoutMS = self.max_server_selection_delay)  # mongod --auth # with --auth to mandate password for access

            print("Servers connected ... \n Server Details: ",
                  connection.server_info())  # force connection on a request as connect=True parameter of MongoClient seems to be useless here
            print(connection.database_names())  # Return a list of db, equal to: > show dbs
            print('===========================================')
        except (errors.ServerSelectionTimeoutError, errors.ConnectionFailure) as err:
            print(err)
            print("Server not available")

            sys.exit()

        return connection

    def get_all_db_names (self, connection):
        db_names = connection.database_names()

        return db_names

    def if_db_exists (self, connection, db_target_name):  #
        db_names = self.get_all_db_names(connection)
        status_found = False

        if (db_target_name in db_names):
            print("Database [", db_target_name, "] exists.")
            status_found = True
        else:
            for db_name in db_names:
                print("Database [", db_name, "].")

        return status_found

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
    id = "Library Agent: Internal Agent <mongodb_lib>"
    print ("=====[" + id + " Start]===== \n")
    mongodb_lib_object = mongodb_lib(id)
    mongodb_lib_object.who_am_i()

    # import _Gaia._gaia
    # help(mongodb_lib) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2017-12-02_1700hr_26sec
"""