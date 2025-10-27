"""
    What are the type(s) of error(s) with this program?
    <Your answer here>
    
    How did you fix them?
    <Your answer here>
"""

"""
    This program is a average grade calculator.
    Student can use this to calculate their average for a class
"""


"""
   This function will take two parameters:
    the sum of all grades
    the total assignments
    
    and return the average grade
"""
def calculate_average(sum_of_all_grades, total_assignments):
    return sum_of_all_grades / total_assignments



# set up the variables
count = 1  # this will keep track of all grades we processed so far
grades_sum = 0  # this will keep track of the sum of all grades

# ask the user how many grades they want to enter
total_assignments = int(input("Enter the total number of assignments:"))

# as long as we have not processed all grades, we will ask for
# the next grade and add them to the sum of all grades
while count <= total_assignments:
    # ask for the grade
    grade = int(input("Enter the grade for assignment #" + str(count) + ":"))
    
    # add it to the sum of all grades
    grades_sum += grade
    count +=1
    
    # have we processed all grades yet?
    if count-1 == total_assignments:
        # Yes, we have processed all of them, so now we need to calculate and show the average.
        average = calculate_average(grades_sum, total_assignments)
    
    else:
    # No, we have not processed all assignments yet, so we go back to the loop.
        continue

# We have finished processing all grades, so we want to show the result.
print("Your average grade for this class is:" +  average)