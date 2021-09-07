import requests
import xml.etree.ElementTree as ET

# start ="102 Indian Meadow Dr, Winsted, CT 06098-2221"
End = "Thomaston, CT"
KEY = "xwWAq0XyW2WYOp2DcAJDFcPeCOuunXwg"
start ="burrlington, CT"


url = (f"https://www.mapquestapi.com/directions/v2/route?key={KEY}&from={start}&to={End}&outFormat=xml&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false")

response = requests.get(url)
root = ET.fromstring(response.content)

endPointsStreet  = []
endPointsCity    = []
endPointsState   = []
endPointsPostal  = []

address ={"street" : endPointsStreet,
          "city"   : endPointsCity,
          "state"  : endPointsState,
          "postal" : endPointsPostal}


routeSteps          = []
routeStepMiles      = []
routeStepDirection  = []

route = {"steps"     : routeSteps,
         "miles"     : routeStepMiles,
         "direction" : routeStepDirection}


def extractData():
    #driving direction steps
    for each in root.findall("route/legs/leg/maneuvers/maneuver/narrative"):
        routeSteps.append(each.text)


    #driving direction step distance
    for each in root.findall("route/legs/leg/maneuvers/maneuver/distance"):
        routeStepMiles.append(each.text)


    #driving direction step direction
    for each in root.findall("route/legs/leg/maneuvers/maneuver/directionName"):
        routeStepDirection.append(each.text)


    # #starting point street
    for each in root.findall("route/locations/location/street"):
        endPointsStreet.append(each.text)

    # #starting point city
    for each in root.findall("route/locations/location/adminArea5"):
        endPointsCity.append(each.text)

    # #starting point state
    for each in root.findall("route/locations/location/adminArea3"):
        endPointsState.append(each.text)

    # #starting point postal
    for each in root.findall("route/locations/location/postalCode"):
        endPointsPostal.append(each.text)


def getstartPoint(address):
    
    if address['street'][0] == None:
        address['street'][0] = "1 Main St,"
    
    if address['postal'][0] == None:
        address['postal'][0] = " "

    start = "starting Point:\n"
    start += address['street'][0]
    start += "\n"
    start += address['city'][0]
    start += ", "
    start += address['state'][0]
    start += "\n"
    start += address['postal'][0]
    start += "\n"
    return start

def getEndPoint(address):
    
    if address['street'][1] == None:
        address['street'][1] = "1 Main St,"
    
    if address['postal'][1] == None:
        address['postal'][1] = " "  

    end = "ending Point:\n"
    end += address['street'][1]
    end += "\n"
    end += address['city'][1]
    end += ", "
    end += address['state'][1]
    end += "\n"
    end += address['postal'][1]
    end += "\n"
    return end

def getDirections(route):

    directions ="Turn By Turn Directions:\n"
    
    for i in range(len(route['steps'])):    
        directions += ("Step %2d: " % (i+1))
        directions += route['steps'][i]
        directions += "\n"
        if i < len(route['steps'])-1:
            directions += ("%14s %0.2f miles " % ("Drive",float(route['miles'][i])))
            directions += ("heading %s" % route['direction'][i])
            directions += "\n\n"
        
    return directions

def getTotalMiles(stepMiles):
    totalMiles = 0
    for each in stepMiles:
        totalMiles += float(each)
    
    return "Total Miles: %0.2f \n" % totalMiles 



def main():
    
    extractData()

    print("\n")
    print(getstartPoint(address))

    print(getDirections(route))

    print(getTotalMiles(routeStepMiles))

    print(getEndPoint(address))



if __name__ == "__main__":
    main()