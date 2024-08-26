'''
Write a function (using def!) that takes a number and returns True if it's even. Let's call the function is_even

Use your is_even function to return only the even numbers from the following list:

numbers = [1,56,234,87,4,76,24,69,90,135]
Now, rewrite your code to use a lambda: write the is_even code in-line, rather than defining and then using your function. Look at the slides for a hint.

Next, re-write your code to return all the odd numbers in the numbers collection.
'''
numbers = [1,56,234,87,4,76,24,69,90,135]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
even_numbers = []
# calling is_even function
# for num in numbers:
#     if is_even(num):
#         even_numbers.append(num)
        
# using lambda for is_even function
for num in numbers:
    even = lambda x: True if x % 2 == 0 else False
    if even(num):
        even_numbers.append(num) 

# Using the built-in function not and your function is_even, find another way to return all the odd numbers in the numbers collection from the previous section.
odd_numbers = []
# using not function to check for odd numbers
for num in numbers:
    even = lambda x: True if x % 2 == 0 else False
    if not even(num):
        odd_numbers.append(num)
    
        
print(even_numbers)
print(odd_numbers)