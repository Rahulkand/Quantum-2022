
def findAllRecord(DB,Collection,ln):
    try:
        
        record = Collection.find_one({"plate_number":ln})
        
            
    except Exception:
        print(Exception)