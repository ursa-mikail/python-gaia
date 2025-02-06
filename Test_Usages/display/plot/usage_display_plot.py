####################################
import os, sys

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
    title = 'Random Data'
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
    # display_plot_object.display_pie_chart(title_main, title, labels, percentages, explode_options)


    number_of_graphs = 7
    grid_options = [True, False, True, False, True, False, True]
    x_axis_data_sets = []
    y_axis_data_sets = []
    plot_marker_styles = []
    subplot_choices = ['ROW_WISE', 'COLUMN_WISE']
    row_or_column_wise_option = subplot_choices[1]
    description_x_labels = []
    description_y_labels = []
    title_main = title

    for i in range(0, number_of_graphs):
        x_axis_data_sets.append(data_generator_object.generate_random_integers(number_of_data_points, upperBound, lowerBound))
        y_axis_data_sets.append(data_generator_object.generate_random_integers(number_of_data_points, upperBound, lowerBound))
        plot_marker_styles.append(markings[i])
        description_x_labels.append(description_x_label)
        description_y_labels.append(description_y_label)
        titles.append(title)

    color_sets = [colors[0], colors[1], colors[2]]
    scale = x_axis_data_sets[3]
    print("scale: ", scale)

    annotations = None
    annotations = list(range(0, number_of_data_points - 100))
    display_plot_object.display_scatter_plot(title_main, title, x_axis_data_sets, y_axis_data_sets, description_x_label, description_x_label, scale, color_sets, grid_option, annotations)

    display_plot_object.display_graph_row_or_column_wise(title_main, titles, x_axis_data_sets, y_axis_data_sets,
                                     description_x_labels, description_y_labels, plot_marker_styles,
                                     row_or_column_wise_option, grid_options)
    
    display_plot_object.display_graph_evenly(title_main, titles, x_axis_data_sets, y_axis_data_sets,
                                     description_x_labels, description_y_labels, plot_marker_styles, grid_options)



    print("=====[" + id_display_plot + " End]===== \n");
    print("=====[" + id_data_generator + " End]===== \n");

"""
# version: 2017-11-10_2155hr_04sec
"""