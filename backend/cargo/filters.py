def filter_by_distance(queryset, distance, weight):
    cargoes_fitred_by_weight = [
        cargo for cargo in queryset
        if cargo.weight == int(weight)
    ]
    cargoes_fltred_by_weight_and_distance = []
    for cargo in cargoes_fitred_by_weight:

        fitred_trucks_by_distance = [
            truck for truck in cargo.trucks_with_distance
            if truck['distance'] <= int(distance)
        ]
        cargo.nearest_trucks = len(fitred_trucks_by_distance)
        cargoes_fltred_by_weight_and_distance.append(cargo)

    return cargoes_fltred_by_weight_and_distance

