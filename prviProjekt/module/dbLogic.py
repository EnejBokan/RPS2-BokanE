from module import dbConfig
from module.objects import dnevnikObj

def isConnected():
        
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        return True
    except:
        return False
    finally:
        cursor.close()
        mydb.close()

def getAll ():
    
    sql = """
    SELECT d.id, d.datumCas, d.visina, d.teza, d.itm FROM dnevnik d WHERE isDeleted = 0;
    """
    
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        rtn = []
        for r in result:
            obj = dnevnikObj(r[0], r[1], r[2], r[3], r[4])
            rtn.append(obj)
        return rtn
    except:
        return []
    finally:
        # cursor.close()
        # mydb.close()
        pass

def insertData (visina, teza, itm):
    
    sql ="""
    INSERT INTO dnevnik (datumCas, visina, teza, itm)
    VALUES (NOW(), {}, {}, {});
    """.format(visina, teza, itm)
    vrniID = -1
    print("****************DEBUG**************")
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()
        vrniID = cursor.lastrowid
        return vrniID
    except:
        mydb.rollback
        return vrniID
    finally:
        cursor.close()
        mydb.close()

#Brisanje vnosov v dnevniku
def brisanjeITM (id):
    sql = """
    DELETE FROM dnevnik 
        WHERE ID = {};
    """.format(id)
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()
        return True
    except:
        mydb.rollback()
        return False
    finally:
        cursor.close()
        mydb.close()
        
#Brisanje samo is Spletne strani
def softDeleteItm(id):
    
    sql = """
    UPDATE dnevnik
        SET IsDeleted = 1
        WHERE ID = {};
    """.format(id)
    print("SQL")
    print(sql)
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()
        return True
    except:
        mydb.rollback()
        return False
    finally:
        cursor.close()
        mydb.close()