import string
import time

def test(file):
    file.seek(0,2)
    y = 1
    while y > 0:
        x = file.readline()
        if not x:
            time.sleep(0.1)
            continue
        yield x

#ip you do not want to log
ip = ''

file1 = open("nginx/access.log","r")
file2 = open("log.txt","w")
while True:

	for line in test(file1):

                line1 = line.split(" ")

                result = ''.join([i for i in line1[0] if i.isdigit() ])
                if result != ip:
                        file2.write(line)

