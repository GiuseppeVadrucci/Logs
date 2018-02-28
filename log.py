import string
import time

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

#ip you do not want to log
ip = ''

file1 = open("nginx/access.log","r")
file2 = open("log.txt","w")
while True:

	for line in follow(file1):

                line1 = line.split(" ")

                result = ''.join([i for i in line1[0] if i.isdigit() ])
                if result != ip:
                        file2.write(line)

