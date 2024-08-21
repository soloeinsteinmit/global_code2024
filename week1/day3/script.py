name = input("What is your name? ")
age = input("How old are you?  ")
yob = "years" if int(age) > 1 else 'year'
print(f"\nHello {name}! You are {age} {yob} old.")
