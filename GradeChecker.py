#Determines final grade output text
def final_grade(number):
    if number >80:
        print(f"Final grade is {number}% - Distinction")
        run_again()
    elif number >=40 and number <= 80:
        print(f"Final grade is {number}% - Pass")
        run_again()
    else:
        print(f"Final grade is {number}% -Fail")
        run_again()
#Checks whether to round grade up
def multiple_of_5_check(grade):
    grade_check = grade
    original_grade = grade
    if grade_check %5 ==0:
        final_grade(original_grade)
    else:
        while grade_check %5 != 0:
            grade_check +=1
#Checks the difference between the original grade and the next multiple of 5
            difference = grade_check - original_grade
        if difference <3:
            final_grade(grade_check)
        else:
            final_grade(original_grade)
#checks if the user wants to check another grade
def run_again():
    check = input("\nWould you like to check another grade 'y' or 'n'?")
    if check == "y":
        grade_checker()
    else:
        print("Okay, have a nice day!")
#Initial check to see if grade is higher than 40
def grade_checker():
    grade = int(input("\nPlease type in the grade you want to check to find out if it is a Fail, Pass or Distinction\n"))
    if grade <=39:
        final_grade(grade)

    else:
        multiple_of_5_check(grade)
#This starts off the whole process
grade_checker()
