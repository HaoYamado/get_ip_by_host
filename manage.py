
import socket
import sys

hostname = sys.argv[1] # argv[1] - для аргументов в терминале ОС

ip = socket.gethostbyname(hostname) # Наименование хоста
print('Сайт:', hostname, '\n' 'IP:', ip)