import time
from motor import init,forward,reverse,stop,water,motor_right
import RPi.GPIO as gpio


def right(tf):
    motor_right(tf)
    pass



def angle_fix(current_rotate_position,rotate_time):
    while current_rotate_position !=0:
        right(rotate_time)
        current_rotate_position = current_rotate_position+1
        if current_rotate_position ==4:
            current_rotate_position = 0

def func_sensor(t,hu,p,counter,max_num,move_time,stabilizer,current_rotate_position,rotate_time,temp_threshold,pressure_threshold,humid_threshold):



    # bool to ensure only one time mvement each time we run this function
    unmove = True
    if t > temp_threshold and counter <max_num and unmove:
        angle_fix(current_rotate_position,rotate_time)
        reverse(move_time)  # set move_time manually here to control the time of operation
        counter=counter+1
        unmove =False
    elif hu > humid_threshold and counter <max_num and stabilizer and unmove:
        angle_fix(current_rotate_position, rotate_time)
        reverse(move_time) # set x move_time manually here to control the time of operation
        counter = counter + 1
        stabilizer = False
        unmove = False

    elif hu > 140 and counter <max_num and unmove: # humidity toward dangerous level,backward without waiting
        angle_fix(current_rotate_position, rotate_time)
        reverse(move_time) # set x move_time manually here to control the time of operation
        counter = counter + 1
        stabilizer = False
        unmove = False
    elif p > pressure_threshold and counter <max_num and unmove:
        angle_fix(current_rotate_position, rotate_time)
        reverse(move_time) # set move_time manually here to control the time of operation
        counter = counter + 1
        unmove = False
    else:
        pass
    return stabilizer, counter,current_rotate_position


def func_return(counter,move_time,current_rotate_position,rotate_time):

    while current_rotate_position !=0:
        right(rotate_time)
        current_rotate_position = current_rotate_position+1
        if current_rotate_position ==4:
            current_rotate_position = 0


    if counter!=0 :
        forward(move_time)#here move_timeshould be the same value with the previous function,前面退了几次这里一次性前进回去
        pointer=0
        counter = counter -1
    else:
        pass
    return counter,current_rotate_position


def addwater(water_time):
    water(water_time)















