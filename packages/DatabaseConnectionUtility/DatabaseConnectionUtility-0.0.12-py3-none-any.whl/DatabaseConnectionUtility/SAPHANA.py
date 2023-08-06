from pandas import DataFrame 
from hdbcli import dbapi
import loggerutility as logger

class SAPHANA:

    def getConnection(self, dbDetails):   
        logger.log(f"Called sapDB getConnection","0") 
        uid  = ''                   
        pwd  = ''                   
        url  = ''                   
        port =  443
        pool =  None
    
        if 'NAME' in dbDetails.keys():
            if dbDetails.get('NAME') != None:
                uid = dbDetails['NAME']
        
        if 'KEY' in dbDetails.keys():
            if dbDetails.get('KEY') != None:
                pwd = dbDetails['KEY']
        
        if 'URL' in dbDetails.keys():
            if dbDetails.get('URL') != None:
                url = dbDetails['URL']  

        try:
            pool = dbapi.connect(address=url, port=443, user=uid, password=pwd, encrypt='true', sslValidateCertificate='false') 
            if pool != None:
                logger.log(f'Connected to SAP DB.','0')
        
        except Exception as e:
            logger.log(f'Issue in SAP connection.{e}', '0')
            raise e
        
        
        return pool
