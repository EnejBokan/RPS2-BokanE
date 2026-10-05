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
def insertData (visina, teza, itm):
    
    sql ="""
    INSERT INTO dnevnik (datumCas, visina, teza, itm)
    VALUES0(NOW(), {}, {}, {});
    """.format(visina, teza, itm)
    
    try:
        mydb =dbconfig.dbConnect()
        cursor = mydb.cursor()
        mydb.commit()
        vrniID = cursor.lastrowid
        return vrniID
    except:
        return -1
    finally:
        cursor.close()
        mydb.close()