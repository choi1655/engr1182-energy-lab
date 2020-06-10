# ====================================================================
# CSCC ENGR 1182 Summer 2020
# Energy Lab Part 1
# Linear Apparatus Calculations
# Author: John Choi
# ====================================================================
import math

# ====================================================================
# GLOBAL
# ====================================================================
LENGTH = 1080  # unit: mm, length of hypotenuse
BALL_RADIUS = 0.01272  # unit m, geometric radius of the ball
ROLLING_RADIUS = 0.01018  # unit m, effective rolling radius of the ball on the track

# ====================================================================
# FUNCTIONS
# ====================================================================


def calculate_incline_angle(h1):
    # get degree
    inner = h1 / 1080
    print(inner)
    degree_radian = math.asin(inner)
    print("ß: \t% f rad" % degree_radian)
    # calculate static friction coefficient
    static_friction_coef = math.tan(degree_radian)
    inner = 1 + (5.0 / 2) * ((ROLLING_RADIUS / BALL_RADIUS) ** 2)
    inner *= static_friction_coef
    angle = math.atan(inner)
    # convert to degrees
    angle *= (180 / math.pi)
    print("Angle in degrees: \t% f" % angle)
    return angle


def get_average(num_list):
    avg = 0
    for num in num_list:
        avg += num
    return avg / len(num_list)

# ====================================================================
# MAIN
# ====================================================================


angles = []

# Straddle
print("Straddle\n")
heights = [323.33, 346.67, 300, 383, 383.33]
h1 = get_average(heights)
straddle_incline_angle = calculate_incline_angle(h1)
angles.append(straddle_incline_angle)

# Right
print("\nRight\n")
heights = [350, 333.33, 350, 421.33, 360]
h1 = get_average(heights)
right_incline_angle = calculate_incline_angle(h1)
angles.append(right_incline_angle)

# Left
print("\nLeft\n")
heights = [343.33, 316.67, 293.33, 409, 363.33]
h1 = get_average(heights)
left_incline_angle = calculate_incline_angle(h1)
angles.append(left_incline_angle)

# Calculate average of incline angles
avg_angle = get_average(angles)
print("\n\nThe average incline angle is % f" % avg_angle)
