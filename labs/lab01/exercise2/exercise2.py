# Lab 01 Exercise 2: Camping Logistics
import math
def calculate_tent_cost(participants,tent_capacity,tent_price):
    total_tents = participants / tent_capacity
    cost = math.ceil(total_tents) * tent_price
    return cost