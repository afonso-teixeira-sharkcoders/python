from time import sleep

i = 100

while i >= 1:
    print(i)
    sleep(1)
    if i == 1:
        print("End")
    i = i - 1

