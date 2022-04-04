# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# def is_consecutive(a_list):

def is_consecutive(a_list):
    b_list = list(range(min(a_list), max(a_list)+1))
    print(a_list == b_list)

a_list = [7,9,6,5,3]
a_list = sorted(a_list)

is_consecutive(a_list)