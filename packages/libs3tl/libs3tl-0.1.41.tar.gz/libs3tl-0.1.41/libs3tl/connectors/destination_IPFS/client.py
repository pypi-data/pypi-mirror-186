
import os
import requests
import sys
import json

class IPFSDestination:
    """
    destination connector for IPFS as destination .
    This function is used to initialize a IPFSdestination object and is called when creating an instance of this class.
   .

        Configuration parameters in json format:
    
    """

    def __init__(self, config: dict, clientSelf):
        self.clientSelf = clientSelf
        self.customIPFSURL = "http://20.245.125.82:5000/uploadfiletoipfs"
     


    def check(self):
        """
        This check() function is used to check if the url  connection is successful.
        It attempts to connect to the IPFS url provided by user  and prints a success message if successful.
        """
        try:
           print("check")
           
            
        except Exception as e:
            self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(e)}")


    

    def read(self, query: str = None):
        """
        Read content and store it at temperory location.
        
        """
        try:
            print("test")
          

        except Exception as e:
            self.clientSelf.logError(self.clientSelf.step, f"Failed to fetch the data: {str(e)}")

    def getRelativeFile(self, filename):
        # dirname = os.path.dirname(__file__) ## python directory should not be fetched  using __file__
        dirname = sys.path[0] + '/'
        filename = os.path.join(dirname, filename)
        return filename
   
    def write(self,path, MyFiles):
        """
        This function is used to write data  on the IPFS node. It takes in the file object . 
        It tries to uploade file on private IPFS node and return output object with file ,hash, uploaded size and url to access it .
        """

        print(path,MyFiles)
        
        try:
            if path :         
                newURL = self.customIPFSURL + "?dir_path=" + str(path)
            else :
                newURL = self.customIPFSURL
            x = requests.post(newURL, files =MyFiles)
                 
            if x.ok :
                self.clientSelf.logInfo(self.clientSelf.step, 'IPFS  connection successful')
                
                outputContent = json.loads(x.content)
                FinalURL= 'http://20.245.125.82:8080/ipfs/'+ str(outputContent['Hash'])
                FinalOutpUT= {'name':outputContent['Name'],'Hash':outputContent['Hash'],'Size':outputContent['Size'],'URL':FinalURL}
                self.clientSelf.logInfo(self.clientSelf.step, str(FinalOutpUT))
                return  FinalOutpUT
            else :
                print (x.text)
                self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(x._content)}")
                return x.content
            
        except Exception as e:
            self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(e)}")
  