# Initiate variables
grade_all = 0
credits_all = 0
total_weighted_grade = 0
list_of_grades = []


# While grade is 0, ask for grade.
while True:
        grade = round(float(input()), 1)
        # If grade is less than 0, break loop, no output.
        if grade < 0:
            break
        # Else ask for credits.
        credits = int(input())
        # Add up credits with every runthrough.
        credits_all += credits
        # Add grades to list of grades with every runthrough.
        list_of_grades.append(grade)
        # Calculate total weighted grade.
        total_weighted_grade += grade *credits


# Once loop is broken, calulate weighted average, given toatl credts are not 0.
if credits_all != 0:
    weighted_avg_grade = total_weighted_grade/credits_all
    weighted_avg_grade = round(weighted_avg_grade, 2)

    # Print result.
    print(f"Weighted average grade: {weighted_avg_grade}")
# printing highest value in list, given list is not empty.
if list_of_grades:
    print(f"Highest grade: {max(list_of_grades)}")


