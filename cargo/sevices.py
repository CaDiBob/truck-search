from geopy import distance


def get_distance_from_truck_to_load(truck, cargo):
    truck_coordinates = (truck.location.lat, truck.location.lon)
    cargo_coordinates = (cargo.pickup_location.lat, cargo.pickup_location.lon)
    distance_to_load = round(distance.distance(
        truck_coordinates, cargo_coordinates).miles, 3)
    return distance_to_load
