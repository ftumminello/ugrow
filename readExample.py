import time

while 1:
    with open("out.log", "r") as f:
        content = f.read()
        print(content)
    sleep(5) # suspend execution for 5 seconds