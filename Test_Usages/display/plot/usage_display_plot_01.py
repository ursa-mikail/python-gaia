####################################
import os, sys
import math as math

# point to path
lib_path = os.path.abspath('../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/display/plot')
sys.path.append(lib_path)

# import package from path
from data_generator import data_generator	# file name
from display_plot import display_plot

####################################
## main
####################################
if __name__ == "__main__":
    id_data_generator = "Test Usage Agent: <data_generator>"
    print ("=====[" + id_data_generator + " Start]===== \n")
    data_generator_object = data_generator(id_data_generator)

    id_display_plot = "Test Usage Agent: <display_plot >"
    print("=====[" + id_display_plot  + " Start]===== \n")
    display_plot_object = display_plot (id_display_plot )

    grid_option = True
    number_of_data_points, upperBound, lowerBound = 100, 100, 10
    x_data = data_generator_object.generate_random_integers(number_of_data_points, upperBound, lowerBound)
    y_data = data_generator_object.generate_random_integers(number_of_data_points, upperBound, lowerBound)

    markings = ['ko-', 'r.-', 'bx-', 'g+', 'g^', 'cs', 'm*']
    titles = []
    title = 'bernoulli distribution'
    title_main = title
    description_x_label, description_y_label = 'x_axis', 'y_axis'
    plot_marker_style = markings[0]

    colors = ['green', 'yellow', 'brown', 'orange', 'violet', 'indigo', 'purple', 'magenta', 'cyan', 'black', 'white', 'blue']
    background_color, line_color, linewidth = colors[10], colors[0], 2
    display_plot_object.define_settings (background_color, line_color, linewidth)
    bar_option = ['VERTICAL', 'HORIZONTAL']
    bar_option_chosen = bar_option[0]

    error = [5] * len(x_data)
    # display_plot_object.display_bar_chart (title_main, title, x_data, y_data, error, description_x_label, description_y_label, bar_option_chosen, grid_option)

    # display_plot_object.display_graph(title_main, title, x_data, y_data, description_x_label, description_y_label, plot_marker_style, grid_option)
    labels = 'Pneuma', 'Soma', 'Psyche', 'Opus'
    percentages = [15, 30, 45, 10]
    explode_options = (0, 0.1, 0, 0)  # only "explode" the 2nd slice

    grid_options = [True, False, True, False, True, False, True]

    # https://www.codecogs.com/latex/eqneditor.php
    # bernoulli distribution
    # p^x * (1-p)^1-x | x € (0, 1).
    """
    P_x = \left\{\begin{matrix} 
    1-p, & x = 0
    \\ p,  & x = 1
    \end{matrix} \right.
    
    E(X) = 1*p + 0*(1-p) = p
    V(X) = E(X^²) – [E(X)]^² = p – p^² = p(1-p)
    """
    p = 0.15
    q = 1 - p
    x_data = ['success', 'failure']
    y_data = [p, q]
    description_y_label = 'y'
    description_x_label = 'x'
    display_plot_object.display_bar_chart(title_main, title, x_data, y_data, None,  description_x_label, description_y_label,
                                          'VERTICAL', grid_option)

    title = 'uniform distribution'
    # uniform distribution
    # f_x = \frac{1}{b-a} | - \infty < a \leq x \leq b < \infty
    # E(X) = (a+b)/2; V(X) =  (b-a)^²/12
    b = 100
    a = 1
    x_data = range(a, b)
    y_data = [1/(b-a)] * (b-a)

    display_plot_object.display_bar_chart(title_main, title, x_data, y_data, None, description_x_label,
                                          description_y_label,
                                          'VERTICAL', grid_option)

    # binomial distribution
    # P_x = \frac{n!}{(n-x)!x!}p^xq^{n-x}
    # µ = n*p; Var(X) = n*p*q
    title = 'binomial distribution'
    # p = 0.5; q = 0.5
    n = 100 # trials
    x_data = range(0, n)
    y_data = []

    for i in range(0, len(x_data)):
        y_data.append(math.factorial(n)/(math.factorial(n - x_data[i]) * math.factorial(x_data[i]) * p**x_data[i] * q**(n - x_data[i])))

    display_plot_object.display_bar_chart(title_main, title, x_data, y_data, None, description_x_label,
                                          description_y_label,
                                          'VERTICAL', grid_option)

    # normal distribution
    # f_x = \frac{1}{\sqrt {2 \pi} \sigma } e^{-\frac{1}{2}(\frac{x-\mu }{\sigma})^2} | - \infty < x < \infty
    # E(X) = µ ; Var(X) = σ^2
    title = 'normal distribution'
    exponent = 0
    sigma = math.sqrt(0.7) # math.sqrt(1.5)
    mu = 1.5 # 0.4
    import numpy as np

    bin = 0.5 # 1.0
    x_data = np.arange(-30, 30, bin) # range(-30, 30)
    y_data = []

    for i in range(0, len(x_data)):
        exponent = math.exp(-(1/2) * ((x_data[i] - mu)/sigma)**2)
        y_data.append((1/(math.sqrt(2 * math.pi))*sigma) * exponent )

    # print(len(y_data), "", len(x_data))
    display_plot_object.display_bar_chart(title_main, title, x_data, y_data, None, description_x_label,
                                          description_y_label,
                                          'VERTICAL', grid_option)

    # poisson distribution
    # P_x = \frac{\mu^x}{x! } e^{\mu} | x = 0 ....
    # µ = lambda*t | t = time_interval ; E(X) = µ ; Var(X) = µ
    title = 'poisson distribution'
    bin = 1
    x_data = np.arange(0, 20, bin)  # number of events in that time interval.
    lambda_0 = 5 # rate at which an event occurs
    t = 5
    mu = lambda_0 *t
    y_data = []

    for i in range(0, len(x_data)):
        exponent = math.exp(- mu)
        y_data.append( (mu ** (x_data[i])) /math.factorial(x_data[i]) * exponent)


    cumulative_probability = 0
    number_of_incidents = 6
    mu = 1.5*4
    for i in range(0, number_of_incidents):
        exponent = math.exp(- mu)
        cumulative_probability = cumulative_probability + ( (mu ** (x_data[i])) /math.factorial(x_data[i]) * exponent)

    print("cumulative_probability: ", cumulative_probability)

    display_plot_object.display_bar_chart(title_main, title, x_data, y_data, None, description_x_label,
                                          description_y_label,
                                          'VERTICAL', grid_option)

    # exponential distribution, e.g. Length of time between 2 events, life-time of an organism, etc
    # f_x = \lambda e^{- \lambda  x} | x >= 0
    # lambda is called the failure rate of a device at any time t
    # E(X) = 1/λ; Var(X) = (1/λ)²
    """
    P{X≤x} = 1 – e^-λx, corresponds to the area under the density curve to the left of x.
    P{X>x} = e^-λx, corresponds to the area under the density curve to the right of x.
    P{x1<X≤ x2} = e^-λ_x1 – e^-λ_x2, corresponds to the area under the density curve between x1 and x2.
    """
    title = 'exponential distribution'
    lambda_0 = 0.25
    bin = 0.5
    x_data = np.arange(0, 12, bin)  #
    y_data = []

    for i in range(0, len(x_data)):
        exponent = math.exp(- lambda_0 * x_data[i])
        y_data.append( lambda_0 * exponent)

    display_plot_object.display_bar_chart(title_main, title, x_data, y_data, None, description_x_label,
                                          description_y_label,
                                          'VERTICAL', grid_option)

    print("=====[" + id_display_plot + " End]===== \n");
    print("=====[" + id_data_generator + " End]===== \n");

"""
# version: 2017-11-10_2155hr_04sec
"""