import snowflake.connector
import loggerutility as logger

class SnowFlake:
    def getConnection(self, dbDetails):  
        logger.log(f"inside SnowFlake getConnection","0") 
        uid  = ""                                             
        pwd  = ""                                             
        # url  = ""                                             
        # port = 3306
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
            self.pool = snowflake.connector.connect(account=url, database=database, user=uid, password=pwd)
        except Exception as e:
            logger.log(f"\nIssue in SnowFlake connection.{e}","0")
            
            return e
        if pool !=None:
            logger.log(f"\nConnected to SnowFlake DB.","0")
            
        return pool
