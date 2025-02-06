# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import math
import mplcursors
import numpy as np

# ref: https://matplotlib.org/gallery.html

class display_plot:
    """ Template model of Gaia """
    id = ""

    def __init__(self, id):
        self.id = id
        self.fig                = None
        self.annotation_control = None
        self.sc                 = None
        self.plot_index         = None # ax
        self.norm               = None
        self.cmap               = None
        self.line               = None
        self.x, self.y          = None, None
        self.annotations_on_points = None
        self.c                  = np.random.randint(1,5,size=15)
        print ("_gaia object [%s] is born\n" % self.id)

    def define_settings (self, background_color, line_color, linewidth):
        plt.rcParams['axes.facecolor'] = background_color  # set background color
        plt.rcParams['lines.color'] = line_color
        plt.rcParams['lines.linewidth'] = linewidth

        return None

    # ref: https://matplotlib.org/users/customizing.html

    # This should be called before others as it initiates the graph
    def set_figure_and_graph_titles(self, figure_title, graph_title):
        plt.figure(figure_title)
        #fig = plt.figure()
        #fig.suptitle("Title centered above all subplots", fontsize=14)
        plt.title(graph_title)
        return None

    def draw_vertical_line(self, x_coordinate, line_color=None, linestyle=None, linewidth=None):
        plt.axvline(x_coordinate, color=line_color, linestyle=linestyle, linewidth=linewidth)
        return None

    def draw_horizontal_line(self, y_coordinate, line_color=None, linestyle=None, linewidth=None):
        plt.axhline(y_coordinate, color=line_color, linestyle=linestyle, linewidth=linewidth)
        return None

    def set_x_and_y_axis_labels(self, x_label, y_label, fontsize = None, color = None):
        plt.xlabel(x_label, fontsize=fontsize, color=color)
        plt.ylabel(y_label, fontsize=fontsize, color=color)
        return None

    def draw_plot(self, x_data, y_data, linestyle=None, linewidth=None, mark_points_on_this_list=None):
        plt.plot(x_data, y_data, linestyle, linewidth, markevery=mark_points_on_this_list)
        return None

    def set_graph_boundaries(self, x_lower, x_upper, y_lower, y_upper):
        x_boundaries_y_boundaries = [x_lower, x_upper, y_lower, y_upper]
        plt.axis(x_boundaries_y_boundaries)
        return None

    def mark_coordinate(self, x_coordinate, y_coordinate, mark_style):
        plt.plot(x_coordinate, y_coordinate, mark_style)
        return None

    def set_text_in_graph(self, position_of_text_in_graph, text):
        plt.text(position_of_text_in_graph[0], position_of_text_in_graph[1], text)
        return None

    def mark_coordinate_with_intersecting_lines_and_label (self, coordinates, text, mark_style = None, line_color=None, linestyle=None, linewidth=None):
        offset_for_text = 0.2
        x_coordinate, y_coordinate = coordinates[0], coordinates[1]
        self.draw_horizontal_line(y_coordinate, line_color, linestyle, linewidth)
        self.draw_vertical_line(x_coordinate, line_color, linestyle, linewidth)
        coordinates_of_text = [float(x_coordinate + offset_for_text), float(y_coordinate + offset_for_text)]
        print(coordinates_of_text)
        self.set_text_in_graph(coordinates_of_text, text)
        self.mark_coordinate(x_coordinate, y_coordinate, mark_style)

        return None

    def mark_multiple_coordinates_with_intersecting_lines_and_labels(self, coordinates_list, text_list, mark_style_list=None, line_color_list=None,
                                                          linestyle_list=None, linewidth_list=None):
        number_of_coordinates = len(coordinates_list)

        for i in range(0, number_of_coordinates):
            self.mark_coordinate_with_intersecting_lines_and_label(coordinates_list[i], text_list[i], mark_style_list[i], line_color_list[i],
                                                                   linestyle_list[i], linewidth_list[i])

        return None

    def update_annotation_for_scatter_plot(self, ind):
        pos = self.sc.get_offsets()[ind["ind"][0]]
        self.annotation_control.xy = pos
        # text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), " ".join([names[n] for n in ind["ind"]]))
        # text = 'trial-text \n' * 5
        self.annotations_on_points = 'trial-text \n' * 5

        self.annotation_control.set_text(self.annotations_on_points)
        # self.annotation_control.get_bbox_patch().set_facecolor(self.cmap(self.norm(self.c[ind["ind"][0]])))
        self.annotation_control.get_bbox_patch().set_alpha(0.4)

        return None

    def hover_to_reveal_text_for_scatter_plot(self, event):
        vis = self.annotation_control.get_visible()
        if event.inaxes == self.plot_index:
            cont, ind = self.sc.contains(event)
            # cont, ind = self.line.contains(event)
            if cont:
                self.update_annotation_for_scatter_plot(ind)
                self.annotation_control.set_visible(True)
                self.fig.canvas.draw_idle()
            else:
                if vis:
                    self.annotation_control.set_visible(False)
                    self.fig.canvas.draw_idle()

        return None

    def display_scatter_plot (self, title_main, title, x_axis_data_sets, y_axis_data_sets, description_x_label, description_y_label, scale, color_sets, grid_option = False, annotations = None):
        #plt.figure(title_main)
        #plt.title(title)

        # number_of_sets = len(x_axis_data_sets)

        self.fig, self.plot_index = plt.subplots()
        # self.fig.suptitle(title_main, fontsize=10)
        self.plot_index.set_title(title)

        set_index = 0

        for color_index in color_sets:
            self.sc = plt.scatter(x_axis_data_sets[set_index], y_axis_data_sets[set_index], c=color_index, s=scale, label=color_index,
                       alpha=0.3, edgecolors='none')
            set_index = set_index + 1

        if (annotations != None):
            for i, text in enumerate(annotations):
                plt.annotate(text, (x_axis_data_sets[i], y_axis_data_sets[i]))

            self.annotation_control = self.plot_index.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                                bbox=dict(boxstyle="round", fc="w"),
                                arrowprops=dict(arrowstyle="->"))
            self.annotation_control.set_visible(False)

            self.fig.canvas.mpl_connect("motion_notify_event", self.hover_to_reveal_text_for_scatter_plot)

        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.legend()

        plt.xlabel(description_x_label)
        plt.ylabel(description_y_label)
        plt.grid(grid_option)

        plt.show()

        return None

    def display_pie_chart (self, title_main, title, labels, percentages, explode_options):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        plt.figure(title_main)
        plt.title(title)
        plt.pie(percentages, explode = explode_options, labels = labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()

        return None

    def display_bar_chart (self, title_main, title, x_axis_data, y_axis_data, error, description_x_label, description_y_label, bar_option, grid_option = False):
        plt.figure(title_main)
        plt.title(title)

        if (bar_option == 'VERTICAL'):
            plt.bar(x_axis_data, y_axis_data, align = 'center')
        elif (bar_option == 'HORIZONTAL'):
            plt.barh(y_axis_data, x_axis_data, xerr=error, align='center',
                color='green', ecolor='black')
        else:
            print('Unavailable option: ', bar_option)

        plt.xlabel(description_x_label)
        plt.ylabel(description_y_label)

        plt.grid(grid_option)
        plt.show()

        return None

    def display_histogram (self, title_main, title, x_axis_data, x_data_labels, description_x_label, grid_option = False):
        description_y_label = "Frequency"

        plt.figure(title_main)
        plt.title(title)
        frequencies, bins, patches = plt.hist(x_axis_data, label = x_data_labels)
        plt.legend(prop={'size': 10})
        plt.xlabel(description_x_label)
        plt.ylabel(description_y_label)

        plt.grid(grid_option)
        plt.show()

        return frequencies, bins

    def update_annotation(self, ind):
        pos = self.line.get_data()
        self.annotation_control.xy = (self.x[ind["ind"][0]], self.y[ind["ind"][0]])
        # text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), " ".join([names[n] for n in ind["ind"]]))
        # text = 'trial-text \n' * 5
        # self.annotations_on_points = 'trial-text \n' * 5

        self.annotation_control.set_text(self.annotations_on_points)
        # self.annotation_control.get_bbox_patch().set_facecolor(self.cmap(self.norm(self.c[ind["ind"][0]])))
        self.annotation_control.get_bbox_patch().set_alpha(0.4)

        return None

    def hover_to_reveal_text(self, event):
        vis = self.annotation_control.get_visible()
        if event.inaxes == self.plot_index:
            # cont, ind = self.sc.contains(event)
            cont, ind = self.line.contains(event)
            if cont:
                self.update_annotation(ind)
                self.annotation_control.set_visible(True)
                self.fig.canvas.draw_idle()
            else:
                if vis:
                    self.annotation_control.set_visible(False)
                    self.fig.canvas.draw_idle()

        return None

    def display_graph (self, title_main, title, x_axis_data, y_axis_data, description_x_label, description_y_label, plot_marker_style, grid_option = False, annotations = None):
        self.fig = plt.figure(title_main)
        plt.title(title)
        self.plot_index = plt.subplot()
        self.line,  = plt.plot(x_axis_data, y_axis_data, plot_marker_style)
        self.x, self.y = x_axis_data, y_axis_data

        if (annotations != None):
            """
            for i, text in enumerate(annotations):
                plt.annotate(text, (x_axis_data[i], y_axis_data[i]))
            """
            self.annotations_on_points = annotations
            self.annotation_control = self.plot_index.annotate("", xy=(0, 0), xytext=(20, 20),
                                                               textcoords="offset points",
                                                               bbox=dict(boxstyle="round", fc="w"),
                                                               arrowprops=dict(arrowstyle="->"))
            self.annotation_control.set_visible(False)
            self.fig.canvas.mpl_connect("motion_notify_event", self.hover_to_reveal_text)

        plt.xlabel(description_x_label)
        plt.ylabel(description_y_label)

        plt.grid(grid_option)
        plt.show()

        return None



    def display_graph_row_or_column_wise (self, title_main, titles, x_axis_data_sets, y_axis_data_sets,
                                          description_x_labels, description_y_labels, plot_marker_styles,
                                          row_or_column_wise_option, grid_options, annotations = None):

        try:
            grid_options
        except NameError: # variable undefined
            grid_options = [False] * len(x_axis_data_sets)
        else:  # variable exist
            pass;

        self.norm = plt.Normalize(1,4)
        self.cmap = plt.cm.RdYlGn

        self.fig = plt.figure(title_main)

        assert (len(x_axis_data_sets) == len(y_axis_data_sets)), "len(x_axis_data_sets) != len(y_axis_data_sets)"
        number_of_graphs = len(x_axis_data_sets)

        if (row_or_column_wise_option == 'ROW_WISE'):
            total_number_of_rows, total_number_of_columns = number_of_graphs, 1

        elif (row_or_column_wise_option == 'COLUMN_WISE'):
            total_number_of_rows, total_number_of_columns = 1, number_of_graphs

        else:
            print ('Unavailable option: ', row_or_column_wise_option)

        # plot now
        for graph_index in range(0, number_of_graphs):
            # self.plot_index := ax
            self.plot_index = plt.subplot(total_number_of_rows, total_number_of_columns, (graph_index + 1))  # graph_index starts at 1
            self.line, = plt.plot(x_axis_data_sets[graph_index], y_axis_data_sets[graph_index], plot_marker_styles[graph_index])
            self.x, self.y = x_axis_data_sets[graph_index], y_axis_data_sets[graph_index]
            plt.xlabel(description_x_labels[graph_index])
            plt.ylabel(description_y_labels[graph_index])

            plt.grid(grid_options[graph_index])
            plt.title(titles[graph_index])

            # annotations = None # turn off 1st as even-based annotation is not working yet
            if (annotations != None):
                # mplcursors.cursor(hover=True)
                self.annotation_control = self.plot_index.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
                self.annotation_control.set_visible(False)
                self.fig.canvas.mpl_connect("motion_notify_event", self.hover_to_reveal_text)
        # display plot now
        plt.show()

        return None

    def display_graph_evenly (self, title_main, titles, x_axis_data_sets, y_axis_data_sets,
                                description_x_labels, description_y_labels, plot_marker_styles, grid_options):

        try:
            grid_options
        except NameError: # variable undefined
            grid_options = [False] * len(x_axis_data_sets)
        else:  # variable exist
            pass;

        plt.figure(title_main)

        assert (len(x_axis_data_sets) == len(y_axis_data_sets)), "len(x_axis_data_sets) != len(y_axis_data_sets)"
        number_of_graphs = len(x_axis_data_sets)

        total_number_of_rows = math.sqrt(number_of_graphs)
        total_number_of_rows = math.ceil(total_number_of_rows) # == total_number_of_columns
        total_number_of_columns = total_number_of_rows

        graph_index = 0

        # plot now
        for graph_index in range(0, number_of_graphs):
            plt.subplot(total_number_of_rows, total_number_of_columns,
                        (graph_index + 1))  # graph_index starts at 1
            plt.plot(x_axis_data_sets[graph_index], y_axis_data_sets[graph_index], plot_marker_styles[graph_index])
            plt.xlabel(description_x_labels[graph_index])
            plt.ylabel(description_y_labels[graph_index])

            plt.grid(grid_options[graph_index])
            plt.title(titles[graph_index])
        # display plot now
        plt.show()

        return None

    def who_am_i(self): #
        """ Introspection """
        self.line_storage = [];

        print ("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print ("_gaia object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <display_plot>"
    print ("=====[" + id + " Start]===== \n")
    display_plot_object = display_plot(id)
    display_plot_object.who_am_i()

    # import _Gaia._gaia
    # help(display_plot) # introspect

    print ("=====[" + id + " End]===== \n");

"""
# version: 2017-11-10_2139hr_51sec
"""