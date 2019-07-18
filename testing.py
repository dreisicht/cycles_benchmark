import datetime
import time

global last_time
last_time = datetime.datetime.now()

def delta_timer():
    '''Function to get quick delta timing'''
    global last_time
    deltat = datetime.datetime.now() - last_time
    last_time = datetime.datetime.now()
    return deltat

print(delta_timer())
time.sleep(1)
print(delta_timer())
