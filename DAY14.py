# From a list containing ints, strings and floats, make three lists to store them separately.
# lst = [1,2,3,4,5,6,"a","b","c","d",10.1,2.2,36.1]

# integer = [1,2,3,4,5,6]
# string = ["a","b","c","d"]
# my_float = [10.1,2.2,36.1]


# lst = [1,2,3,4]
# new_lst = []
# for i in lst:
#     new_lst.append(i)
#     print(new_lst)

'''
[1]
[1,2]
[1,2,3]
[1,2,3,4]
'''
'''
#Functions/classes ----->DRY(do not repeat yourself)
parammeter/arguments---/

def xyz(a,b):----------------> func declaration(parameters)
    {body}
    {body}-------------------> func body
    {body}
xyz("john","sam")------------> func call(arguments)

'''


# def greet(name):
#     print(f"Good morning {name}")

# def greet(name):
#     return(f"Good morning {name}")

# # return---you are returnig the cvalue to the func itself
# # return ---- {logic/print} = func_name ------> var_name = func_name() -----> var_name
# # print ------{logic} ----> console

# res = greet("Tom")
# print(res)



# def greet(name):
#     return(f"Good morning {name}")
# print(greet("Tom"))     # greet = return{}  ----> print(greet)


def display(name="students"):
    print(f"Good morning {name}")
display()


# calculator(): add...subs..mul...div

'''
Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both.
 If the salary is missing in the function call assign default value 9000 to salary
'''
# def calcu(a,b):
#     print(f"addition of {a} and {b} is: {a+b}")
#     print(a-b)
#     print(a/b)
#     print(a*b)
# num1=int(input('Enter number 1:'))
# num2=int(input('Enter number 2:'))
# calcu(num1,num2)

def showinfo(lst):
    for i in lst:
        print(i)
   

# showinfo('Harsh',25000)
showinfo([1,2,3,4,5,6,7,8,9])
'''
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius


Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4


Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5


Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2

Write a Python program to calculate a dog's age in dog's years. Go to the editor
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
'''