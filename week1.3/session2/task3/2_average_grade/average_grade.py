# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

with open("student_data.csv", "r") as file:
    header = file.readline()
    data = []
    for line in file:
        data.append(line.split(",")) 
        # Each line is a subarray of elements in data
        




# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

def findAverages():
    studentAverages = {} # ID: (Name, Average)
    for i in data:
        average = (int(i[2]) + int(i[3]) + int(i[4])) / 3

        studentAverages[i[0]] = (i[1], average)
    return studentAverages

with open("report.txt", "w") as file: 
    students = findAverages()
    lines = []
    lines.append("ID,Name,Average")
    for key, value in students.items():
        ID = key
        name = value[0]
        average = value[1]

        line = f"{ID},{name},{average:.2f}"
        lines.append(line)

    for line in lines:
        file.write(line+"\n")


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
