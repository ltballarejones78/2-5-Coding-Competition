#cerner_2^5_2019
from datetime import datetime, timedelta
import winsound
import time
while 1:
    duration = 5000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    print 'Drink at Least 4oz Of Water'

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=0)

    while datetime.now() < dt:
        time.sleep(1)
