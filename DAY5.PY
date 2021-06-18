#List :- [0......n-1]
'''
1) capable to hold multiple data type
2) Duplications are allowed inside the list
3) List mutable data type
4) Orderd, changable and duplication are allowed
'''

my_list = [1,2,3,"Pune","Mumbai",True,False,15.5,1,2,3]

# print(my_list[-1])

# print(len(my_list))  #11(1---n)

# print(my_list[len(my_list)-1])

# print(type(my_list))

# print(my_list[0:3])


#nested list

my_list1 = [1,2,3,4,5,["mumbai","pune","delhi"],True,["Python"],False]

print(len(my_list1)) #8
print(my_list1[5][2])#delhi
# print(my_list1[-3][0])#mumbai
# print(my_list1[-3][-1])#delhi
print(my_list1[-2][0])



my_countries = ["mumbai","pune",[400078,4000081,4000095,400051],["USA","JAPAN","AUS",["MEXICO"]],"NASHIK","DELHI"]
# 400095,Mexico,delhi,AUS

print(my_countries[2][-2],my_countries[-3][-1][0],my_countries[-1],my_countries[-3][-2])



my_fruits = ["apple","mango",[[1,2,3,4],"hello_world"],"grapes"]
# 3, hello_world
print(my_fruits[2][0][2])
print(my_fruits[2][1])



list1 = [["harry","john"],1,4,6,9,["India"],400078]
# 9 , india, john
print(list1[4], list1[5][0], list1[0][1])


