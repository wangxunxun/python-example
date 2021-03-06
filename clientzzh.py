import socket
import select
import sys
import os
from threading import Thread


class ChatClient:

    def __init__(self, host, port, nickname):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.input = self.socket.makefile('rb', 0)
        self.output = self.socket.makefile('wb', 0)
        

        authenticationDemand = self.input.readline().decode('utf-8')
        if not authenticationDemand.startswith("Who are you?"):
            raise Exception ("This doesn't seem to be a Python Chat Server.")
        self.output.write((nickname + '\r\n').encode('utf-8'))
        response = self.input.readline().strip().decode('utf-8')
        if not response.startswith("Hello"):
            raise Exception (response)
        print(response)

        self.output.write(('/names\r\n').encode('utf-8'))
        print("Currently in the chat room:", self.input.readline().decode('utf-8').strip())

        self.run()
 
    def run(self):        
        propagateStandardInput = self.PropagateStandardInput(self.output)
        propagateStandardInput.start()
        inputText = True
        while inputText:
            inputText = self.input.readline().decode('utf-8')
            if inputText:
                print (inputText.strip())
        propagateStandardInput.done = True

    class PropagateStandardInput(Thread):
        def __init__(self, output):
            Thread.__init__(self)
            self.setDaemon(True)
            self.output = output
            self.done = False

        def run(self):
            while not self.done:
                inputText = sys.stdin.readline().strip()
                if inputText:
                    self.output.write((inputText + '\r\n').encode('utf-8'))


if __name__ == '__main__':
    hostname = 'localhost'
    port = 50007
    nickname = 'test1'



    ChatClient(hostname, port, nickname)