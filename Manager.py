class Manager:
    # Here's the class that does all the heavy work
    # The primary way in which all the data gets cleaned
    # and pushed to the Google sheet
    def __init__(self, authorize):
        # Just the init method establishing access
        # to the main tab self.master_roster
        # a list for the student names with their col and row
        # and a list to store the weeks with their respective range
        self.master_roster = authorize.initialize(0)
        self.student_cells = self.master_roster.range("A3:A71")

        self.week_ranges = ["B{0}:B{0}", "C{0}:I{0}"]

    def parse_input(self, user_input):
        clause, arguments = ";", ","
        command_pos, arguments_pos = 0, 1

        if not clause in user_input:
            return user_input.strip(), ()

        parsed_clauses = user_input.split(clause)

        command = parsed_clauses[command_pos].strip()
        dirty_arguments = parsed_clauses[arguments_pos].split(arguments)
        arguments = [str(args.strip().upper()) for args in dirty_arguments]

        return command, tuple(arguments)

    def grade_name_week(self, name, week):
        # This method grades by individual student. It loops through
        # the weeks assignments and updates grades at the end.

        # Formats name and week to find in the sheet.
        name, week = " ".join([n.lower().capitalize() for n in name.split(" ")]), int(week)
        print("Grading {}:".format(name))

        # Finds the range of cells to easily iterate through.
        name_cell = self.master_roster.find(name)
        week_range = self.week_ranges[week].format(name_cell.row)
        week_range_assnmnts = self.master_roster.range(week_range)

        # Iterate and ask for grade for each assignment.
        for assnmnt in week_range_assnmnts:
            assnmnt_name = self.master_roster.cell(2, assnmnt.col).value
            assnmnt.value = input("{} grade is ".format(assnmnt_name))


        # Updates grades in batch
        self.master_roster.update_cells(week_range_assnmnts)

        # Return for State in Editor.py
        return "Grading {} for week {} complete".format(name, week)

    def grade_by_week(self, week):
        # Iterate through all students of the chosen week
        for stdnt in self.student_cells:
            print(self.grade_name_week(stdnt.value, week))
        return "All students graded for week {}".format(week)

    def grade_by_range(self, start, end, week):
        start, end = int(start), int(end)
        student_cells = self.master_roster.range("A{}:A{}".format(start, end))
        for cell in student_cells:
            print(self.grade_name_week(cell.value, week))
