import numpy as np


def test_01 (data_generator_object, display_plot_object, lib_statistics_object):
    mu, sigma = 0, 1  # mean and standard deviation
    number_of_points = 50
    data_points = data_generator_object.generate_data_given_mean_and_variance(mu, sigma, number_of_points)
    print(data_points)
    x_data = list(range(number_of_points))
    y_data = data_points

    grid_option = True
    markings = ['ko-', 'r.-', 'bx-', 'g+', 'g^', 'cs', 'm*']
    titles = []
    title = 'Random Data'
    title_main = title
    description_x_label, description_y_label = 'x_axis', 'y_axis'
    plot_marker_style = markings[0]

    colors = ['green', 'yellow', 'brown', 'orange', 'violet', 'indigo', 'purple', 'magenta', 'cyan', 'black', 'white',
              'blue']
    background_color, line_color, linewidth = colors[10], colors[0], 2
    display_plot_object.define_settings(background_color, line_color, linewidth)

    number_of_points = 1000
    x_data_00 = np.random.randn(number_of_points)
    x_data_01 = np.random.randn(number_of_points)
    x_data_02 = np.random.randn(number_of_points)
    x_data_labels = ["x_data_00", "x_data_01", "x_data_02"]
    x_data = [x_data_00, x_data_01, x_data_02]
    title_main, title = "Histogram", "PDF"
    # display_plot_object.display_graph(title_main, title, x_data, y_data, description_x_label, description_y_label, plot_marker_style, grid_option)
    frequencies, bins = display_plot_object.display_histogram (title_main, title, x_data, x_data_labels, description_x_label, grid_option)
    print(frequencies)
    print(bins)

    x_data = np.random.randn(number_of_points)
    frequencies, bins = lib_statistics_object.compute_histogram(x_data)
    print(frequencies)
    print(bins)
    title_main, title = "Cumulative Distribution Graph", "CDF"
    cumulative_data = lib_statistics_object.compute_CDF(x_data)
    display_plot_object.display_graph (title_main, title, list(range(len(x_data))), cumulative_data, description_x_label, description_y_label, plot_marker_style, grid_option)
    print(cumulative_data[0], cumulative_data[5], cumulative_data[50], cumulative_data[100], cumulative_data[500])

    return None