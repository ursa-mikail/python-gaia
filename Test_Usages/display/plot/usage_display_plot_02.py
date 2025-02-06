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

    number_of_data_points, upperBound, lowerBound = 100, 17, 5
    x_data = data_generator_object.generate_random_integers(number_of_data_points, upperBound, lowerBound)
    y_data = data_generator_object.generate_random_integers(number_of_data_points, upperBound, lowerBound)

    grid_option = True

    markings = ['ko-', 'r.-', 'bx-', 'g+', 'g^', 'cs', 'm*']
    titles = []
    title = 'Random Data'
    title_main = title
    description_x_label, description_y_label = 'x_axis', 'y_axis'
    plot_marker_style = markings[0]

    annotations = list(range(0, number_of_data_points))
    # annotations = None

    # display_plot_object.display_graph(title_main, title, x_data, y_data, description_x_label, description_y_label, plot_marker_style, grid_option, annotations)

    colors = ['green', 'yellow', 'brown', 'orange', 'violet', 'indigo', 'purple', 'magenta', 'cyan', 'black', 'white',
              'blue']

    color_sets = []
    for i in range(len(colors)):
        color_sets.append(colors[i])

    scale = x_data
    print("scale: ", scale)
    display_plot_object.display_scatter_plot(title_main, title, x_data, y_data, description_x_label, description_y_label, scale, color_sets, grid_option, annotations)

    print("=====[" + id_display_plot + " End]===== \n");
    print("=====[" + id_data_generator + " End]===== \n");

"""
# version: 2018-01-27_2100hr_01sec
"""