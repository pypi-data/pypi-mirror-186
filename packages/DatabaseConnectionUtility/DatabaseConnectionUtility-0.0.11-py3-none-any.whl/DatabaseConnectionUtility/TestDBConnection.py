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


class TestDBConnection:
    def getConnectionStatus(self ):
        logger.log(f'\n Inside TestDBConnection method', "0")
        dbDetails = request.get_data('dbDetails', None)
        logger.log(f'\n dbDetails 1: {dbDetails}', "0")
        dbDetails = dbDetails[10:]
        logger.log(f'\n dbDetails 2: {dbDetails}', "0")
        dbDetails= json.loads(dbDetails)
        logger.log(f'\n dbDetails 3: {dbDetails}', "0")
             
        
        pool=None
        if dbDetails != None:
            try:
            	
                klass = globals()[dbDetails['DB_VENDORE']]
                dbObject = klass()
                pool = dbObject.getConnection(dbDetails)
                
                if pool != None:
                    logger.log(f'\nSUCCESS', "0")
                    return "SUCCESS"
                else:
                    logger.log(f'\nUNSUCCESSFUL', "0")
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
