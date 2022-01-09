#
# CPU Percent Test
#
# Connor Lindsay
#

import psutil
import time
import numpy as np

interval = 0.1 # seconds
duration = 60  # seconds

dataNum = int(duration/interval)
data = np.zeros((dataNum,), dtype=float)
index = 0

Tf = time.perf_counter() + duration
Tint = time.perf_counter() + interval
while True:
    t = time.perf_counter() 
    if t > Tint:
        data[index] = psutil.cpu_percent()
        Tint += interval
        index += 1
        if index >= dataNum:
            break

    if t > Tf:
        break
    
print(data)
