
def toDeleteAllRecord(Db,Collection,check,drop):
    #to delete only one record
    if(check==1):
        try:
            recordToDelete={"plate_number":drop}
            Collection.delete_one(recordToDelete)
            print("deleted Record" + drop)
        except Exception:
            print(Exception)
    elif(check==2):
    #to delete all records
        try:
            Db.drop_collection("CAM1")
            print("deleted all records")
        except Exception:
            print(Exception)