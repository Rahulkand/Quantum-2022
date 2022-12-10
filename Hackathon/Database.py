import pymongo
from insert import create
import Retrive
# from Delete import *
import random
from location import locations


key="mongodb+srv://backupnhce:backup@recognization.7lwvemz.mongodb.net/test"
try:
    cluster = pymongo.MongoClient(key)
    print("Connected Successfully")
    Db = cluster["Licence_Number_DB"]
    Collection = Db["CAM"]
except Exception:
    print( Exception)






location = input("Enter to which camera the data to be appended")
def randomnum():
    send= []
    for i in range (0,3,1):
        string = "KA"
        number = random.randint(0000,9999)
        licence_number_plate = string + str(number)
        send.append(licence_number_plate)
    return send
if(location == "Majestic"):
    
    mongo = randomnum()
    create(Db,Collection,mongo)
elif(location == "Rajankunte"):
    mongo = randomnum()
    create(Db,Collection_1,mongo)
collections = []
ln = input("Enter the NUMBER of licence plate")
Retrive.findAllRecord(Db,Collection,ln)
# check=int(input("enter the 1 to delete one record or 2 to delete many record"))
# if(check==1):
#     licence_number = input("enter the licence number to delete")
#     print(licence_number,type(licence_number))
#     toDeleteAllRecord(Db,Collection,check,licence_number)









 