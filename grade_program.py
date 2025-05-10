#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: May 8, 2025
# This program converts the level of a student to their grade


# This program converts the level of a student to their grade
def calc_grade(level):
    # initialize user_grade to -1
    user_grade = -1
    # If user enters 4+ in string then user_grade is 98
    if level == "4+":
        user_grade = 98
    # If user enters 4 in string then user_grade is 92
    elif level == "4":
        user_grade = 92
    # If user enters 4- in string then user_grade is 88
    elif level == "4-":
        user_grade = 83
    # If user enters 3+ in string then user_grade is 80
    elif level == "3+":
        user_grade = 78
    # If user enters 3 in string then user_grade is 75
    elif level == "3":
        user_grade = 75
    # If user enters 3- in string then user_grade is 73
    elif level == "3-":
        user_grade = 73
    # If user enters 2+ in string then user_grade is 70
    elif level == "2+":
        user_grade = 70
    # If user enters 2 in string then user_grade is 65
    elif level == "2":
        user_grade = 65
    # If user enters 2- in string then user_grade is 63
    elif level == "2-":
        user_grade = 63
    # If user enters 1+ in string then user_grade is 60
    elif level == "1+":
        user_grade = 60
    # If user enters 1 in string then user_grade is 55
    elif level == "1":
        user_grade = 55
    # If user enters 1- in string then user_grade is 53
    elif level == "1-":
        user_grade = 53
    # If user enters anything else then user_grade is still -1
    else:
        user_grade = -1
    # Return the user_grade
    return user_grade


def main():
    # This function gets the user input and calls the calc_grade function
    user_level = input("Enter your level: ")
    # Call the calc_grade function and store the result in user_grade
    user_grade = calc_grade(user_level)
    # If user_grade is -1
    # then print "Invalid enter."
    if user_grade == -1:
        # Print "Invalid enter."
        print("Invalid enter.")
    else:
        # Print the user_grade
        print("Your mark is: {}".format(user_grade))


if __name__ == "__main__":
    main()
