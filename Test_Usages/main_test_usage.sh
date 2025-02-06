# add to Automated test registry
# all tests are added for automated testing

# to-do:
# update a counter for number of test run
# for each module test run, update the status run as : n of N completed, and announced which test is done. 
# update the version

source_subject_folder='./time/'
eval "cd ${source_subject_folder}"
clear; python3 usage_timer.py
eval "cd -"


# version: 2017-09-23_1351hr_07sec