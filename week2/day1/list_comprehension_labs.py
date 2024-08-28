'''
5: List comprehensions
'''

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
n = []
[n.append(len(word)) for word in words]

# print(n)

# Create a list out of only the positive numbers from this list:
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
pos_numbers = []
[pos_numbers.append(num) for num in numbers if num > 0]
# print(f"list of positive numbers are -> {pos_numbers}")


# Create a list containing only the even numbers from this list:
numbers1 = [12, 54, 33, 67, 24, 89, 11, 24, 47]
even_numbers = []
[even_numbers.append(num) for num in numbers1 if num % 2 == 0]
# print(f"list of even numbers are -> {even_numbers}")



# Create a list containing tuples of the uppercase version and the length of the following words:
words1 = ["hello", "my", "name", "is", "Sam"]
uppercase_length = []
[uppercase_length.append((word.upper(), len(word))) for word in words1 ]

print(f"list of uppercase version and length are -> {uppercase_length}")

