name = input("What is your name? ")
age = input("How old are you?  ")
age = int(age)

if 0 < age < 10 : 
    print("Hello " + name + "! You are a child of " + str(age) + " years old.")
elif 10 <= age < 18:
    print("Hello " + name + "! You are a teenager of " + str(age) + " years old.")
elif age > 18: 
    print("Hello" + name + "! You are an adult and should be working on more complex stuff than this!")

else: 
    print("Enter a vilid age " + name)

# yob = "years" if int(age) > 1 else 'year'
# print(f"\nHello {name}! You are {age} {yob} old.")


