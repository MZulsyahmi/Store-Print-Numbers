from random import uniform
import time

#store up to 30 numbers
num_store = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    num_random = uniform(0, 100.00)
    num_store.append(float(num_random))
    
    #print latest number
    print("Value: {:.2f}    ".format(num_store[-1]), end='')
    
    #print number 10 sec before
    num_10sec = num_store[-10]
    print("Value 10sec: {:.2f}".format(num_10sec))
    time.sleep(1)   #delay for 1 sec
