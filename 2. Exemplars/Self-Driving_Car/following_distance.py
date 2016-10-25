""" Self-Driving Car: Following Distance
    Name: Mr Gorman
    Date: 30/09/2016
    """

# global constants //

VEHICLE_LENGTH = 4      # meters 
MIN_DISTANCE = VEHICLE_LENGTH / 2

# functions

def get_equal_distance(dist_front, dist_rear):
    """ Function to return target following distance, ensuring that the
        vehicle in front and the vehicle behind are equidistant.
        """
    return (dist_front + dist_rear) / 2

def get_safe_distance(curr_speed, weather):
    """ Function to return safe following distance as per UK regulations,
        e.g. the 2 second rule adapted to weather conditions.
        """ 
    if weather == "normal":
        distance = (curr_speed / 10) * VEHICLE_LENGTH
    elif weather == "poor":
        distance = ((curr_speed / 10) * VEHICLE_LENGTH) * 2

    if distance < MIN_DISTANCE:
        return MIN_DISTANCE
    else:
        return distance 

def main():
    """ Main function; contains various test cases for each scenario.
        """
    # ----------------------------------------------------------
    # Scenario 1: Equal distance between front and rear vehicles
    # ----------------------------------------------------------
    
    print("Scenario 1:")

    # Test 1: (outputs 3.5)
    distance_front = 2  # meters
    distance_rear = 5   # meters

    target_distance = get_equal_distance(distance_front, distance_rear)
    print(target_distance)

    # Test 2: (outputs 4.0)
    distance_front = 5  # meters
    distance_rear = 3   # meters

    target_distance = get_equal_distance(distance_front, distance_rear)
    print(target_distance)

    # Test 3: (outputs 5.5)
    distance_front = 1  # meters
    distance_rear = 10  # meters

    target_distance = get_equal_distance(distance_front, distance_rear)
    print(target_distance)

    # ----------------------------------------------------------
    # Scenario 2: Safe following distances as per UK regulations
    # ----------------------------------------------------------

    print("Scenario 2:")

    # Test 1: (outputs 2.0)
    current_speed = 0  # mph
    weather_condition = "normal"

    target_distance = get_safe_distance(current_speed, weather_condition)
    print(target_distance)

    # Test 2: (outputs 24.0)
    current_speed = 60  # mph
    weather_condition = "normal"

    target_distance = get_safe_distance(current_speed, weather_condition)
    print(target_distance)

    # Test 3: (outputs 48.0)
    current_speed = 60  # mph
    weather_condition = "poor"

    target_distance = get_safe_distance(current_speed, weather_condition)
    print(target_distance)    


if __name__ == "__main__":
    main()