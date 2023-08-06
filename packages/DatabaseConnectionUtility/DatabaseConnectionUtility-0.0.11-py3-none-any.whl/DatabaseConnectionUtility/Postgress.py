import loggerutility as logger
import psycopg2


class Postgress:
    def getConnection(self, dbDetails):
        logger.log(f"Called Postgress getConnection.", "0")

        uid  = ""                                             
        pwd  = ""                                             
        url  = ""                                             
        port = 5432
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
            self.pool = psycopg2.connect(database=database, user=uid, password=pwd, host=url, port=port)
            if pool !=None:
                logger.log(f"\nConnected to Postgress DB.","0")
        
        except Exception as e:
            logger.log(f"\nIssue in Postgress connection.{e}","0")
            raise e
            
        return pool
