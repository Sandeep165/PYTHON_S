# conditional flow  if...else

'''
if (expression):  #True/False
    print{if}
else :
    print{else}

if elif else
if (expression):  #True/False
    print{if}
elif (expression): #True/False
    print{elif}
else :
    print{else}

'''

num = 10
# if num>=10:
#     print("Number is 10 or greater than 10")
# else:
#     print("Number is less than 10")


'''
AND/OR/NOT

       AND OR  NOT
1   1   1   1   0
1   0   0   1   0
0   1   0   1   0
0   0   0   0   1

'''
# num1,num2,num3 = 10,12,-5
# if num1>num2 or num2>0:
#     print("num1 is the positive number")
# else:
#     print("negative number")

#num1,num2,num3.....highest among three numb

# if (num1 > num2) and (num1 > num3):
#    largest = num1
# elif (num2 > num1) and (num2 > num3):
#    largest = num2
# else:
#    largest = num3
 
# print("The largest number is",largest)


# and / &

# num1,num2,num3 = 12,13,-1


# if num1>num2 & num1>num3 :
#     print("num1 is greatest",num1)
# elif num2>num3 & num2>num1:
#     print("num2 is greatest", num2)
# else:
#     print("num 3 is greatest",num3)

# and (expression------>True)
# &   (True/False)

# print(num1>num2 & num1>num3)     

'''
#421

1 --> 001
2 --> 010
3 --> 011
4 --> 100
5 --> 101

100 ---> 4
101 ---> 5
---
100 --->4

'''
# Write a program to check whether a person is eligible for voting or not
# Write a program to check whether a number entered by user is even or odd.
'''
 Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge amt = 0
Next 100 units   {unit>100 unit<=200}                         Rs 5 per unit
After 200 units                                             Rs 10 per unit

95 ---->0
100 --->0
101 ---> 5
150 ---> (150-100)5      {100 - 200}
201 ---> 10(201-200)     {200>}
(For example if input unit is 350 than total bill amount is 1500)
'''
# num = int(input("Enter number of unit: "))

# if num<101 :
#     print("Charge amount is Rs0")
      
# elif num>100 and num<201:
#     print("Charge amount is Rs",(num-100)*5)
           
# else:
#     print("Charge amount is Rs",(num-200)*10)

# a = int(input("input the number of units:"))
# if a<=100:
#     b=0
# elif (a>100) and (a<=200):
#     b=(a-100)*5
# else :
#     b=(a-200)*10

# print(b)


# no=int(input("enter the units"))
# if(no <=100):
#     print("the amount is 0")
# elif(no >= 101 and no <=200):
#     sub= (no -100)*5
#     print("amount is",sub)
# elif(no >=201):
#     subs =(no-200)*10
#     print("amount is ",subs)
# else:
#     print("invalid input")
'''
+
-
/  -----> normal
*
%------> 
// ----->floor

+= 
'''


# pswrd code
# 1234{last digit of the numb}
# num------------> last digit   4578 ---->8

num = 156
print(num%10)



'''
Q:-
Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not.


Q:-
Write a program to display "Hello" if a number entered by user is a multiple of five , 
otherwise print "Bye"


Q:-
Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
         > 90                                         A
         > 80 and <= 90                               B
         >= 60 and <= 80                              C
         below 60                                     D



Q:-
Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.

Note :

An equilateral triangle is a triangle in which all three sides are equal.

A scalene triangle is a triangle that has three unequal sides.

An isosceles triangle is a triangle with (at least) two equal sides.


Q:-
Accept three sides of triangle and check whether the triangle is possible or not.

(triangle is possible only when sum of any two sides is greater than 3rd side)


Q:-
Accept the marks of English, Math and Science, Social Studies Subject and display the stream allotted according to following

All Subjects more than 80 marks —       Science Stream

English >80 and Math, Science above 50 –Commerce Stream

English > 80 and Social studies > 80    —   Humanities

'''
