# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
# def hello_name(user_name):

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")


user_name = input("What is your username? ")
user_name = user_name.strip()

hello_name(user_name)