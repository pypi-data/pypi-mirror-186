import traceback
from flask import request
import json
from .Oracle import Oracle  
from .SAPHANA import SAPHANA
from .InMemory import InMemory
from .Dremio import Dremio
from .MySql import MySql
from .ExcelFile import ExcelFile
from .Postgress import Postgress
from .MSSQLServer import MSSQLServer
from .Tally import Tally
import loggerutility as logger
from .FileURL import FileURL
from .RestAPI import RestAPI


class TestDBConnection:
    def getConnectionStatus(self ):
        logger.log(f'\n Inside TestDBConnection', "0")
        dbDetails = request.get_data('dbDetails', None)
        dbDetails = dbDetails[10:]
        dbDetails= json.loads(dbDetails)
        logger.log(f'\n TestDBConnection dbDetails : {dbDetails}{type(dbDetails)}', "0")
        
        pool=None
        if dbDetails != None:
            try:
                if dbDetails['DB_VENDORE'] == "FileURL":
                    klass = globals()[dbDetails['DB_VENDORE']]
                    fileObject = klass()
                    fileStatus = fileObject.getFile(dbDetails)
                    if fileStatus:
                        logger.log(f"File exists","0")
                        return "SUCCESS"
                        
                elif dbDetails['DB_VENDORE'] == "RestAPI":
                    klass = globals()[dbDetails['DB_VENDORE']]
                    fileObject = klass()
                    apiStatus = fileObject.testAPI(dbDetails)
                    if apiStatus == '200':
                        logger.log(f"Response-200","0")
                        return "SUCCESS"
                    
                else:    
                    klass = globals()[dbDetails['DB_VENDORE']]
                    dbObject = klass()
                    pool = dbObject.getConnection(dbDetails)
                    
                    if pool != None:
                        logger.log(f"SUCCESS","0")
                        return "SUCCESS"
                        
                    else:
                        logger.log(f"UNSUCCESSFUL","0")
                        return "UNSUCCESSFUL"
            except Exception as e:
                logger.log(f"TestDBConnection issue: {e}","0")
                trace = traceback.format_exc()
                descr = str(e)
                return self.getErrorXml( "Connection Failed", descr, trace)
    
    def getErrorXml(self, msg, descr, trace):

        errorXml = '''<Root>
                        <Header>
                            <editFlag>null</editFlag>
                        </Header>
                        <Errors>
                            <error type="E">
                                <message><![CDATA['''+msg+''']]></message>
                                <description><![CDATA['''+descr+''']]></description>
                                <trace><![CDATA['''+trace+''']]></trace>
                                <type>E</type>
                            </error>
                        </Errors>
                    </Root>'''

        return errorXml
