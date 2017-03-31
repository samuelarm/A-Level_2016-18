import time
import random
def speed_calculation (time_one, time_two, distance):
    """ this is a function to work out the speed
        that a car is traveling between two points
        """
    difference = time_two - time_one 
    average_speed = (distance/difference)
    return average_speed

def speeding_message(miles_per_hour, speed_limit):
    """ this is a function to work out if the car
        is speeding the prints a message to notify
        the user
        """
    if miles_per_hour > speed_limit:
        print("This car was going over the speed limit")
    elif miles_per_hour == speed_limit:
        print("This car is travelling at the speed limit")
    else:
        print ("This car going under the speed limit")
        

def number_plate_validation (number_plate):
    """ this is a function to work out if the
        the number plate is corrrect doesn't
        work
        """
    letter_one = test[:2]
    number_one = test[2:4]
    letter_two = test[5:]
    if all ((letter_one.isalpha(), number_one.isdigit(), letter_two.isalpha())):
        print("The number plate is valid")
    else:
        print ("The number plate is invalid")



#testing
#variable list
distance = 1
time_one = time.time()
time_two = time_one + random.randint(50,100)
speed_limit = 60
test = ("xx22 xxx")
# testing over

miles_per_second = speed_calculation(time_one, time_two, distance)
miles_per_hour = miles_per_second * 60 * 60
miles_per_hour = round(miles_per_hour,2)
print ("The car is traviling at",miles_per_hour,"mph")
speed_message = speeding_message(miles_per_hour, speed_limit)
number_plate_test = number_plate_validation(test)
