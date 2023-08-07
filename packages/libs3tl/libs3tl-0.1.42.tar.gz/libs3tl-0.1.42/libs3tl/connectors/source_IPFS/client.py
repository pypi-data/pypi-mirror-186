
import os
import requests
import sys
import json
from enum import Enum
from airbyte_cdk.models import AirbyteConnectionStatus,Status

class IPFSSource:
    """
    Source connector for IPFS Source .
    This function is used to initialize a IPFSSource object and is called when creating an instance of this class.
    It takes in a configuration dictionary containing the relevant IPFS link information necessary .

        Configuration parameters in json format:
        - IPFSURL (string): link to fetch data from ipfs source.
              
    """

    def __init__(self, config: dict, clientSelf):
        self.IPFSURL = config["IPFSURL"]
        self.clientSelf = clientSelf
       
     


    def check(self)-> AirbyteConnectionStatus:
        """
        This check() function is used to check if the url  connection is successful.
        It attempts to connect to the IPFS url provided by user  and prints a success message if successful.
        """
        try:
           
            f = requests.get(self.IPFSURL)
            if f.ok :
                self.clientSelf.logInfo(self.clientSelf.step, 'IPFS  connection successful')
                return AirbyteConnectionStatus(status=Status.SUCCEEDED)
            else :
                self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(f._content)}")
                return AirbyteConnectionStatus(status=Status.FAILED,message=str(f._content))
            
        except Exception as e:
            self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(e)}")


    

    def read(self):
        """
        Read content and store it at temperory location.
        
        """
        try:
            streamData = requests.get(self.IPFSURL)
            if streamData.ok :
                self.clientSelf.logInfo(self.clientSelf.step, ' Read Data successful')
                return  streamData
            else :
                self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(streamData._content)}")
                return streamData
        except Exception as e:
            self.clientSelf.logError(self.clientSelf.step, f"Failed to fetch the data: {str(e)}")


        
        