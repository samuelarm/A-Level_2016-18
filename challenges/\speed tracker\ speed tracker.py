import time
import random
def speed_calculation (time_one, time_two, distance):
    """ this is a function to work out the speed
        that a car is traveling between two points
        """
    difference = time_two - time_one 
    average_speed = (distance/difference)
    return average_speed

#testing 
distance = 1

time_one = time.time()
time_two = time_one + random.randint(20,40) 


miles_per_second = speed_calculation(time_one, time_two, distance)
miles_per_hour = miles_per_second * 60 * 60
miles_per_hour = round(miles_per_hour,2)
print ("the car is traviling at",miles_per_hour,"mph")
