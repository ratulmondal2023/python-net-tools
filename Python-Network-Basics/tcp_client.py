import socket

target_host = "www.devanon.netlify.app"
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send(b"GET /HTTP/1.1\r\nHost: devanon.netlify.app\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()


# copyright@Anon 
# devanon.netlify.app
