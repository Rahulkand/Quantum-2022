
def create (Db,Collection,number_plate):
    class recordSchema:
        def __init__(self,plate_no):
            self.plate_no = plate_no

    #array to store values retrived from OCR
    recordsCam1 = []
   

    #Creating instances
    for i in range(0,len(number_plate),1):
            object = recordSchema(number_plate[i])

            recordsCam1.append(object)

    #insert records into database
    try:
            for i in range(0,len(number_plate),1):
                Collection.insert_one({
                "plate_number" : recordsCam1[i].plate_no,

            })
                
    except Exception:
            print(Exception)