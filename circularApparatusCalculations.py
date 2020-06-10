# ====================================================================
# CSCC ENGR 1182 Summer 2020
# Energy Lab Part 1
# Circular Arc Apparatus Calculations
# Author: John Choi
# ====================================================================

# ====================================================================
# FUNCTIONS
# ====================================================================
from typing import Any, Union


def calculate_energy_loss_per_travel(adjusted_rolling_friction, ball_weight):
    return adjusted_rolling_friction * ball_weight


def get_adjusted_rolling_friction(rolling_friction, n):
    return rolling_friction / n


def calculate_normalized_centripetal_acceleration(centripetal_acceleration):
    return 1 + (centripetal_acceleration / 9.81)


def calculate_centripetal_acceleration(velocity, radius_of_arc_segment):
    return (velocity ** 2) / radius_of_arc_segment


def calculate_average_rolling_friction(hsp, hrest, distance):
    return (hsp - hrest) / distance


def calculate_average_speed(distance_traveled, time):
    return distance_traveled / time


def get_total_distance_traveled(num_of_cycles, ssp):
    return (4 * num_of_cycles * ssp) / 2.0


def calculate_energy_loss(height_rest, arc_radius, hsp, ssp, cycle, time):
    weight = 0.0951  # unit: N, weight of the ball
    # get distance traveled by the ball
    distance_traveled = get_total_distance_traveled(cycle, ssp)
    print("Distance traveled by the ball: \t\t% .3f" % distance_traveled)
    # get average speed of the ball
    avg_speed = calculate_average_speed(distance_traveled / 1000.0, time)
    print("Average speed of the ball: \t\t% f m/s" % avg_speed)
    # get average rolling friction coefficient
    avg_rolling_friction_coef = calculate_average_rolling_friction(hsp, height_rest, distance_traveled)
    print("Average rolling friction coefficient: \t% f m" % avg_rolling_friction_coef)
    # calculate the centripetal acceleration
    a = calculate_centripetal_acceleration(avg_speed, arc_radius / 1000.0)
    print("Centripetal acceleration: \t\t% f m" % a)
    # calculate normalized centripetal acceleration
    n = calculate_normalized_centripetal_acceleration(a)
    print("Normalized centripetal acceleration: \t% f m/s^2" % n)
    # adjust the rolling friction coefficient for normalized acceleration
    adjusted_rolling_friction = get_adjusted_rolling_friction(avg_rolling_friction_coef, n)
    print("Adjusted rolling friction coefficient: \t% f m" % adjusted_rolling_friction)
    # calculate energy loss per meter of travel
    energy_loss = calculate_energy_loss_per_travel(adjusted_rolling_friction, weight)
    print("Energy loss per meter of travel: \t% f J/m" % energy_loss)
    return energy_loss


def get_average(list):
    avg = 0
    for num in list:
        avg += num

    return avg / len(list)


# ====================================================================
# MAIN
# ====================================================================

# ID 6 values
print("Circular Arc Apparatus ID 6\n")
average_cycles = [32.667, 16.333, 15.333, 19.333, 11.667]
average_times = [46, 42.2867, 39.43, 49.9267, 28]

h_rest = 183  # resting height
arc_radius = 1000  # radius of the arc
starting_height = 287  # starting height
ssp = 460

avg_cycles = get_average(average_cycles)
avg_time = get_average(average_times)
energy_loss_1 = calculate_energy_loss(h_rest, arc_radius, starting_height, ssp, avg_cycles, avg_time)

# ID 4 values
print("\n\nCircular Arc Apparatus ID 4\n")
average_cycles = [14.667, 24.333, 28.667, 22.333, 14.333]
average_times = [27.6367, 30.32, 34.6633, 27.48, 18.3333]

h_rest = 201  # resting height
arc_radius = 250  # radius of the arc
starting_height = 260  # starting height
ssp = 176

avg_cycles = get_average(average_cycles)
avg_time = get_average(average_times)

energy_loss_2 = calculate_energy_loss(h_rest, arc_radius, starting_height, ssp, avg_cycles, avg_time)

avg_energy_loss: Union[float, Any] = (energy_loss_1 + energy_loss_2) / 2.0

print("\n\nAverage Energy Loss: \t\t% f J/m" % avg_energy_loss)
