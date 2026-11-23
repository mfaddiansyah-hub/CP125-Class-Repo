# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
        return (2)
    elif vehicle_type == "Hybrid":
        if (hour >= 22 or hour <= 6):
            return (2)
        else:
            return (5)
    else:
        return (5)