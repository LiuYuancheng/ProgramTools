# encoding: utf-8
# zmq worker dealer example: https://gist.github.com/anopheles/3706633


import zmq
from collections import defaultdict

context = zmq.Context()
client = context.socket(zmq.ROUTER)
client.bind("tcp://*:5556")

poll = zmq.Poller()
poll.register(client, zmq.POLLIN)
counter = defaultdict(int)

while True:
    # handle input
    sockets = dict(poll.poll(1000))
    if sockets:
        identity = client.recv()
        msg = client.recv()
        counter[identity] += 1
    
    # start recording
    for identity in counter.keys():
        client.send(identity, zmq.SNDMORE)
        client.send("START")

    print(counter)



# encoding: utf-8

import random
import zmq
import time

context = zmq.Context()
worker = context.socket(zmq.DEALER)
worker.setsockopt(zmq.IDENTITY, str(random.randint(0, 8000)))
worker.connect("tcp://localhost:5556")
start = False
worker.send("Hello")
while True:
    if start:
        worker.send("recording data: %s" % random.randint(0,100))
        time.sleep(0.5)
    request = worker.recv()
    if request == "START":
        start = True
    if request == "STOP":
        start = False
    if request == "END":
        print "A is finishing"
        break



