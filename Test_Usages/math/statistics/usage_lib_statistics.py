from usage_lib_statistics_support import *
from usage_lib_statistics_test_00 import *
from usage_lib_statistics_test_01 import *
from usage_lib_statistics_test_02 import *
from usage_lib_statistics_test_03 import *


####################################
## main
####################################
ON, OFF = True, False
declaration_silent = ON

if __name__ == "__main__":
    id_data_processor = "Test Usage Agent <data_processor>"
    id_data_manipulator = "Test Usage  Agent <data_manipulator>"
    id_lib_statistics = "Test Usage  Agent <lib_statistics>"
    id_display_console = "Test Usage  Agent <display_console>"
    id_data_generator = "Test Usage Agent: <data_generator>"
    id_display_plot = "Test Usage Agent: <display_plot >"

    object_ids = [id_data_processor, id_data_manipulator, id_lib_statistics, id_display_console]

    if (declaration_silent == OFF):
        declare_object_start(object_ids)

    data_processor_object = data_processor(id_data_processor)
    data_manipulator_object = data_manipulator(id_data_manipulator)
    lib_statistics_object  = lib_statistics(id_lib_statistics)
    display_console_object = display_console(id_display_console)

    # test_00(data_manipulator_object, lib_statistics_object, display_console_object)
    
    object_ids = [id_data_generator, id_display_plot]
    declare_object_start(object_ids)
    data_generator_object = data_generator(id_data_generator)
    display_plot_object = display_plot(id_display_plot)

    # test_01(data_generator_object, display_plot_object, lib_statistics_object)
    # test_02(lib_statistics_object)
    test_03(lib_statistics_object)

    object_ids = [id_data_processor, id_data_manipulator, id_lib_statistics, id_display_console, id_data_generator, id_display_plot]

    if (declaration_silent == OFF):
        declare_object_end(object_ids)

"""
# version: 2018-01-18_2324hr_42sec
"""

# ref: https://plot.ly/matplotlib/histograms/
# https://stackoverflow.com/questions/22127769/python-frequency-of-occurrences
# https://stackoverflow.com/questions/28709564/matplotlib-histogram-with-frequency-and-counts
# https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/