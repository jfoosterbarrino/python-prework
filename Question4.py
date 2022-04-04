# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
# def is_leap_year(a_year):

def is_leap_year(a_year):
    print(a_year % 400 == 0 or a_year % 100 != 0 and a_year % 4 ==0)

a_year = int(input("Please enter the year: "))

is_leap_year(a_year)
