# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient(one_way_km,budget):
    fuel_total = (one_way_km * 2) / 10
    fuel_cost = fuel_total * 2
    if fuel_cost > budget:
        return False
    else:
        return True