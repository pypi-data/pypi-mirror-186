
import os, re
import pandas as pd
import loggerutility as logger

class FileURL:
    def getFile(self, dbDetails):
        
        if 'URL' in dbDetails.keys():
            if dbDetails.get('URL') != None:
                filePath = dbDetails['URL']
        
        logger.log(f"FilePath::: {filePath}","0")
        try:

            if os.path.exists(filePath):
                return True
            else:
                raise Exception("File not found.")

        except Exception as e:
            logger.log(f"exception in File-Url:: {e}","0")
            raise e

    def getData(self, calculationData):
        dfObject=None
        try:
            if 'dbDetails' in calculationData.keys() and calculationData.get('dbDetails') != None:
                if calculationData.get('dbDetails')['URL'] != None:
                    filePath = calculationData['dbDetails']['URL']

            if 'source_sql' in calculationData.keys():
                if calculationData.get('source_sql') != None:
                    sqlQuery = calculationData['source_sql']

            if os.path.exists(filePath):
                if filePath[-3:] == "csv" :
                    dfObject = pd.read_csv(filePath)
                elif filePath[-4:] == "xlsx" :
                    dfObject = pd.read_excel(filePath)
                else:
                    logger.log(f"Invalid file type","0") 
                    raise Exception("Invalid file type")     
            else:
                logger.log(f"File does not exist at ::: {filePath}","0")  

            columnNameStr= sqlQuery[7:sqlQuery.find("from")].strip()
            if "," in columnNameStr:
                columnNameStr=columnNameStr.split(",")
                columnNameList=[i.strip() for i in columnNameStr]
                dfObject = dfObject[columnNameList]
                logger.log(f" FileURL df:: {dfObject}","0")
            else:
                dfObject = dfObject[columnNameStr].to_frame()  
                logger.log(f" FileURL df:: {dfObject}","0")
            return dfObject
        
        except Exception as e:
            logger.log(f'\n Print exception returnString inside FileURL getData() : {e}', "0")
            raise Exception(e)
            
        