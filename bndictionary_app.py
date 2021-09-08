import time
import pymongo
import sqlite3

def encrypt():
    pass
# same as decrypt function
def decrypt(bArr):
    PASSWORD = ")@5D$k#*!"
    ENCRYPTION_KEYS = bytearray(PASSWORD)
    length = len(ENCRYPTION_KEYS)
    length2 = len(bArr)
    for i in length2:
        bArr[i] = (ENCRYPTION_KEYS[i % length] ^ bArr[i])
    return bArr

def main():
    
    print("Start")

    con = sqlite3.connect(r'D:\PythonProject\dictionary_project\data\pbd400.db')
    cur = con.cursor()
    # PASSWORD = ")@5D$k#*!"
    # ENCRYPTION_KEYS = bytearray(PASSWORD)
    # for row in cur.execute('SELECT serial,word FROM eng WHERE word = "ANT"'):
    #     print(row)
    # result = cur.execute(f"SELECT word FROM other WHERE serial = {row[0]} ")
    # print(result)
    # for bn in result:
    #     print(bn[0])

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["bengali_dictionary_app"]
    mycol = mydb["words"]
    # print(help(pymongo))

    # Creating a list of records which we 
    # insert in the collection using the
    # update_many() method.
    # mylist = [
    #     { "_id": 1, "name": "Vishwash", "Roll No": "1001", "Branch":"CSE"},
    #     { "_id": 2, "name": "Vishesh", "Roll No": "1002", "Branch":"IT"},
    #     { "_id": 3, "name": "Shivam", "Roll No": "1003", "Branch":"ME"},
    #     { "_id": 4, "name": "Yash", "Roll No": "1004", "Branch":"ECE"},
    # ]

    # In the above list _id field is provided so it inserted in 
    # the collection as specified.
    
    # Inseting the entire list in the collection
    # mycol.insert_many(mylist)
    # print collection statistics
    # print( mydb.command("collstats", "events"))

    # print database statistics
    print( mydb.command("dbstats"))
    # mongo_docs = []
    words = list()

    # for index, word in enumerate(cur.execute("SELECT word FROM eng")):
    #     words.append(word)
    # for word in words:
    #     # print(word[0])
    #     try:
    #         row = cur.execute(f'SELECT serial,word FROM eng WHERE word = "{word[0]}"')
    #         serial = row.fetchone()[0]
    #     except TypeError:
    #         pass
    #     # print(row.fetchone()[0])
    #     for bn in cur.execute(f'SELECT word FROM other WHERE serial = "{serial}"'):
    #         # doc_body = {"word": word[0], "bn_meanings": bn[0]}
    #         # mongo_docs.append(doc_body)
    #         print(f"{index} {word[0]} {bn[0]}")

    # mycol.insert_many(mongo_docs)
    # print("Successfully saved to mongodb local.")
    # print(cur.fetchall())
    # Save (commit) the changes
    # con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    # close sqlite connection...
    con.close()
    # close mongodb connection.. 
    # client.close()

if(__name__ == "__main__"):
    main()