# Eric Reece - 1/3/2021
# This is a refresher program for simple python arithmetic:
#   - Takes user input to display their name in reverse.
#   - It will calculate the area of a circle given a user-provided radius.
#   - Takes a series of values separated by commas, then produces a list and tuple of said values.

# Key features: utilizes a defined function, string manipulation, input validation, sorted() function,
import string
import math


# Function to obtain the area of a circle given a radius

def get_area(r):
    return math.pi * (r * r)


if __name__ == '__main__':

    firstName = input("Enter your first name: ")
    lastName = input("Hello, " + firstName + ", what is your last name? ")

    print("Your name in reverse is: " + lastName + " " + firstName)
    radius = float(input("Enter a radius to compute the area of a circle: "))
    print(get_area(radius))

    user_continue = True
    while user_continue:
        values = input("Enter a series of numbers separated by commas: ")
        user_list = values.split(",")
        user_tuple = tuple(user_list)

        print('List: ', sorted(user_list))
        print('Tuple: ', sorted(user_tuple))
        user_choice = input("Would you like to enter another list of values? (y/n)")
        while user_choice not in ['y', 'n']:
            user_choice = input("Please enter either y or n.\nContinue? ")
        if user_choice != 'y':
            user_continue = False
            print("Good bye.")
    exit()
