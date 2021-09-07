import pika

# establish connection to broker on local machine
con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# establish channel
channel = con.channel()

# declare a queue
channel.queue_declare(queue='churchill')


# register a call back
def callback(ch, method, properties, body):
    print(body)


# consume received messages
channel.basic_consume(queue='churchill',
                      auto_ack=True,
                      on_message_callback=callback)

# output to standard output.
print('Hold for incomming messages. To exit press CTRL+C')
channel.start_consuming()