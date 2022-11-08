import random

greetings = ('Hey', 'Hello', 'Good Morning', 'Hi')
name = input("What is your name? ").title()
greeting = random.choice(greetings)
print(greeting +', ' + name)