#Question 1
#Write a funtion to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print("hello "+ user_name + "!")

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for num in range(100):
        if num % 2 != 0:
            print(num)

first_odds()

#Question 3
#Please write a python function, max_num_in_list to return the max number of a given list. 

a_list=[1,5,8,77,99,178,199,251,256]
def max_num_in_list(a_list):
    
    print("the largest number in the list is " + str(max(a_list)))
max_num_in_list(a_list)

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisable ny 4 , but not
#divisible by 100, unless it is also divisable by 400.The return should be a boolean Type(true/false).

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0:
        return True
    return False
print(is_leap_year(2020))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but 
# [1,2,4,5] are not consecutive numbers. The return should be boolean type.


def is_consecutive(num):
    for i in range (len(num)-1):
        if num[i] + 1 != num[i+1]:
            return False
    return True
list=[1,2,3,4,5]
print(is_consecutive(list))
