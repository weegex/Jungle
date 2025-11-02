import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (r"127.0.0.1", 8000)
client.connect(server_address)
