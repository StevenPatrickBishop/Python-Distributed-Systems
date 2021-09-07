from xmlrpc.client import ServerProxy
import sys
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
elif len(sys.argv) != 5:
    errors = True
    error_message = f"\n\n Expecting 4 arguments: {len(sys.argv) - 1} given\n\n"

else:
    try:  # test for numeric percent value
        num_test = int(sys.argv[2])
        num_test = int(sys.argv[3])
        num_test = int(sys.argv[4])
        
    except ValueError as e:  # catch numeric value exception
        errors = True
        error_message = f"\n\n Port or integers given in an improper format... port: {sys.argv[2]}, int x: {sys.argv[3]}, int y: {sys.argv[4]}\n\n"


if not errors:


    #get server and port
    host = sys.argv[1]     #"localhost"
    port =  int(sys.argv[2])    #8000

    #establish connection to server
    serverAddress = "http://%s:%s/" % (host,port)
    proxy = ServerProxy(serverAddress)
    
    x = int(sys.argv[3])
    y = int(sys.argv[4])

    def main():
        print(proxy.name())
        print(proxy.serverTime())
        print(proxy.add(x,y))
        print(proxy.sub(x,y))
        print(proxy.mult(x,y))
        print(proxy.div(x,y))
        serverHelp = proxy.help()
        for key in serverHelp:
            print(key,':', serverHelp[key],'\n')


    if __name__ == "__main__":
        main()

else:
    print(error_message)  # print error message if main logic is not run