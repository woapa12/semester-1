# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
file_name = input("File name: ")
# open the file
import csv
grades = [(70, "1"),
          (60, "2:1"),
          (50, "2:2"),
          (40, "3"),
          (0, "F")]
# read in the data, and for each student calculate their average grade and classification
with open(file_name, "r") as f:
    content = csv.DictReader(f)

    out = []
    for student in content:
        modules = 0
        total = 0
        for i, (key, value) in enumerate(student.items()):
            if i == 0:
                student_id = value
            elif value != "":
                modules += 1
                total += int(value)
        average = total/modules
        classification = ""
        for t, c in grades:
            if average >= t:
                classification = c
                break

        line = (f"{student_id},{average:.2f},{classification}")
        out.append(line)

    with open(f"{file_name}_out.csv", "w") as g:
        g.writelines(l + "\n" for l in out)

    

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder