'''
Write a Python class for a Person. The person should inherit from Object and have the following methods:

A constructor which takes the persons name and date of birth
speak() - prints "hello"
walk() - prints "walking away"
get_name() - returns the person's name
get_age() - returns the person's age

Write another class called Student. Student inherits from Person and has the following methods:

The constructor also takes a String List of course names
get_courses() - returns the course list
speak() - in the subclass, prints "I'm so tired!"

'''
from datetime import datetime



class Person:
    # constructor
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def speak(self):
        print("Hello")
    
    def walk(self):
        print("walking away")
        
    def get_name(self):
        return self.name
        
    def get_age(self):
        # Get the current date and time
        now = datetime.now()

        # Extract the year from the current date
        current_year = now.year
        return f" You are {current_year - self.dob} of age"
    

class Student(Person):
    def __init__(self, *course_name):
        self.course_names = course_name
        
    def get_courses(self):
        return list(self.course_names)
    
    # method overriding
    def speak(self):
        print("I'm so tired!")
    