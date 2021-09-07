from xmlrpc.server import SimpleXMLRPCServer
import sys
import time
import os
import os.path


# ************************ General Error Handling *********************************

# flag for program errors
errors = False
error_message = ""

# test for a valid file in directory
if not (os.path.exists(sys.argv[0])):
    errors = True
    error_message = f"\n\n Given file cannot be found! {sys.argv[1]}\n\n"

# test for valid argument quantities
elif len(sys.argv) != 3:
    errors = True
    error_message = f"\n\n Expecting 2 arguments: {len(sys.argv) - 1} given\n\n"

else:
    try:  # test for numeric percent value
        num_test = int(sys.argv[2])

        
    except ValueError as e:  # catch numeric value exception
        errors = True
        error_message = f"\n\n Port given in an improper format {sys.argv[2]}\n\n"


if not errors:

  # ************************      Setup       *********************************

    #get server and port
    host = sys.argv[1]     #"localhost"
    port =  int(sys.argv[2])    #8000

    #define and create server
    server = SimpleXMLRPCServer((host, port))


 # ************************ Function definitions *********************************

        
    def main():  #listen for client interaction
        print(f"Listening on port {port}...")
        server.serve_forever()

    def name(): #Returns the server name passed on command line
        serverName = "Server Name: %s, %s on port:%s " % (host, server.server_address[0],server.server_address[1])
        return serverName

    def help(): #List of the supported server procedures
        helpDict = {
            "Help Overview" : "List of the supported server procedures",
            "name()" : "Returns the server name passed on command line",
            "help()" : "Returns a list of supported procedures",
            "serverTime()" : "Returns current time at server 24h format",
            "add(x,y)" : "Returns sum of x and y (x + y)",
            "sub(x,y)" : "Returns difference of x and y (x - y)",
            "mult(x,y)" : "Returns product of x and y (x * y)",
            "div(x,y)" : "Returns quotient of x and y (x / y)"
        }
        return helpDict

    def serverTime(): #Returns current time at server 24h format
        serverTime = time.strftime('%H:%M:%S')
        return (f"Time at the server is: {serverTime}")

    def add(x,y): #Returns sum of x and y (x + y)
        sum = x + y
        return (f"{x} + {y} = {sum}")  

    def sub(x,y): #Returns difference of x and y (x - y)
        difference = x - y
        return (f"{x} - {y} = {difference}")  

    def mult(x, y):  #Returns product of x and y (x * y)
        product = x * y
        return (f"{x} * {y} = {product}") 

    def div(x,y): #Returns quotient of x and y (x / y)
        if y == 0:
            return "Divide by zero error"
        else:
            quotient = x / y
            return (f"{x} / {y} = {quotient}") 

    #register functions with server
    server.register_function(name, "name")
    server.register_function(help, "help")
    server.register_function(serverTime, "serverTime")
    server.register_function(add, "add")
    server.register_function(sub, "sub")
    server.register_function(mult, "mult")
    server.register_function(div, "div")

    

    if __name__ == "__main__":
        main()


else:
    print(error_message)  # print error message if main logic is not run