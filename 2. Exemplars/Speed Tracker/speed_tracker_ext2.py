""" Speed Tracker (Extension 2)
    Name: Mr Gorman
    Date: 24/03/2017
    """

import re
import random
from datetime import datetime, timedelta

SPEED_LIMIT = 70 # mph

def save_data(filename, data_list):
    """ Procedure to save a list of data to a file.
        """
    try:
        with open(filename, "w") as file:
            for data in data_list:
                file.write(str(data))
        print("Data saved to file \"%s\"" % filename)
    except:
        print("ERROR: Data not saved to file")

def load_data(filename):
    """ Function to load data from a file and return
        each line as a list item.
        """
    try:
        with open(filename, "r") as file:
            data_list = file.readlines()
        print("Data loaded from file \"%s\"" % filename)
        return data_list
    except FileNotFoundError:
        print("ERROR: \"%s\" not found" % filename)
    except:
        print("ERROR: Data not loaded from file")

def calculate_average_speed(timestring_in, timestring_out, distance=1):
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

def validate_number_plate(number_plate_string):
    """ Function to test whether a number plate matches a
        valid pattern (2 letters, 2 numbers, space, 3 letters).
        Returns True or False.
        """
    valid_pattern = re.match(r"\w{2}\d{2} \w{3}", number_plate_string)
    if valid_pattern != None:
        return True
    else:
        return False

def generate_random_data():
    """ Function to generate and return a list of random time 
        and number plate data.
        
        Constraints:
          - Time data must be chronological and allow for speeds
            between 20 and 180 mph (i.e. durations between 180 and 
            20 seconds). Must return 2 datetime objects.
          - Number plate data must be between 1 and 8 characters.
        """
    data_list = []

    # generate random time data

    # generate random number plate data

    return data_list

def process_data_log(data_list):
    """ Function to process speed tracking data list and return
        a list of offending vehicles (i.e. those exceeding the  
        speed limit of 70 mph or with an invalid number plate).
        """
    offence_log = []

    for record in data_list:
        attributes = record.replace("\n", "").split(sep=",")
        average_speed = calculate_average_speed(attributes[0], attributes[1])
        valid_number_plate = validate_number_plate(attributes[2])
        
        add_to_log = False
        log = attributes[0] + ", " + attributes[1] + ", " + attributes[2]
        
        if average_speed > SPEED_LIMIT:
            add_to_log = True
            log += ", Exceeded speed limit by " + str(average_speed - SPEED_LIMIT)
        if not valid_number_plate:
            add_to_log = True
            log += ", Invalid number plate"
        
        if add_to_log:
            offence_log.append(log)
    
    return offence_log
        

def main():
    """ Main program
        """
    # random_data = generate_random_data()
    # save_data("2. Exemplars/Speed Tracker/random_data.txt", random_data)

    data_log = load_data("2. Exemplars/Speed Tracker/random_data.txt")
    for record in data_log:
        print(record)

    processed_data_log = process_data_log(data_log)
    for record in processed_data_log:
        print(record)

    # save_data("2. Exemplars/Speed Tracker/speed_tracker.log", processed_data_log)


if __name__ == "__main__":
    main()
