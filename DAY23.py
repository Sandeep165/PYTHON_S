'''
Get the Area of a Country

completeformattingmathnumbersstrings
Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

Examples
area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"

area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"

area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"

Notes
The total world's landmass is 148,940,000 [Km^2]
Round the result to two decimal places.





Sort Positives, Keep Negatives
Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.

Examples
pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]

pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]

pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]

pos_neg_sort([]) ➞ []
Notes
If given an empty list, you should return an empty list.
Integers will always be either positive or negative (0 isn't included in the tests).


'''
# def pos_neg_sort(main_list):
#     sec_list = []
#     print(f"main list: \t\t{main_list}")
#     for i in range(0, len(main_list)):
#         if(main_list[i] >= 0):
#             sec_list.append(main_list[i])
    
#     sec_list.sort(reverse=False)

#     for i in range(0, len(main_list)):
#         if(main_list[i] <0):
#             sec_list.insert(i, main_list[i])
    
#     print(f"positive sorted list:   {sec_list}")


# pos_neg_sort([6, 5, 4, 0, 3, 2, -1, 1])


# def landMass(country, country_mass):
#     total_mass= 148940000
#     return "{} is {}% of total world's landmass".format(country, round((country_mass/total_mass)*100, 2))

# print(landMass("USA", 1648195))


def remove_duplicates(value):
    new = set(value)
    return "".join(new)
print(remove_duplicates("112233445698@#$"))
