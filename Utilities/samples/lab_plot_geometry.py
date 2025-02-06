import matplotlib.pyplot as plt
import numpy as np
import math

def plot_point(point_start, angle_in_degrees, length_of_line):
    '''
    point - Tuple (x, y)
    angle - Angle you want your end point at in degrees.
    length - Length of the line you want to plot.

    Will plot the line on a 10 x 10 plot.
    '''
    x, y = point_start # unpack the first point

    print(x, y)

    # find the end point
    endy = length_of_line * math.sin(math.radians(angle_in_degrees))
    endx = length_of_line * math.cos(math.radians(angle_in_degrees))

    # plot the points
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.set_ylim([-70, 70])  # set the bounds to be 10, 10
    ax.set_xlim([-70, 70])
    ax.plot([x, endx], [y, endy])

    ax.grid(True)
    plt.show()

def switch_diagram_draw(argument):
    switcher = {
        'leave_1': leave_1, # "leave_1",
        'leave_2': leave_2,
        'leave_3': leave_3,
        'leave_4': leave_4,
        'leave_6': leave_6,
        'spiral_anti_clock_wise_2nd_quadrant': spiral_anti_clock_wise_2nd_quadrant,
        'spiral_anti_clock_wise_1st_quadrant': spiral_anti_clock_wise_1st_quadrant,
        'cardioid': cardioid,
        'circle': circle,
        'line': line,
        'line_perpendular_to_origin': line_perpendular_to_origin,
        #6: "June",

    }
    print (switcher.get(argument, "Invalid option"))
    # Get the function from switcher dictionary
    function_chosen = switcher.get(argument, lambda: "Invalid month")
    r, theta = function_chosen() # run function

    return function_chosen, r, theta

def leave_1():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    a = 1  # np.arange(0, 2, bin)
    r = a*np.cos(3*theta)
    return r, theta

def leave_2():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    a = 1  # np.arange(0, 2, bin)
    r = a * np.sin(2 * theta)
    return r, theta

def leave_3():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    a = 1  # np.arange(0, 2, bin)
    r = a*np.cos(3*theta)
    return r, theta

def leave_4():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    a = 1  # np.arange(0, 2, bin)
    r = a*np.cos(2*theta)
    r0 = [0] * len(r)

    for i in range(0, len(r)):
        r0[i] = math.sqrt(math.fabs(r[i]))
    return r0, theta

def leave_6():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    a = 1  # np.arange(0, 2, bin)
    r = a*np.cos(3*theta)
    r0 = [0] * len(r)

    for i in range(0, len(r)):
        r0[i] = math.sqrt(math.fabs(r[i]))
    return r0, theta


def spiral_anti_clock_wise_2nd_quadrant():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    k = -0.5 # > 0, < 0
    r = k*theta
    return r, theta

def spiral_anti_clock_wise_1st_quadrant():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    k = 0.2 # > 0, < 0
    r = k*theta
    return r, theta

def cardioid():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    a, b = -0.4, 0.8 # a >, =, <
    r = a + (b * np.cos(theta))
    return r, theta

def circle():
    bin = 0.01
    x = np.arange(0, 2, bin)
    theta = 2 * np.pi * x
    a = 0.8
    r = (a * np.cos(theta))
    # r = [a]*len(theta)
    return r, theta

def line():
    bin = 0.01
    r = np.arange(0, 2, bin)
    angle_in_degrees = 60
    theta = [math.radians(angle_in_degrees)] * len(r)
    return r, theta

