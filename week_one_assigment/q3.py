import math as m


def get_distance_time(distance):
    # Gets time in hours
    return distance / 740


def calculate_distance(lat1, long1, lat2, long2):
    return 6371.01 * m.acos((m.sin(m.radians(lat1)) * m.sin(m.radians(lat2))) +
                            (m.cos(m.radians(lat1)) * m.cos(m.radians(lat2)) * m.cos(m.radians(long1) - m.radians(long2))))


def get_coordinates():
    while True:
        try:
            lat1 = float(input("Position 1 latitude: "))
            long1 = float(input("Position 1 longitude: "))
            lat2 = float(input("Position 2 latitude: "))
            long2 = float(input("Position 2 longitude: "))
            distance = round(calculate_distance(lat1, long1, lat2, long2), 3)
            time_in_hours = get_distance_time(distance)
            print(
                f"It would take you about: {round(time_in_hours, 2)} hours to travel the distance: {distance} km in a speed of: 740 km/h ")
            print(distance)
        except ValueError:
            print("Not valid, go again: ")


get_coordinates()
