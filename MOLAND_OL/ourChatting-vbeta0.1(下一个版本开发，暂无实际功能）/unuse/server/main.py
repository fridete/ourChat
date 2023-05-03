#server
import socket
import time
from threading import Thread


class Server:
    
    #init function
    def __init__(self):
        self.server = socket.socket()
        self.server.blind("127.0.0.1",8989)
        self.server.listen(5)
        #all client
        self.clients=[]
        #name and ip
        self.clients_name_ip={}
    
    def get_conn(self):
        while True:
            #get the information of the cilent
            client,address=self.server.accept()
        print(address)
        data="the server is connectted!please enter your name and the password"