from zmqpubsub.zmq_subscriber import Subscriber


# In this function the received data of VS8 in JSON format will be accessible.
def callbackFunc(message_in_json_object):
    print(message_in_json_object)
    print("")


if __name__ == '__main__':
    #  IMEC public IP: 193.190.127.147, for testing local host IP: 127.0.0.1
    subscriber = Subscriber(ip='193.190.127.147', port='2001')
    subscriber.subscribe(topic="allData", callback=callbackFunc)

