# zmqpubsubdemo

Python demo Publisher and Subscriber are using ZMQ. The public IP adress of IMEC server is 193.190.127.147, and port 2001. 
To retrieve data from VS8 from a particular topic you give in the name of the topic and a callback funtion to receive and process the data.

## Installation
1. Open a new terminal and download this repository: 
- `git clone https://gitlab.ilabt.imec.be/vcharpentier1/zmqpubsubdemo.git`
2. Install pip3
- `sudo apt-get update`
- `sudo apt-get -y install python3-pip`
2. Install pyzmq
- `sudo pip3 install pyzmq`

### Run the Publisher
- `cd zmqpubsubdemo`
- `python3 publisher.py`

### Run the Subscriber
- `cd zmqpubsubdemo`
- `python3 subscriber.py`

