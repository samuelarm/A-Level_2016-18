""" Speed Tracker (Extension 1)
    Name: Mr Gorman
    Date: 24/03/2017
    """

import re
from datetime import datetime, timedelta

def average_speed(timestring_in, timestring_out, distance=1):
    """ Function to return the average speed in mph of a vehicle 
        travelling between 2 speed cameras placed 1 mile apart.
        
        Expected timestring format = "HH:MM:SS"
        """
    try:
        time_format = "%H:%M:%S"
        time_in = datetime.strptime(timestring_in, time_format)     # convert string to datetime object (HH:MM:SS)
        time_out = datetime.strptime(timestring_out, time_format)   # convert string to datetime object (HH:MM:SS)
        duration = (time_out - time_in).seconds                     # timedelta object represented in seconds
        return round((distance / duration) * 60 * 60, 2)            # speed in mph, rounded to 2 decimal places
    except ZeroDivisionError:
        print("ERROR: timestring_in cannot equal timestring_out")
        return 0
    except:
        print("ERROR: Cannot calculate average speed. Check your data!")
        return 0

def valid_number_plate(number_plate_string):
    """ Function to test whether a number plate matches a
        valid pattern (2 letters, 2 numbers, space, 3 letters).
        Returns True or False.
        """
    valid_pattern = re.match(r"\w{2}\d{2} \w{3}", number_plate_string)
    if valid_pattern != None:
        return True
    else:
        return False

# test
print(average_speed("15:00:00", "15:01:00"), "mph")
print(valid_number_plate("ET25 HME"))
print(valid_number_plate("2COO L4U"))