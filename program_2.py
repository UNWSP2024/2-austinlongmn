# Age Average Calculator
# Programmer: Austin Long
# Date: 1/28/2025

def average_age():
    # Declare constants
    number_of_friends = 5

    # Get User Input
    age_1 = int(input("Enter friend 1's age: "))
    age_2 = int(input("Enter friend 2's age: "))
    age_3 = int(input("Enter friend 3's age: "))
    age_4 = int(input("Enter friend 4's age: "))
    age_5 = int(input("Enter friend 5's age: "))

    # Sum ages
    age_sum = age_1 + age_2 + age_3 + age_4 + age_5

    # Average the ages (integers are automatically cast to floats here)
    age_average = age_sum / number_of_friends

    # Print the results
    print(age_average)

# Line which calls the above function.
average_age()