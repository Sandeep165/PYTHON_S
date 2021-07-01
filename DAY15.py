'''
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

def multiple():
    for i in range (1500, 2701):
        if(i%7==0 and i%5==0):
            print(i)

multiple()


2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius

f = (c*1.8)+32
def Cel_To_Fah(n)
    return (n*1.8)+32


Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4

n1=int(input('Enter the start of Series:'))
n=int(input('Enter the end of Series:'))
even=0
odd=0
for i in range(n1,(n+1)):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print(f'There are {even} Even and {odd} ODD Numbers between {n1} and {n}')



Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5

for i in range(0,6):
    if(i==6 or i==3):
        continue
    else:
        print(i)


Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2

string1= "Pyhton 3.2"

letter_count= 0; 
digit_count= 0
for i in range(0, len(string1)):
    if(string1[i].isdigit()):
        digit_count += 1
    elif(string1[i] == " "):
        letter_count -= 1
    else:
        letter_count += 1
print(f"Letter count:{letter_count}\nDigit count: {digit_count}")




Write a Python program to calculate a dog's age in dog's years. Go to the editor
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15 -2 =*4 + 21                                  
The dog's age in dog's years is 73



# Solve the quadratic equation ax**2 + bx + c = 0
#6x2+11x-35


string1= "Pyhton 3.2"
letter_count= 0; 
digit_count= 0
for i in range(0, len(string1)):
    if(string1[i].isdigit()):
        digit_count += 1
    elif(string1[i] == " "):
        letter_count -= 1
    else:
        letter_count += 1
print(f"Letter count:{letter_count}\nDigit count: {digit_count}")

'''

# a = int((input('Enter a: ')))
# b = int((input('Enter b: ')))
# c = int((input('Enter c: ')))

# r1=(-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
# print(r1)
# r2=(-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
# print(r2)

# print(f"root of the equation are{r1},{r2}")
# def eq_rts( a, b, c):
#     dis = b * b - 4 * a * c 
#     sqrt_val = ((abs(dis))**0.5)
     
#     if dis > 0: 
#         print(" real and different roots ") 
#         print((-b + sqrt_val)/(2 * a)) 
#         print((-b - sqrt_val)/(2 * a)) 
      
#     elif dis == 0: 
#         print(" real and same roots") 
#         print(-b / (2 * a)) 
#     else:
#         print("Complex Roots") 
#         print(- b / (2 * a), " + i", sqrt_val) 
#         print(- b / (2 * a), " - i", sqrt_val)
# eq_rts(6,11,-35)

'''
Write a Python program to calculate a dog's age in dog's years. Go to the editor
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15=  -2 =*4 + 21                                  
The dog's age in dog's years is 73

dog 1 = 10.5yrs of human
dog 2 = 10.5yrs of human
first 2 yr all dogs have 21yrs
dog 3 = 10.5+10.5+4
21+ 1*4 = 25


yr-2 = x*4

def dog_age(x):
    if x>2:
        print(21+(x-2)*4)
    elif x<2 and x>0:
        print(x*10.5)
    else:
        print("invalid input")
  


age=int(input("Enter the age in human years:"))
print(dog_age(age))

'''


def func(para = "Students"):
    print("Good morning", para)
# func("Rakesh")





#parameter > arguments: default value    
#parameter < arguments: *args/**kwargs
# def names(name_lst):
#     print(name_lst)
    # for i in name_lst:
    #     print(i)
# lst = ["john","sam","smith"]


# names("john","sam","smith")


# *args/**kwargs
#*args arguments
#**kwargs keywords



def names(**person):
    print("The first name is ", person["fname"])

# names(c1="john",c3="smith",c2="sam",)
names(fname = "Steven", lname = "Smith")

'''
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
'''
# def func(x):
#     if x%3==0 and x%5==0:
#         return "FizzBuzz"
#     elif x%3==0:
#         return "Fizz"
#     elif x%5==0:
#         return "Buzz"
#     else:
#         return "x"


# myvar=int(input("Enter a number:"))
# print(func(myvar))


def modify(mylist):
    mylist[0] *= 10
    return mylist
L=[1,3,5,7,9]
M=modify(L)
print(L)
print(M)
print(M == L)


