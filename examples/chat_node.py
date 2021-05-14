#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (MyOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the MyOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################

import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode


HOME_PORT = int(input("Set your PORT, ideally give it some random number, e.g. 8542:"))

node_1 = MyOwnPeer2PeerNode("127.0.0.1", HOME_PORT)
node_1.start()

attempts = 5
for i in range(attempts):
    try:
        HOST = input("HOST:")
        PORT = int(input("PORT:"))
        print("Trying to connect to HOST: {}, PORT: {}".format(HOST, PORT))
        node_1.connect_with_node(HOST, PORT)
        break
    except Exception as e:
        print("Retry connection")
    if i == attempts-1:
        print("Too many connection attempts. Make sure that the other node is up")

print("Connected to HOST: {}, PORT: {}".format(HOST,PORT))

while True:
    msg = input("msg:")
    node_1.send_to_nodes(msg)
