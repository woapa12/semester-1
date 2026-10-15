# Worksheet 1.2: Task 1 Solution
import sys
score = input("Enter grade from 0-100: ")
def validateScore(score):
    if not score.isnumeric():
        return False
    if int(score) > 100 or int(score) < 0:
        return False
    return True

if not validateScore(score):
    sys.exit("Error: Grade must be an integer between 0 and 100")
else:
    score = int(score)
    if score < 40:
        result = "Fail"
    elif score < 70:
        result = "Pass"
    else:
        result = "Distinction"
    print(str(score) + " is a "+result)
