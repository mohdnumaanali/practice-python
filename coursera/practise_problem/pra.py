# # import re

# # # Open your actual data file
# # handle = open('regex_sum_2347366')

# # total = 0
# # for line in handle:
# #     numbers = re.findall('[0-9]+', line)
# #     for num in numbers:
# #         total += int(num)

# # print(total)


# import re
# data = open("random")
# get = len(data)

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()         