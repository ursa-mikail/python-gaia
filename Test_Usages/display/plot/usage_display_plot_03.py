####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/display/plot')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/time')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/data/data_structure')
sys.path.append(lib_path)


# import package from path
from data_generator import data_generator  # file name
from display_plot import display_plot
from timer_0 import timer_0 as timer	# file name
# from timer import timer	# file name
from json_manager import json_manager



####################################
## main
####################################
if __name__ == "__main__":
    id_timer = "Test Usage Agent: < timer >"
    print("=====[" + id_timer + " Start]===== \n")
    timer_object = timer(id_timer)
    print("\ntimestamp: " + timer_object.get_timestamp(), "\n\n")
    """

    """
    id_json_manager = "Usage Agent: <json_manager>"
    print("=====[" + id_json_manager + " Start]===== \n")
    json_manager_object = json_manager(id)
    # https://jsonlint.com, https://www.freeformatter.com/json-validator.html
    json_file = ['./data_test/in_0.json', './data_test/domain_scores_in.json', './data_test/domain_scores_out.json']

    labels_scores = 'pneumaScores', 'somaScores', 'psycheScores', 'opusScores', 'kismetScores', 'CEDIP_scores'

    file_json_chosen = json_file[1]
    json_file_data = json_manager_object.load_json_data_from_file(file_json_chosen)
    #print(json_file_data)
    #print(json_file_data[labels_scores[0]])
    pneumaScores = json_file_data[labels_scores[0]]
    somaScores = json_file_data[labels_scores[1]]
    psycheScores = json_file_data[labels_scores[2]]
    opusScores = json_file_data[labels_scores[3]]
    kismetScores = json_file_data[labels_scores[4]]
    CEDIP_scores = json_file_data[labels_scores[5]]


    """
    file_json_chosen = json_file[1]
    json_manager_object.write_json_data_to_file(json_file_data, file_json_chosen)
    """

    labels = 'Pneuma', 'Soma', 'Psyche', 'Opus', 'Kismet', 'CEDIP_scores'
    score_book = [pneumaScores, somaScores, psycheScores, opusScores, kismetScores, CEDIP_scores]
    number_of_graphs = len(score_book)

    id_display_plot = "Test Usage Agent: <display_plot >"
    print("=====[" + id_display_plot + " Start]===== \n")
    display_plot_object = display_plot(id_display_plot)

    grid_option = True

    markings = ['ko-', 'r.-', 'bx-', 'g+', 'g^', 'cs', 'm*']
    titles = []
    title = 'Ayahuasca'
    title_main = title
    description_x_label, description_y_label = 'x_axis', 'y_axis'
    plot_marker_style = markings[0]

    colors = ['green', 'yellow', 'brown', 'orange', 'violet', 'indigo', 'purple', 'magenta', 'cyan', 'black', 'white',
              'blue']
    background_color, line_color, linewidth = colors[10], colors[0], 2
    display_plot_object.define_settings(background_color, line_color, linewidth)
    bar_option = ['VERTICAL', 'HORIZONTAL']
    bar_option_chosen = bar_option[0]

    # display_plot_object.display_bar_chart (title_main, title, x_data, y_data, error, description_x_label, description_y_label, bar_option_chosen, grid_option)
    # display_plot_object.display_graph(title_main, title, x_data, y_data, description_x_label, description_y_label, plot_marker_style, grid_option)

    percentages = [15, 30, 45, 10]
    explode_options = (0, 0.1, 0, 0)  # only "explode" the 2nd slice
    # display_plot_object.display_pie_chart(title_main, title, labels, percentages, explode_options)

    grid_options = [True, False, True, False, True, False, True]
    x_axis_data_sets, y_axis_data_sets = [], []
    plot_marker_styles = []
    subplot_choices = ['ROW_WISE', 'COLUMN_WISE']
    row_or_column_wise_option = subplot_choices[1]
    description_x_labels = []
    description_y_labels = []
    title_main = title

    description_x_label, description_y_label = 'days', 'scores'

    for i in range(0, number_of_graphs):
        x_axis_data_sets.append(range(0, len(score_book[i])))
        y_axis_data_sets.append(score_book[i])
        # plot_marker_styles.append(markings[i])
        plot_marker_styles.append(markings[2])
        description_x_labels.append(description_x_label)
        description_y_labels.append(description_y_label)
        titles.append(labels[i])


    color_sets = [colors[0], colors[1], colors[2]]
    scale = x_axis_data_sets[1]
    print("scale: ", scale)

    # annotations = None
    annotations = ['test_00', 'test_01']
    """
    display_plot_object.display_graph_row_or_column_wise(title_main, titles, x_axis_data_sets, y_axis_data_sets,
                                                         description_x_labels, description_y_labels, plot_marker_styles,
                                                         row_or_column_wise_option, grid_options, annotations)

    display_plot_object.display_graph_evenly(title_main, titles, x_axis_data_sets, y_axis_data_sets,
                                             description_x_labels, description_y_labels, plot_marker_styles,
                                             grid_options)

    """
    choice_index = 5
    x_axis_data, y_axis_data = x_axis_data_sets[choice_index], y_axis_data_sets[choice_index]
    title = labels[choice_index]
    description_x_label, description_y_label, plot_marker_style = description_x_labels[choice_index], description_y_labels[choice_index], plot_marker_styles[choice_index]
    display_plot_object.display_graph (title_main, title, x_axis_data, y_axis_data, description_x_label, description_y_label, plot_marker_style, grid_option, annotations)


    average_scores = [float(sum(pneumaScores)/len(pneumaScores)), float(sum(somaScores)/len(somaScores)),
                      float(sum(psycheScores)/len(psycheScores)), float(sum(opusScores)/len(opusScores)),
                      float(sum(kismetScores)/len(kismetScores)), float(sum(CEDIP_scores)/len(CEDIP_scores)), ]

    for i in range(0, number_of_graphs):
        print(labels[i], " : ", average_scores[i])

    print("=====[" + id_display_plot + " End]===== \n")

"""
# version: 2018-04-07_1553hr_03sec
"""