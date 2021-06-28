# # ternary operator   
# num1 = 450
# num2 = 470
# num3 = 400

# # if num1>num2:
# #     print("A")
# # elif num2>num1:
# #     print("B")
# # else:
# #     print("C")

# # {if} condition /{elif} condition /else{}

# # print("A") if num1>num2 else print("B") if num1< num2 else print("C")
# print(f"{num1} is greater") if(num1>num2 and num1>num3) else print(f"{num2} is greater") if(num2>num3) else print(f"{num3} is greater")


# loops inside the python
# while  /   for loop

'''
i ---> init
while (condition):
    {while}
    counter/false!
'''

i = 1

# while (i<210):
#     print(i%2 == 0)
#     i += 1

# break
# while i <6:
#     print(i)
#     if i == 3:
#         break
#     print(i)
#     i += 1

#pass
# while i < 10:
#     # print(i)
#     if i == 5:
#         pass
#     print(i)
#     i+=1

#continue
# while i < 8:
#     # print(i)
#     if i ==3:
#         continue
#     print(i)
#     i+=1


# count = 1
# while i<4:
#     print("inside the loop...")
#     i+=1

# print("outside the loop/.")


i = 1
sum = 0
n = 10


while i<=n:
    sum = sum +i  #1...#3...#55
    i+=1

print("The sum is :", sum)