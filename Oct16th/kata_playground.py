"""
Persistent Bugger.
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative 
persistence, which is the number of times you must multiply the digits in num until you reach a single 
digit.

For example:
 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.
 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.
"""
from functools import reduce
def persistence(n):
    # Way to keep track of the multiplied digits
    # Way to keep track of the number of loops
    # Check if the length of the number is one
    count = 1
    def digit_reducer(n)

        multiplied_number = 1
        length = len(str(n))
        if length > 1:
            for digit_string in str(n):
                digit = int(digit_string)
                multiplied_number *= digit
            count += persistence(multiplied_number)
            
        return count

print(persistence(999))
print(persistence(12345))