# n = int(input())
# nums = list(map(int, input().split()) )  
# print(nums)
# print(sorted(set(nums))[-2])

# lst = [(206,"Sandeep","Mumbai"),(207,"Harry","Pune")]
# Id :-
# [206,207]
# Name:-
# ["Sandeep","Harry"]
# City:-
# ["Mumbai","Pune"]

# print(lst[0][2])
# print(lst[1][1])

'''
Python: Create a new list taking specific elements from a tuple and convert a string value to integer
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
Name :
[]
DOB:
[]
Weight:
[]
'''
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
name=list(map(lambda x: x[0],student_data))
dob=list(map(lambda x: x[1],student_data))
weight=list(map(lambda x: x[2],student_data))
print(f'Name:{name}\nDOB:{dob}\nWeight:{weight}')
