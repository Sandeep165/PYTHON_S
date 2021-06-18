#python arithmetic operators
'''
Addition            +
Substraction        -
Multiplication      *
Division            /
Floor division      //
Exponential         **
Modulus             %

'''

#string formatting

name = "John"
age = 21
city = "mumbai"

# print("My name is ", name, "My age is ", age, "I live in ", city) # method 1
# print("My  name is {name} My age is {age} I live in {city}".format(name = "John",age = 22,city = "mumbai"))#method
# print(f"My name is {name}. My age is {age}. I live in {city}") #method

# num1 = int(input("Enter the number1:-"))
# num2 = int(input("Enter the number2:-"))
# print(f"Addition of {num1} & {num2} is : {num1 + num2}")
# print(f"Subtraction of {num1} & {num2} is : {num1 - num2}")

# print("Addition of ", num1, "and", num2,"is :-", num1+num2)
# print("Substraction of ", num1, "and", num2,"is :-", num1-num2)
# print("Division of ", num1, "and", num2,"is :-", num1/num2)
# print("Multiplication of ", num1, "and", num2,"is :-", num1*num2)
# print("Floor Division of ", num1, "and", num2,"is :-", num1//num2)
# print("Modulo of ", num1, "and", num2,"is :-", num1%num2)
# print("Exponential of ", num1, "and", num2,"is :-", num1 ** num2)



#Python Assignment operators
'''
=
+=  
-= 
*=

num_1 = 10
num_1 -= 5 # 10 +5 
print(num_1)
'''


#Python Comparison operator
'''
== (t/f)    comparison
!=          not equals to
x>y         greater than    
x<y         less than
a>=b        greater than equal
b<=a        less than equal

'''
a = 5
b = 10
print(a < b) # True
print(a > b) # False


#python logical operator

'''
and 
t t -_> t
t f --> f
f t --> f
f f --> f

or
t t --> t
t f --> t
f t --> t
f f --> f

not
t --> f
f --> t
'''

x = 10

# print(x>5 and x <9) # false
# print(x>11 or x<9) # false
# print(not(x>5 and x <9)) # True

# is operator // ==
list1 = ["apple","mango"]
list2 = ["apple", "mango"]
x = list1

# print(list1 == list2)  # true
# print(list1 is x)      # true
# print(list1 is list2)  #false

x = 10  
#true and false   --> false
print(x>5 and x < 9) # false
print(x>11 or x<9) # false



# data type ----> String(str)
'''
Twinkle, twinkle, little star\n
How I wonder what you are\n
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
'''

name = " Father's "

name = 'Sam'  #father's

name = '''
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are 
'''

# print(name)

string = "hello world"
print(string[4]) # o
print(string[6]) # w
print(string[-7]) # 0

# string slicing   var_name[start:end:step]   #start inclusive end exclusive

str1 = "I love python"
print(str1[::1])
