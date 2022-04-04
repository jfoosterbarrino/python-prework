# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
# def hello_name(user_name):

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")


user_name = input("What is your username? ")
user_name = user_name.strip()

hello_name(user_name)


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
# def first_odds():

def first_odds():
    for value in range(1,101,2):
        print(value)
    return None

first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
# def max_num_in_list(a_list)

def max_num_in_list(a_list):
    print(max(a_list))

a_list = [43,97,65,3,25]

max_num_in_list(a_list)


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
# def is_leap_year(a_year):

def is_leap_year(a_year):
    print(a_year % 400 == 0 or a_year % 100 != 0 and a_year % 4 ==0)

a_year = int(input("Please enter the year: "))

is_leap_year(a_year)


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# def is_consecutive(a_list):

def is_consecutive(a_list):
    b_list = list(range(min(a_list), max(a_list)+1))
    print(a_list == b_list)

a_list = [7,9,6,5,3]
a_list = sorted(a_list)

is_consecutive(a_list)