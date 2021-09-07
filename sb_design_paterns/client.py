from directions import Directions
from connection import Connection


def introductoryMessage():
    print("\n\n")
    print("Welcome to the python driving directions web service app")
    print("To get driving directions, enter a starting point and an ending destination")
    print("\n")

def applicationInstructions():
    print("Acceptable formats:") 
    print(" ### street, city, state ( optional: zip/postal )")
    print(" city, state ( optional: zip/postal )")
    print(" city")
    print(" zip/postal ")
    print("\n")
    input("Press Enter to begin")
    print("\n")


def main():
    #print introduction and instructions
    introductoryMessage()
    applicationInstructions()
    
    running = True

    while running:
        # gather start and endpoints
        start   = input("Enter a start address: ")#"Thomaston, CT"
        end = input("Enter a destination address: ")#"burrlington, CT"
        print("\n")

   
        #create directions instance
        d = Directions(start,end)
        
        #print results
        try:
            print(d.getStartPoint())
            print(d.getDirections())
            print(d.getTotalMiles())
            print(d.getEndPoint())
        except:
            print("Something has gone wrong. Directions cannot be retrieved")
            print("check the start or destination address")
            print("\n")
        
        cont = input("Press Enter to get more directions or enter 0 to quit: ")
        if cont == "0":
            running = False
            print("Good Bye\n")


  


if __name__ == "__main__":
    main()