from functools import reduce

total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
# print(total)

# Write a function called join_strings that takes a list of words and uses + to join them all together. For example:

words = ['Hello', ' world']
# function to join_stings using +
def join_string(list_of_words):
    sentence = ""
    for i in list_of_words:
        sentence += i
    return sentence
    
# print(join_string(words))

# using reduce for join_string
def join_string1(list_of_words):
    sentence = reduce(lambda word, sentence: word + sentence, list_of_words)
    return sentence

print(join_string1(words))