from Manager import *
from Authorize import *
from Data import *

def editor(state, feeds, googleapis, json_file, spread_sheet_name):
    manager = Manager(Authorize(feeds, googleapis, json_file, spread_sheet_name))
    termination_clause = "EXIT"
    manager_functions = {"exit" : lambda: termination_clause,
                         "help" : lambda: manager_keys,
                         "grade" : manager.grade_name_week}
    manager_keys = "The commands are: " + ', '.join([k for k in manager_functions.keys()])

    while state != termination_clause:
        try:
            print(state)
            command, arguments = manager.parse_input(input("Ready for next Command \n"))
            state = manager_functions[command](*arguments)
        except KeyError:
            state = "Wrong command!"
        except TypeError:
            state = "Wrong arguments!"
        except ValueError:
            state = "Invalid argument types!"
        except gspread.exceptions.CellNotFound:
            state = "Cell not found!"



editor("Start editing", feeds, googleapis, json_file, spread_sheet_name)