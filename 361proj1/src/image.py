# Author: Robin Shindelman
# Date: 2023-01-11
# Description: This program communicates with the UI. It waits for a number to
# to be sent to it from the number generator, then retrieves the image path at
# that index and writes it back to UI. 

import os
from time import sleep


image_dir = '/Users/robinshindelman/repos/school/361.SE1/361proj1/images'
image_paths = [os.path.join(image_dir, image) for image in os.listdir(image_dir)]
pipe = '/Users/robinshindelman/repos/school/361.SE1/361proj1/src/img_service.txt'
poss_nums = [str(num) for num in range(0, 500)]

exiter = True
while exiter:
    sleep(1)
    # Receiving:
    with open(pipe, 'r') as comm:
        line1 = comm.readline()
        if line1 in poss_nums:
            return_path = image_paths[int(line1)]
            comm.close()
            comm = open(pipe, 'w')
            comm.write(return_path)
            comm.close()
        # Exit program
        if line1 == 'quit':
            exiter = False
