import time
from motor import init,forward,reverse,stop
import RPi.GPIO as gpio


def right(tf):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()
    forward(0.025)

def funcclk(times,time):

        for x in range(1,times):#how many times rotate per day
            right(time)#here, set time to control the rotation time(angle)
            time.sleep(86400/times)#time interval between each rotation

def funcsensor(t,hu,p,counter,max_num,move_time,stabilizer):
    # bool to ensure only one time mvement each time we run this function
    unmove = True
    if t > 35 and counter <max_num and unmove:
        reverse(move_time)  # set move_time manually here to control the time of operation
        counter=counter+1
        unmove =False
    elif hu > 80 and counter <max_num and stabilizer and unmove:
        reverse(move_time) # set x move_time manually here to control the time of operation
        counter = counter + 1
        stabilizer = False
        unmove = False

    elif hu > 140 and counter <max_num and unmove: # humidity toward dangerous level,backward without waiting
        reverse(move_time) # set x move_time manually here to control the time of operation
        counter = counter + 1
        stabilizer = False
        unmove = False
    elif p > 1005.7 and counter <max_num and unmove:
        reverse(move_time) # set move_time manually here to control the time of operation
        counter = counter + 1
        unmove = False
    else:
        pass
    return stabilizer, counter


def funcreturn(counter,move_time):
    if counter!=0 :
        forward(move_time)#here move_timeshould be the same value with the previous function,前面退了几次这里一次性前进回去
        pointer=0
        counter = counter -1
    else:
        pass
    return counter















