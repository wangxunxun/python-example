
try:
  import SocketServer
except Exception as e:
  import socketserver as SocketServer

import re
import socket

class ClientError(Exception):
  pass


class PythonChatServer(SocketServer.ThreadingTCPServer):

  def __init__(self, server_address, RequestHandlerClass):
    SocketServer.ThreadingTCPServer.__init__(self, server_address, RequestHandlerClass)
    self.users = {}


class RequestHandler(SocketServer.StreamRequestHandler):

  NICKNAME = re.compile('^[A-Za-z0-9_-]+$')

  def handle(self):
    self.nickname = None

    self.privateMessage("Who are you?")
    nickname=self._readline()
    done = False
    try:
      self.nickCommand(nickname)
      self.privateMessage('Hello %s, welcome to the Python Chat Server.' % nickname)
      self.broadcast('%s has joined the chat.' %nickname,False)
    except (ClientError) as error:
      self.privateMessage(error.args[0])
      done = True
    except socket.error:
      done = True

    while not done:
      try:
        done = self.processInput()
      except (ClientError) as error:
        self.privateMessage(str(error))
      except socket.error:
        done = True

  def finish(self):
    if self.nickname:
      message = '%s has quit.' % self.nickname
      if hasattr(self, 'partingWords'):
        message = '%s has quit: %s' % (self.nickname, self.partingWords)
      self.broadcast(message, False)

      if self.server.users.get(self.nickname):
        del(self.server.users[self.nickname])
    self.request.close()

  def processInput(self):
    done = False
    l = self._readline()
    command, arg = self._parseCommand(l)
    if command:
      done = command(arg)
    else:
      l = '<%s> %s\n' % (self.nickname, l)
      self.broadcast(l)
    return done

  def nickCommand(self,nickname):
    if not nickname:
      raise ClientError('No nickname provided.')
    if not self.NICKNAME.match(nickname):
      raise ClientError('Invalid nickname: %s' % nickname)
    if nickname == self.nickname:
      raise ClientError('You\'re already known as %s.' % nickname)
    if self.server.users.get(nickname,None):
      raise ClientError('There\'s already a user named "%s" here.' %nickname)
    oldNickname = None
    if self.nickname:
      oldNickname=self.nickname
      del(self.server.users[self.nickname])
    self.server.users[nickname]=self.wfile
    self.nickname=nickname
    if oldNickname:
      self.broadcast('%s is now known as %s' % (oldNickname, self.nickname))

  def quitCommand(self, partingWords):
    if partingWords:
      self.partingWords = partingWords
    return True

  def namesCommand(self, ignored):
    self.privateMessage(', '.join(self.server.users.keys()))

  def broadcast(self, message, includeThisUser=True):
    message = self._ensureNewline(message)
    for user, output in self.server.users.items():
      if includeThisUser or user != self.nickname:
        output.write(message.encode('utf-8'))

  def privateMessage(self, message):
    self.wfile.write(self._ensureNewline(message).encode('utf-8'))

  def _readline(self):
    return self.rfile.readline().strip().decode('utf-8')

  def _ensureNewline(self, s):
    if s and s[-1] !='\n':
      s += '\r\n'
    return s

  def _parseCommand(self, input):
    commandMethod, arg = None, None
    if input and input[0]=='/':
      if len(input) < 2:
        raise ClientError('Invalid command: "%s"' % input)
      commandAndArg = input[1:].split(' ',1)
      if len(commandAndArg) == 2:
        command, arg = commandAndArg
      else:
        command = commandAndArg[0]
      commandMethod = getattr(self, command + 'Command', None)
      if not commandMethod:
        raise ClientError('No such command: "%s"' %command)
    return commandMethod, arg


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 3:
    print('Usage: %s [hostname] [port number]' %sys.argv[0])
    sys.exit(1)
  hostname = sys.argv[1]
  port = int(sys.argv[2])
  PythonChatServer((hostname,port),RequestHandler).serve_forever()