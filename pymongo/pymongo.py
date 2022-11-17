import sys
import pymongo
import json
import bson
import os
def main():
    query_string = {'$regex': '.*1.*'}
    from bson.json_util import loads, dumps
    myclient = pymongo.MongoClient('mongodb:')
    mydb = myclient["appstack"]
    mycol = mydb["app_info"]
    myquery = {"":query_string}
    mydoc = mycol.find(myquery)
    json_str = dumps(mydoc)
    y = json.loads(json_str)
    print("\n\n")
    print("############App list############")
    print("App count is",len(y))
    print("\nApp ID is")
    if os.path.exists("app_list.txt"):
        os.remove("app_list.txt")
    else:
        print("file does not exist")
    for index in range(len(y)):
        for key in y[index]:
            if key == "appid":
                with open("app_list.txt", "a") as f:
                    print(y[index][key], file=f)
                    print(y[index][key])
            else:
                continue

if __name__ == '__main__':
    main()