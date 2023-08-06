import pymssql as ms_sql
import loggerutility as logger

class SQLServer:
    def getConnection(self, dbDetails):  
        logger.log(f"inside Ms-Sql getConnection","0") 
        uid  = ""                                             
        pwd  = ""                                             
        url  = ""                                             
        pool = None
        database = ""
        
        if 'NAME' in dbDetails.keys():
            if dbDetails.get('NAME') != None:
                uid = dbDetails['NAME']
        
        if 'KEY' in dbDetails.keys():
            if dbDetails.get('KEY') != None:
                pwd = dbDetails['KEY']
        
        if 'URL' in dbDetails.keys():
            if dbDetails.get('URL') != None:
                url = dbDetails['URL']

        if 'DATABASE' in dbDetails.keys():
            if dbDetails.get('DATABASE') != None:
                database = dbDetails['DATABASE']

        try:
            pool = ms_sql.connect(host=url, user=uid, password=pwd, database=database)
            if pool !=None:
                logger.log(f"Connected to Ms-Sql DB.","0")
        
        except Exception as e:
            logger.log(f"Issue in Ms-Sql connection.{e}","0")
            
            raise e
            
        return pool
