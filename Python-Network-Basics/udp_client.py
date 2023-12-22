import socket

target_host = "142.250.196.78"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"AAABBBCCC",(target_host, target_port))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()


# copyright@Anon 
# devanon.netlify.app
