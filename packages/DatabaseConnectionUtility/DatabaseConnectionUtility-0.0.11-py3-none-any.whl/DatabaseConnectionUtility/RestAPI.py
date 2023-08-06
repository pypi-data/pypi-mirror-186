
import os, requests, json
import pandas as pd
import loggerutility as logger

class RestAPI:
    def testAPI(self, dbDetails):
        
        if 'URL' in dbDetails.keys():
            if dbDetails.get('URL') != None:
                url = dbDetails['URL']
        
        if 'KEY' in dbDetails.keys():
            if dbDetails.get('KEY') != None:
                apiToken = dbDetails['KEY']

        if 'AUTHENTICATION_TYPE' in dbDetails.keys():
            if dbDetails.get('AUTHENTICATION_TYPE') != None:
                authenticationType = dbDetails['AUTHENTICATION_TYPE']

        try:
            if authenticationType == "N":
                response = requests.get(url)
                if str(response.status_code) == '200':
                    logger.log(f"{response.url} -- {response} ","0")
                    return str(response.status_code)
                else:
                    logger.log(f"Invalid response for {response.url} {str(response)}","0")
                    raise Exception(f"Invalid response {str(response.status_code)} for {response.url}")

            elif authenticationType == "T":
                logger.log(f"Inside token-based condition","0")
                response = requests.request("POST",url + "?key="+ apiToken)
                if str(response.status_code) == '200':
                    logger.log(f"{response.url} -- {response} ","0")
                    return str(response.status_code)
                else:
                    logger.log(f"Invalid response for {response.url} {str(response)}","0")
                    raise Exception(f"Invalid response for {response.url} {str(response)}")

            elif authenticationType == "S":
                pass

            else:
                logger.log(f"Invalid authenticationType::{authenticationType}","0")
                
        except Exception as e:
            logger.log(f"exception in RestAPI:: {e}","0")
            raise e

    def getData(self, calculationData):
        columnNameList=[]
        jsonDataResponse=""
        
        logger.log(f"inside RestAPI getData() calculationData::{calculationData}","0")
        if 'dbDetails' in calculationData.keys() and calculationData.get('dbDetails') != None:
            if 'AUTHENTICATION_TYPE' in calculationData['dbDetails'] and calculationData.get('dbDetails')['AUTHENTICATION_TYPE'] != None:
                authentication_Type = calculationData['dbDetails']['AUTHENTICATION_TYPE']

            if 'URL' in calculationData['dbDetails'] and calculationData.get('dbDetails')['URL'] != None:
                serverUrl = calculationData['dbDetails']['URL']

            if 'NAME' in calculationData['dbDetails'] and calculationData.get('dbDetails')['NAME'] != None:
                userName = calculationData['dbDetails']['NAME']

            if 'KEY' in calculationData['dbDetails'] and calculationData.get('dbDetails')['KEY'] != None:
                password = calculationData['dbDetails']['KEY']
            
            if 'source_sql' in calculationData.keys():
                if calculationData.get('source_sql') != None:
                    sqlQuery = calculationData['source_sql']

        if authentication_Type == 'N':               
            try:
                response = requests.get(serverUrl)
                if str(response.status_code) == '200':
                    logger.log(f"{response.url} -- {response} ","0")
                    jsonDataResponse = response.json()
                    logger.log(f"No-Auth jsonDataResponse : {jsonDataResponse}","0")
                else:
                    logger.log(f"No-Authentication Type Response: {str(response.status_code)}","0")
            except Exception as e:
                logger.log(f'\n Print exception returnString inside auth_type-N : {e}', "0")
                raise Exception(e)

        elif authentication_Type == 'T':      
            try:
                response = requests.request("POST",serverUrl + "?key="+ password)
                if str(response.status_code) == '200':
                    logger.log(f"{response} ","0")
                    jsonDataResponse = response.json()
                    logger.log(f"Auth_Type-T jsonDataResponse : {jsonDataResponse}","0")
                else:
                    logger.log(f"Auth_Type-T Response: {str(response.status_code)}","0")
            except Exception as e:
                logger.log(f'\n Print exception returnSring inside auth_type-T : {e}', "0")
                raise Exception(e)

        elif authentication_Type == 'S':   
            try:
                session= requests.Session()
                formParam = {'USER_CODE': userName, 'PASSWORD': password, 'DATA_FORMAT':'JSON','APP_ID': 'INSIGHTCON'  }
                logger.log(f"formParam session login::::{formParam}","0")
                if "ibase" in serverUrl:
                    serverUrl[:serverUrl.find("ibase")-1]
                response = session.post(serverUrl +"/ibase/rest/E12ExtService/login?", formParam)
                if str(response.status_code) == '200':
                    status = (json.loads(response.text))['Response']['status']
                    if status == 'success':
                        logger.log(f"Session based login successful","0")
                        cookie = response.cookies
                        tokenId = json.loads((json.loads(response.text))['Response']['results'])['TOKEN_ID'] 
                        logger.log(f" TYPE_S cookie :::::{cookie} tokenid:::::::{tokenId}","0")
                        
                        if 'URL' in calculationData['dbDetails'] and calculationData.get('dbDetails')['URL'] != None:
                            serverUrl = calculationData['dbDetails']['URL']
                        
                        formParam = {'TOKEN_ID':tokenId }
                        logger.log(f"formParam visualList::::{formParam}","0")
                        response = session.post(serverUrl , formParam, cookies=cookie)
                        jsonDataResponse=json.loads(response.text)['Response']['results']
                        logger.log(f"visualList type-S : {jsonDataResponse}","0")
                        
                    elif status == 'error':
                        logger.log(f"visualList type-S : {json.loads(response.text)}","0")
                        return json.loads(response.text)
                else:
                    logger.log(f"Session Based Authentication Response: {str(response.status_code)}","0")
                
            except Exception as e:
                logger.log(f'\n Print exception returnSring inside auth_type-S : {e}', "0")
                raise Exception(e)
        
        logger.log(f"jsonDataResponse::{jsonDataResponse}","0")
        dfObject = pd.DataFrame(jsonDataResponse)
        logger.log(f"dfObject::{dfObject}","0")

        columnNameStr= sqlQuery[7:sqlQuery.find("from")].strip()
        if "," in columnNameStr:
            columnNameStr=columnNameStr.split(",")
            columnNameList=[i.strip() for i in columnNameStr]
            dfObject = dfObject[columnNameList]
            logger.log(f" RestAPI no-AuthenticationType df:: {dfObject}","0")
        else:
            dfObject = dfObject[columnNameStr].to_frame()  

        return dfObject

            
        
            
        
