####################################
import matplotlib.pyplot as plt
import numpy as np

import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/display/plot')
sys.path.append(lib_path)

# import package from path
from display_plot import display_plot

####################################
## main
####################################
if __name__ == "__main__":
    id_display_plot = "Test Usage Agent: <display_plot >"
    print("=====[" + id_display_plot + " Start]===== \n")
    display_plot_object = display_plot(id_display_plot)

    grid_option = True
    linestyles = ['-', '--', '-.', ':']

    figure_title, graph_title = '===== Observe =====', r'$\sigma_i=15$'

    display_plot_object.set_figure_and_graph_titles(figure_title, graph_title)
    x_label, y_label = 'x data', 'y data'
    display_plot_object.set_x_and_y_axis_labels(x_label, y_label, fontsize=14, color='red')

    position_of_text_in_graph, text = [4, 4], r'$\mu=100,\ \sigma=15$'
    display_plot_object.set_text_in_graph(position_of_text_in_graph, text)

    display_plot_object.draw_horizontal_line(0.5, 'r', linestyles[1])
    display_plot_object.draw_vertical_line(0.22058956, 'blue', linestyles[3])
    display_plot_object.draw_vertical_line(0.33088437)
    display_plot_object.draw_vertical_line(2.20589566)

    display_plot_object.draw_horizontal_line(0, 'black', linestyles[0], linewidth=2)
    display_plot_object.draw_vertical_line(0, 'black', linestyles[0], linewidth=2)

    xs = np.linspace(-np.pi, np.pi, 30)
    ys = np.sin(xs)

    x_coordinate, y_coordinate, mark_style = 0.22058956, 0.5, 'ro'
    display_plot_object.mark_coordinate(x_coordinate, y_coordinate, mark_style)

    mark_points_on_this_list = [12, 17, 18, 19, 22, 27, 28] # points to mark
    # plt.plot(xs, ys, '-gD', markevery=mark_points_on_this_list)
    display_plot_object.draw_plot(xs, ys, '-gD', '', mark_points_on_this_list)

    xs = np.linspace(-np.pi, np.pi, 25)
    ys = np.sin(xs)
    factor = 2
    x_data, y_data = xs*factor, ys*factor
    display_plot_object.draw_plot(x_data, y_data, linestyle='-b<', linewidth=2)

    t = np.arange(0., 5., 0.2)
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

    x_lower, x_upper, y_lower, y_upper = -3, 15, -5, 11
    display_plot_object.set_graph_boundaries(x_lower, x_upper, y_lower, y_upper)
    plt.grid(grid_option)

    plt.show()

    figure_title, graph_title = '===== Observe II =====', r'$\sigma_i=50$'

    display_plot_object.set_figure_and_graph_titles(figure_title, graph_title)

    coordinates, text, mark_style, line_color, linestyle, linewidth = [2, 2], 'HELLO', 'gx', 'blue', linestyles[1], 2
    display_plot_object.mark_coordinate_with_intersecting_lines_and_label(coordinates, text, mark_style, line_color, linestyle, linewidth)

    display_plot_object.set_graph_boundaries(x_lower, x_upper, y_lower, y_upper)

    points_to_be_marked = [(1, 2), (2, 3), (4, 5), (3, 4), (6, 7), (6, 7), (3, 8)]
    texts_for_labelling = ['x00', 'x01', 'x02', 'x03', 'x04', 'x04', 'x05']
    mark_styles = ['gx', 'ro', 'b<', 'b>', 'b:', 'r1', 'g^']
    line_colors = ['blue', 'green', 'black', 'red', 'green', 'black', 'red']
    linestyles = [linestyles[0], linestyles[1], linestyles[2], linestyles[3], linestyles[0], linestyles[1], linestyles[2]]
    linewidths = [2, 1, 3, 1, 2, 1, 2]
    #print ([x[1] for x in points_to_be_marked])

    display_plot_object.mark_multiple_coordinates_with_intersecting_lines_and_labels(points_to_be_marked, texts_for_labelling, mark_styles,
                                                                     line_colors, linestyles, linewidths)

    plt.grid(grid_option)
    plt.show()

"""
================    ===============================
character           description
================    ===============================
   -                solid line style
   --               dashed line style
   -.               dash-dot line style
   :                dotted line style
   .                point marker
   ,                pixel marker
   o                circle marker
   v                triangle_down marker
   ^                triangle_up marker
   <                triangle_left marker
   >                triangle_right marker
   1                tri_down marker
   2                tri_up marker
   3                tri_left marker
   4                tri_right marker
   s                square marker
   p                pentagon marker
   *                star marker
   h                hexagon1 marker
   H                hexagon2 marker
   +                plus marker
   x                x marker
   D                diamond marker
   d                thin_diamond marker
   |                vline marker
   _                hline marker
================    ===============================
markers=['.',',','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D','d','|','_']
descriptions=['point', 'pixel', 'circle', 'triangle_down', 'triangle_up','triangle_left', 'triangle_right', 'tri_down', 'tri_up', 'tri_left','tri_right', 'octagon', 'square', 'pentagon', 'plus (filled)','star', 'hexagon1', 'hexagon2', 'plus', 'x', 'x (filled)','diamond', 'thin_diamond', 'vline', 'hline']
x=[]
y=[]
for i in range(5):
    for j in range(5):
        x.append(i)
        y.append(j)
plt.figure()
for i,j,m,l in zip(x,y,markers,descriptions):
    plt.scatter(i,j,marker=m)
    plt.text(i-0.15,j+0.15,s=m+' : '+l)
plt.axis([-0.1,4.8,-0.1,4.5])
plt.tight_layout()
plt.axis('off')
plt.show()  

"""