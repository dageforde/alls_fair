# Overview
This is a script for generating a pair rotating schedule for a team of any size working through a project consisting of any number of sprints, given a .json file structured like the one included in with this project

# Requirements
    * Python 3.10.2

# Sample Execution & Output
/usr/local/bin/python3 /Users/Christiaan/pyprojects/tandem/alls_fair/pairing.py 

{'Sprint_1': {'pairs': [{'Pair_1': ['PJ', 'AJ']},
                        {'Pair_2': ['CJ', 'DJ']},
                        {'Solo': ['TJ']}]},
 'days': 5,
 'start_date': 'February 28 2022'}
*********************
{'Sprint_2': {'pairs': [{'Pair_1': ['TJ', 'PJ']},
                        {'Pair_2': ['AJ', 'CJ']},
                        {'Solo': ['DJ']}]},
 'days': 5,
 'start_date': 'March 07 2022'}
*********************
{'Sprint_3': {'pairs': [{'Pair_1': ['DJ', 'TJ']},
                        {'Pair_2': ['PJ', 'AJ']},
                        {'Solo': ['CJ']}]},
 'days': 5,
 'start_date': 'March 14 2022'}
*********************

# Acceptance Criteria
- User can view pair rotation schedule. In this case, the schedule is printed to the terminal
- Each developer pairs with every other developer an equal number of times during the project, or as
close to equal as possible. 
- During any given sprint, at most 1 dev is solo
- The sprint schedule data is persisted. In this case, the data is written back to the directory in a csv file.
