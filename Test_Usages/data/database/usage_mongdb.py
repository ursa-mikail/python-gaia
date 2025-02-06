import os, sys
# point to path
lib_path = os.path.abspath('../../../Libraries/data/database')
sys.path.append(lib_path)

from mongodb_lib import mongodb_lib

if __name__ == "__main__":
    passcode, user_id = 'ursa', 'ursa' # root

    id_mongodb_lib = "Test Usage Agent <mongodb_lib>"
    print ("=====[" + id_mongodb_lib + " Start]===== \n")
    mongodb_lib_object = mongodb_lib(id_mongodb_lib)
    client = mongodb_lib_object.connect_mongodb (user_id, passcode)

    db_ursa_name, collection_name = 'ursa_db', 'events'

    db = client[db_ursa_name] # create DB
    collection = db[collection_name] # create collection
    print("databases: ", client.database_names())

    mongodb_lib_object.if_db_exists(client, db_ursa_name)

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

    """
    query = {
            "publication_date": {
             "$gte": datetime(2015, 9, 1)
        },
            "likes": {
                "$gt": 5
            }
        }
    """
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

    mongodb_lib_object.if_db_exists(client, db_ursa_name)

    client.close()
    print("=====[" + id_mongodb_lib + " End]===== \n")

# https://marcobonzanini.com/2015/09/07/getting-started-with-mongodb-and-python/
# https://bruceelgort.com/2014/03/20/mongodb-and-python-a-simple-example/