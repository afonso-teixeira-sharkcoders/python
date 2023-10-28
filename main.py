from time import sleep

i = 100

while i >= 1:
    print(i)
    sleep(1)
    if i == 1:
        print("fim")
    i = i - 1