def line_perpendular_to_origin():
    bin = 0.01
    x = np.arange(0, 2, bin)
    r = np.arange(0, 2, bin)
    dist_of_perpendular_to_line_from_origin = 0.5
    angle_of_dist_of_perpendular_to_line_from_origin = 15
    theta_angle_of_dist_of_perpendular_to_line_from_origin = [math.radians(angle_of_dist_of_perpendular_to_line_from_origin)] * len(x)

    theta = 2 * np.pi * x
    theta = [2 * np.pi * math.radians(50)] * len(x)
    theta_deltas, degree_deltas, degrees = [0]* len(x), [0]* len(x), [0]* len(x)

    for i in range(0, len(x)):
        #theta_deltas[i] = 1/math.cos(theta[i] - theta_angle_of_dist_of_perpendular_to_line_from_origin[i])
        degrees[i] = math.degrees(theta[i])
        degree_deltas[i] = degrees[i] - angle_of_dist_of_perpendular_to_line_from_origin
        theta_deltas[i] = 1 / math.cos(math.radians(degree_deltas[i]))

        r[i] = r[i] * theta_deltas[i]

    print(theta_deltas)
    return r, theta_deltas

#x = np.arange(0, 2 * (np.pi), 0.1)  # setting the x - coordinates
#y = np.sin(x)   # setting the corresponding y - coordinates
#plt.plot(x, y)  # plotting the points

#a = np.arange(0, 2 * (np.pi), 0.1)
#theta = np.linspace(0, math.pi/6, len(a))
#r = a*np.cos(3*theta)

#plt.plot(x, r)
"""
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
"""

options = ['leave_1', 'leave_2', 'leave_3', 'leave_4', 'leave_6',
           'spiral_anti_clock_wise_2nd_quadrant', 'spiral_anti_clock_wise_1st_quadrant', 'cardioid', 'circle', 'line',
           'line_perpendular_to_origin']
choice = options[5]
function_chosen, r, theta = switch_diagram_draw(choice)


ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)

#ax.plot(theta1, r1)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
"""

x1, y1 = 10, -50
x1, y1 = 0, 0
angle_in_degrees, length_of_line = 30, 20
#angle_in_radians = math.tan(math.radians(angle_in_degrees))

point_start = [x1, y1]
# plot_point(point_start, angle_in_degrees, length_of_line)

bin = 0.01
x = np.arange(0, math.pi * 0.5, bin)
x_in_degrees = [0]*len(x)

for i in range(0, len(x)):
    x_in_degrees[i] = math.degrees(x[i])

print('x: ', x_in_degrees)
print('x_len: ', len(x_in_degrees))

dist_of_perpendular_to_line_from_origin = 3.25
angle_of_dist_of_perpendular_to_line_from_origin = 15
theta_angle_of_dist_of_perpendular_to_line_from_origin = math.radians(angle_of_dist_of_perpendular_to_line_from_origin)


degrees, thetas_in_radians, x_in_radians, r = [0]* len(x), [0]* len(x), [0]* len(x), [1]* len(x)
x, y = [0]* len(x), [0]* len(x)

for i in range(0, len(x)):
    thetas_in_radians[i] = 1 / math.cos(math.radians(x_in_degrees[i] - angle_of_dist_of_perpendular_to_line_from_origin))
    x_in_radians[i] = math.radians(x_in_degrees[i])

    r[i] = r[i] * dist_of_perpendular_to_line_from_origin * thetas_in_radians[i]

    x[i] = r[i] * math.cos(thetas_in_radians[i])
    y[i] = r[i] * math.sin(thetas_in_radians[i])

print(x)
print(y)

plt.figure()
ax = plt.subplot(111)
ax.set_ylim([-2, 10])  # set the bounds to be 10, 10
ax.set_xlim([-2, 10])

ax.grid(True)
plt.plot(x, y, 'x')
plt.show()

angle_in_degrees = 50
angle_in_radians = math.radians(angle_in_degrees)
answer = 1 / math.cos(angle_in_radians)
print("answer: ", answer)
"""


"""
sl = math.tan(math.radians(angle))
x = np.array(range(-10,10))
y = sl*(x-x1) + y1

plt.plot(x,y)
plt.show()
"""


"""
class Switcher(object):
    def numbers_to_months(self, argument):
        # Dispatch method
        method_name = 'month_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()
 
    def month_1(self):
        return "January"
"""