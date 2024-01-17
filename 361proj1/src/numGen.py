# Author: Robin Shindelman
# Date: 2023-01-11
# Description: This is a microservice designed to psuedo-randomly generate a
# single positive integer to send back to the UI via prng_service.txt

from random import randint
from time import sleep


pipe = '/Users/robinshindelman/repos/school/361.SE1/361proj1/src/prng_service.txt'
exiter = True

while exiter:
    sleep(1)
    # Read mode
    with open(pipe, 'r') as comm:
        line1 = comm.readline()
        # If communication received:
        if line1 == 'run':
            comm.close()
            comm = open(pipe, 'w')
            num = randint(0, 499)
            comm.write(str(num))
            comm.close()
        # Quit the app:
        if line1 == 'quit':
            exiter = False
