import pyodbc as pyod 
import loggerutility as logger

class Dremio:
    def getConnection(self, dbDetails):   
        logger.log(f'inside dremio getConnection','0')
        uid  = ""
        pwd  = ""
        url  = ""
        pool = None
        port = 31010
        driver = "/opt/dremio-odbc/lib64/libdrillodbc_sb64.so"
        
        if 'NAME' in dbDetails.keys():
            if dbDetails.get('NAME') != None:
                uid = dbDetails['NAME']
        
        if 'KEY' in dbDetails.keys():
            if dbDetails.get('KEY') != None:
                pwd = dbDetails['KEY']
        
        if 'URL' in dbDetails.keys():
            if dbDetails.get('URL') != None:
                url = dbDetails['URL']
        
        logger.log(f'dbDetails Dremio class: {dbDetails}', '0' )
        try:
            pool = pyod.connect("Driver={};ConnectionType=Direct;HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(driver,url,port,uid,pwd),autocommit=True)
            if pool != None:
                logger.log(f'Connected to Dremio DB.','0')
        
        except Exception as e:
            logger.log(f'Issue in Dremio connection.{e}','0')
            raise e
        
        return pool
