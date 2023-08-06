
### step class ###

step class consist common  functions which can be inherited by other classes  -- setTaskID, setUUID,setTaskExecutionID,startRedisConn,setLogger,loadParams,connectToAPIForKey,createAndGetResponseFromURL,getLogger,exceptionTraceback,getRelativeFile;

### extract class###

extract class consist of init method which sets all loadParams and log files .. also contains super class startup which can be defined from client extract ..  it also consist of startWs- starting websocket connection functions .;

### ML class ###

Ml class consist of startup method ,startMLSubscriber to subscribr to the incoming data ,process ml to process data   , compute ml   to do client ML computations and handoff it to  next step;


### Transform class ###

Transform class consist of startup  ,startTRSubscriber to subscribr to the incoming data , tranformExData -function has to be defined inside clientTranform with own tranform logic .It also consist of microBatchProcessRedisSortedSet  for microbatching    streaming data ./;


### Load Class ###

Load class consist of startup method , loadsubscribers to listen to the data and  client logic to  loading final data needs to be added in client load file;

### New Release Note version='0.1.34' ###

### Connectors Added ###

AzBlob Read (Azure Blob)
Using this connector you can read file from AzBlob;
for Azure Blob  Read connection , create sorce folder inside params and add spec.json with connection configs ;

AzBlob Write(Azure Blob)
Using this connector you can write file to AzBlob;
for Azure Blob  Write connection , create destination folder inside params and add spec.json with connection configs ;

SFTP Read
Using this connector you can read file from SFTP server ;
for SFTP connection , create source folder inside params and add spec.json with connection configs ;

SFTP Write
Using this connector you can read file to SFTP server
for SFTP  Write connection , create destination folder inside params and add spec.json with connection configs ;

Postgres Read
Using this connector you can read file from Postgres database;

Postgres Write
Using this connector you can read file to Postgres database;

IPFS source
you can use this connector to read  file from any  IPFS http url;
this connector contains read function which will return data in bytes format;

IPFS destination
this connector helps you to upload any file on customIPFS node;
write function in this connector uses file and target location as input and will return json consisting contentId ,name and size of file;

