import pika
from threading import Timer
import random
messegeCount = 0




def sendMessage(channel):
    
    global messegeCount
    messegeCount += 1

    def getQuote():
        quotes = [
        "We shape our dwellings, and afterwards our dwellings shape us.",
        "You have enemies? Good. It means youve stood up for something, sometime in your life.",
        "It is not enough that we do our best; sometimes we have to do what is required.",
        "Personally I am always ready to learn, although I do not always like being taught.",
        "The inherent vice of capitalism is the unequal sharing of blessings; the inherent virtue of socialism is the equal sharing of miseries.",
        "The power of man has grown in every sphere, except over himself."
        ]
        
        return "Message number %s: %s" %(messegeCount,random.choice(quotes))
        


    # send message to exchange/queue: once per second(with counter)
    channel.basic_publish(exchange='',
                        routing_key='churchill',
                        body=str(getQuote()))
 
  

def main():
   
    # establish connection to broker on local machine
    con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    # establish channel
    channel = con.channel()

    # declare a queue
    channel.queue_declare(queue='churchill')

    
    sendMessage(channel)
   

    # close connection
    con.close()
    Timer(1,main).start() 
    


if __name__ == "__main__":
    print("Currently sending messages...")
    main()