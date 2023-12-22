import argparse
import cmd
from http import client
from msilib.schema import SelfReg
import socket
import shlex
import subprocess
import sys
import textwrap
import threading
from typing import Self

from networkx import selfloop_edges

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
output.decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BHP Net Tool', formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent('''Example: 
shellcat.py -t 192.168.1.108 -p 5555 -l # command shell 
shellcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
shellcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
echo 'ABC' | ./shellcat.py -t 192.168.1.108 -p 135 # echo text to server port 135 
shellcat.py -t 192.168.1.108 -p 5555 # connect to server
'''))
    
parser.add_argument('- c', '--command', action='store_true', help='command shell')
parser.add_argument('-e', '--execute', help='execute specified command')
parser.add_argument('-l', '--listen', action='store_ture', help='listen')
parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
parser.add_argument('-u', '--upload', help='upload file')
args = parser.parse_args()
if args.listen:
    buffer = ''
else:
    buffer = sys.stdin.read()

nc = ShellCat(args, buffer.encode())
nc.run()

class ShellCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def run(self):
    if self.args.listen:
        self.listen()
    else:
        self.send()

def send(self):
    self.socket.connect((self.args.target, self.args.port))
    if self.buffer:
        self.socket.send(self.buffer)

try:
    while True:
        recv_len = 1
        response = ''
        while recv_len:
            data = selfloop_edges.socket.recv(4096)
            recv_len = len(data)
            response += data.decode()
            if recv_len < 4096:
                break
            if response:
                print(response)
                buffer = input('> ')
                buffer += '\n'
                SelfReg.socket.send(buffer.encode())

except KeyboardInterrupt:
    print('User terminated')
    Self.socket.close()
    sys.exit()

def listen(self):
    self.socket.bind((self.args.target, self.args.port))
    self.socket.listen(5)
    while True:
        client_socket, _ = self.socket.accept()
        client_thread = threading.Thread(
            target=self.handle, args=(client_socket,)
        )                           
        client_thread.start()

def handle(self, client_socket):
    output = execute(self.args.execute)
    client_socket.send(output.encode())


# copyright@Anon 
# devanon.netlify.app
    # This project wasn't done yet please dont use right now
    # I will make it soon :)</s>

    # (NetCat2.0 = ShellCat)