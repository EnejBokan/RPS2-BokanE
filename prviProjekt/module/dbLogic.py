from module import dbConfig

def getAll (koda = ""):
    
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.close()
        mydb.close()
        return True
        
    except:
        return False
    
    finally:
        pass