
import os
from google.cloud import bigquery
import loggerutility as logger

class GoogleBigQuery:
    def getConnection(self, dbDetails):
        pool = None
        if "con_fileName" in dbDetails.keys():
            if len(dbDetails["con_fileName"]) != "" : 
                con_fileName = dbDetails["con_fileName"]
        
        if "DATABASE" in dbDetails.keys():
            if len(dbDetails["DATABASE"]) != "" : 
                databaseName = dbDetails["DATABASE"]
        
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = con_fileName
        pool = bigquery.Client(project=databaseName)
        if pool != None:
            logger.log(f'\n Connected to GoogleBigQuery DB', "0")    

        return pool 

# dbDetails={"DATABASE":"firstproject-361804", "con_fileName":"/home/base/Downloads/firstproject.json"}

# googleData = GoogleBigQuery()
# googleData1 = googleData.getConnection(dbDetails)
# logger.log(f'\n Return Data Fron GoogleBigQuery : {googleData1}', "0")


