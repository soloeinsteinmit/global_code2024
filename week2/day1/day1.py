'''
maps, filters and lambda
'''
# names = ['sams', 'john', 'james']
# nam = map(len, names)
# print(list(nam))


# def too_old(x): return x > 30
# ages = [22, 25, 29, 34, 56, 24, 12]
# print(list(filter(too_old, ages)))

# def too_old(x):
#     a, b = x 
#     return a + b > 30

# ages = [(23, 3), (25, 56), (4,12), (34,2), (56,4), (24,1), (12,3)]
# print(list(filter(too_old, ages)))

# def acceptable_student(x):
#     age, class1 = x 
#     return age > 30 and class1 >= 2

# data = [(25, 1), (17, 3), (100,2)]
# print(list(filter(acceptable_student, data)))

# def acceptable_student(x):
#     age = x['age']
#     level = x['level']
#     return age > 30 and level >= 2

# data = [ {'age': 25, "level": 1}, 
#          {'age': 17, 'level':3},
#          {'age': 100,'level':2}
#         ]
# print(list(filter(acceptable_student, data)))


items = [1, 2, 3, 4, 5]
squares = map((lambda x: x ** 2), items)
print(list(squares))
