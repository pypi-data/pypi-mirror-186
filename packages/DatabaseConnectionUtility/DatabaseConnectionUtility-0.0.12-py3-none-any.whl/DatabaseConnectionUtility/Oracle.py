import cx_Oracle as db
import os
import loggerutility as logger

class Oracle:
    def getConnection(self, dbDetails):   
        logger.log(f"inside oracle method", "0")
        os.environ["LD_LIBRARY_PATH"] = "/lib/oracle/19.9/client64/lib/"
        os.environ["ORACLE_HOME"] = "/lib/oracle/19.9/client64/lib/"

        #For sun release uncomment below 2 lines and comment above 2 lines 
        #os.environ["LD_LIBRARY_PATH"] = "/data/usr/lib/oracle/19.9/client64/lib/"
        #os.environ["ORACLE_HOME"] = "/data/usr/lib/oracle/19.9/client64/lib/"
    
        uid   = ''
        pwd   = ''
        url   = ''
        pool  = None
        isPool  = 'false'
        minPool = 2
        maxPool = 100
        timeout = 180
        
        if 'isPool' in dbDetails.keys():
            if dbDetails.get('IS_POOL') != None:
                isPool = dbDetails['IS_POOL']

        if 'minPool' in dbDetails.keys():
            if dbDetails.get('MIN_POOL') != None:
                minPool = int(dbDetails['MIN_POOL'])

        if 'maxPool' in dbDetails.keys():
            if dbDetails.get('MAX_POOL') != None:
                maxPool = int(dbDetails['MAX_POOL'])

        if 'timeout' in dbDetails.keys():
            if dbDetails.get('TIMEOUT') != None:
                timeout = int(dbDetails['TIMEOUT'])
        
        if 'NAME' in dbDetails.keys():
            if dbDetails.get('NAME') != None:
                uid = dbDetails['NAME']
        
        if 'KEY' in dbDetails.keys():
            if dbDetails.get('KEY') != None:
                pwd = dbDetails['KEY']
        
        if 'URL' in dbDetails.keys():
            if dbDetails.get('URL') != None:
                url = dbDetails['URL']  
        
        logger.log(f'dbDetails in Oracle class: {dbDetails}','0')
        if isPool == 'true' :
            pool = db.SessionPool(user=uid, password=pwd, dsn=url, min=minPool, max=maxPool, increment=1, encoding="UTF-8")
        else:
            try:
                pool = db.connect(user = uid, password = pwd, dsn = url)
                pool.callTimeout = timeout * 1000     

                if pool != None:
                    logger.log(f"Connected to oracle DB.","0")
                    logger.log(f'connection object oracle: {pool}','0')
            except Exception as e :
                logger.log(f"exception in oracle dbConnect {e}","0")
                raise e

        return pool
