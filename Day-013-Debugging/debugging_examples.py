"""
Day 13 - Debugging

This file contains the debugging exercises completed during Day 13
of Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

Each section includes the original buggy code and the corrected version,
along with a brief explanation of the issue.
"""
# ----------------------------------------------------------------------
# Exercise 1: Debugging Odd or Even
# Original Code:
# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
    
# Fixed Code:
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

print(odd_or_even(15))

# ----------------------------------------------------------------------
# Exercise 2: Debugging Leap Year
# Original Code:
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# Fixed Code:
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap(1900))

# ----------------------------------------------------------------------
# Exercise 3: Debugging FizzBuzz
# Original Code:
# Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])

# Fixed Code:
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
            
fizz_buzz(15)
