import requests

class Connection(object):
    # mapquest API Key
    KEY = "xwWAq0XyW2WYOp2DcAJDFcPeCOuunXwg"

    """check if the class has an instance,if not, a new one is created and returned. ohterwise the existing instance is returned. 
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance
    
        
    def getConnection(self,start,end):
         #url needs the API key, a startpoint and an end point along with some route perameters
        #the request is set to return in XML format
        url = (f"https://www.mapquestapi.com/directions/v2/route?key={Connection.KEY}&from={start}&to={end}&outFormat=xml&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false")

        
        connection = requests.get(url)

        return connection
