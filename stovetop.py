from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep
import numpy as np
from collections import deque

sensor = Adafruit_AMG88xx()
sleep(0.1)

# Number of previous max temperature samples to average
NUM_SAMPLES = 4

# Interval between sampling
DELTA_T = 60

# Maximum temperature in celcius
MAX_TEMP = 30

# Number of DELTA_T intervals above max temp before sounding alarm
ABOVE_MAX_CYCLES = 120

above_max_count = 0

# Last n max temperature samples
temp_history = deque(maxlen=NUM_SAMPLES)

while True:
    temp_grid = np.array(sensor.readPixels()).reshape((8, 8))
    temp_history.append(np.amax(temp_grid))

    if np.average(np.array(temp_history)) > MAX_TEMP:
        above_max_count += 1
        if above_max_count > ABOVE_MAX_CYCLES:
            # TODO: Send Email Alert
            pass
    else:
        above_max_count = 0

    sleep(DELTA_T)