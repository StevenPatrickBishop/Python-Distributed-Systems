import requests
import xml.etree.ElementTree as ET

class Directions:
    # mapquest API Key
    KEY = "xwWAq0XyW2WYOp2DcAJDFcPeCOuunXwg"

    #constructor that takes a starting address and a ending destination as arguments
    def __init__(self,start,end):
        self.url            = " "
        self.START          = start
        self.END            = end
        self.streets        = [] 
        self.cities         = []
        self.states         = []
        self.postals        = []
        self.steps          = []
        self.stepMiles      = []
        self.stepDirection  = []
        self.address        = {}
        self.route          = {}


    #peforms the REST Request
    def requestData(self):
        #url needs the API key, a startpoint and an end point along with some route perameters
        #the request is set to return in XML format
        url = (f"https://www.mapquestapi.com/directions/v2/route?key={Directions.KEY}&from={self.START}&to={self.END}&outFormat=xml&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false")

        #using element tree to handle the XML Data, returns a tree root to the caller
        response = requests.get(url)
        root = ET.fromstring(response.content) 
        return root



    def extractData(self,root):

        #using XPath to extract relevent information from the response XML into appropriate lists

        #driving direction steps
        for each in root.findall("route/legs/leg/maneuvers/maneuver/narrative"):
            self.steps.append(each.text)


        #driving direction step distance
        for each in root.findall("route/legs/leg/maneuvers/maneuver/distance"):
            self.stepMiles.append(each.text)


        #driving direction step direction
        for each in root.findall("route/legs/leg/maneuvers/maneuver/directionName"):
            self.stepDirection.append(each.text)

        # #starting point street
        for each in root.findall("route/locations/location/street"):
            self.streets.append(each.text)

        # #starting point city
        for each in root.findall("route/locations/location/adminArea5"):
            self.cities.append(each.text)

        # #starting point state
        for each in root.findall("route/locations/location/adminArea3"):
            self.states.append(each.text)

        # #starting point postal
        for each in root.findall("route/locations/location/postalCode"):
            self.postals.append(each.text)
        
        #creating dictionaries to hold extracted lists to simpify/clarify references to data
        
        self.address = {"street" : self.streets,
                        "city"   : self.cities,
                        "state"  : self.states,
                        "postal" : self.postals}

        self.route   = {"steps"     : self.steps,
                        "miles"     : self.stepMiles,
                        "direction" : self.stepDirection}

    def getStartPoint(self):
        
        #if no street address is provided, this creates a default
        if self.address['street'][0] == None:
            self.address['street'][0] = "1 Main St,"

        #if no postal code is provided, an empty placehoder is created as a default
        if self.address['postal'][0] == None:
            self.address['postal'][0] = " "

        #creates and returns a formated address for display
        start = "starting Point:\n"
        start += self.address['street'][0]
        start += "\n"
        start += self.address['city'][0]
        start += ", "
        start += self.address['state'][0]
        start += "\n"
        start += self.address['postal'][0]
        start += "\n"
        return start


    def getEndPoint(self):
        #if no street address is provided, this creates a default
        if self.address['street'][1] == None:
            self.address['street'][1] = "1 Main St,"

        #if no postal code is provided, an empty placehoder is created as a default
        if self.address['postal'][1] == None:
            self.address['postal'][1] = " "  
        
        #creates and returns a formated address for display
        end = "ending Point:\n"
        end += self.address['street'][1]
        end += "\n"
        end += self.address['city'][1]
        end += ", "
        end += self.address['state'][1]
        end += "\n"
        end += self.address['postal'][1]
        end += "\n"
        return end


    def getDirections(self):
        #creates and returns formated driving steps
        directions ="Turn By Turn Directions:\n"
        
        for i in range(len(self.route['steps'])):    
            directions += ("Step %2d: " % (i+1))
            directions += self.route['steps'][i]
            directions += "\n"
            if i < len(self.route['steps'])-1:
                directions += ("%14s %0.2f miles " % ("Drive",float(self.route['miles'][i])))
                directions += ("heading %s" % self.route['direction'][i])
                directions += "\n\n"
            
        return directions

    def getTotalMiles(self):
        #calculates total trip miles
        totalMiles = 0
        for each in self.stepMiles:
            totalMiles += float(each)
        
        return "Total Miles: %0.2f \n" % totalMiles 