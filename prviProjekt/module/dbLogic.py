from module import dbConfig
from module.objects import dnevnikObj

def getAll ():
    
    sql = """
    SELECT d.id, d.datumCas, d.visina, d.teza, d.itm FROM dnevnik d;
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
        cursor.close()
        mydb.close()

def insertData (visina, teza, itm):
    
    sql ="""
    INSERT INTO dnevnik (datumCas, visina, teza, itm)
    VALUES0(NOW(), {}, {}, {});
    """.format(visina, teza, itm)
    
    try:
        mydb =dbconfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()
        vrniID = cursor.lastrowid
        return vrniID
    except:
        return -1
    finally:
        cursor.close()
        mydb.close()