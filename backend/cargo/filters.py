def filter_by_distance(queryset, distance):
    cargoes = []
    for cargo in queryset:
        fitred_trucks_by_distance = [
            truck for truck in cargo.trucks_with_distance
            if truck['distance'] <= int(distance)
        ]
        cargo.nearest_trucks = len(fitred_trucks_by_distance)
        cargoes.append(cargo)

    return cargoes
