'''

Create a function that takes a string and censors words over four characters with *.

Examples
censor("The code is fourty") ➞ "The code is ******"

censor("Two plus three is five") ➞ "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word.

'''

'''

Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.

Examples
return_end_of_number(553) ➞ "553-RD"

return_end_of_number(34) ➞ "34-TH"

return_end_of_number(1231) ➞ "1231-ST"

return_end_of_number(22) ➞ "22-ND"

return_end_of_number(412) ➞ "412-TH"

'''

# def ordinal(num):
#     n = int(num)
#     if n > 100:
#       suffix = 'th'
#     elif 4 <= n <= 20:
#       suffix = 'th'
#     elif n == 1 or (n % 10) == 1:
#       suffix = 'st'
#     elif n == 2 or (n % 10) == 2:
#       suffix = 'nd'
#     elif n == 3 or (n % 10) == 3:
#       suffix = 'rd'

#     ord_num = str(n) + suffix
#     return ord_num

# def ordinal(num):
#     n = int(num)

#     if 4 <= n <= 20 or (n%10) == 2:
#       suffix = 'th'
#     elif n == 1 or (n % 10) == 1:
#       suffix = 'st'
#     elif n == 2 or (n % 10) == 2:
#       suffix = 'nd'
#     elif n == 3 or (n % 10) == 3:
#       suffix = 'rd'

#     ord_num = str(n) + suffix
#     return ord_num

# print(ordinal(412))


'''
A consecutive-run is a list of adjacent, consecutive integers. This list can be either increasing or decreasing.
 Create a function that takes a list of numbers and returns the length of the longest consecutive-run.

To illustrate:

longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
# Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).
Examples
longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
# Longest consecutive-run: [1, 2, 3].

longest_run([5, 4, 2, 1]) ➞ 2
# Longest consecutive-run: [5, 4] and [2, 1].

longest_run([3, 5, 7, 10, 15]) ➞ 1
# No consecutive runs, so we return 1.
Notes
If there aren't any consecutive runs (there is a gap between each integer), return 1.

'''

