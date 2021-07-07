
'''
# Write a function called lastElement. This function takes one parameter (a list)
# and returns the last value in the list. It should return None if the list is empty.

# Example Output
# lastElement([1,2,3]) # 3
# lastElement([]) # None


# Write a function called returnDay. This function takes in one parameter ( a number from 1-7)
# and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater
# than 7, the function should return None.

# Expected output
# returnDay(1) --> Sunday

def returnDay(a):
  1,2 = "sunday","monday"



Q2:Convert all the characters in uppercase and lowercase and eliminate duplicate letters from a sequence
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
chasrs = [(a,A),(b,B),(e,E),(f,F),(i,I),(o,O),(u,U)]

'''
# chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
# chars1 = set(chars)
# new_lst = list(map(lambda x : ((x.upper(),x.lower())), chars1))
# print(new_lst)

# def returnday(x):
#     if(x==1):
#         return 'Sunday'
#     elif(x==2):
#         return 'Monday'
#     elif(x==3):
#         return 'Tuesday'
#     elif(x==4):
#         return 'Wednesday'
#     elif(x==5):
#         return 'Thursday'
#     elif(x==6):
#         return 'Friday'
#     elif(x==7):
#         return 'Saturday'
#     else:
#         return None
# n=int(input('Enter No:'))
# print(returnday(n))


# def returnDay(num):
#     days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
#     if num in range(1,8):
#         return days[num]
#     else:
#         return None
# print(returnDay(5))
# print(returnDay(8))

def returnday(n):
    day={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
    return day.get(n,None)

print(returnday(17))
