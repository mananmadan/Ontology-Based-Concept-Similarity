import jsonrpc
from jsonrpc import ServerProxy,JsonRpc20,TransportTcpIp
from simplejson import loads
import nltk
import pandas as pd
def coref_resolution(text):
    server = ServerProxy(JsonRpc20(),
                             TransportTcpIp(addr=("127.0.0.1", 8080)))

    result = loads(server.parse(text))
    return result['coref']
text = "Obama is the the president of US. Florida is a nice place. It is good. He lives in Florida. Trump is the current president. He owns Trump tower"
type(text)
coref_resolution(text)