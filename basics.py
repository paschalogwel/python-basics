import datetime
import time
import os
import pandas

print("The date and time is")
print(datetime.datetime.now())

myname = "paschal"
myage = 20
print(myname, myage)

x = 10
y = "20"
z = 30.1

sum1 = x+x
sum2 = y+y
sum3 = z+z
print(sum1, sum2, sum3)
print(type(x), type(y), type(z))

# lists and dictionaries

student_grades1 = [8.5, 9.9, 10]
student_grades = {"paschal": 7, "ogwel": 8, "otieno": 9.5}
test = list(range(1, 11, 2))
print(test)

mysum = sum(student_grades.values())
length = len(student_grades.values())
mean = mysum/length
print(mysum, length, mean)


def average(value):
    if type(value) == dict:
        myaverage = sum(value.values()) / len(value)
    else:
        myaverage = sum(value) / len(value)
    return myaverage

print(average(student_grades))

def area(dimensions):
    square = dimensions[0]*dimensions[1]
    return square
    
print(area([30, 20]))

def weather(temperature):
    if 10 < temperature < 50 :
        return "warm"
    elif temperature > 50:
        return "hot"
    else:
        return "cold"

user_input = float(input("Enter the temperature:"))
print (weather(user_input))

# string formatting
my_input = input("Enter your name:")
message = f"Hello {my_input}!"
message = "Hey %s!" % my_input
print(message)

name = input("Enter your name:")
surname = input("Enter your surname")
Greetings = f"Hello {name} {surname}"
Greetings = "Hello %s %s" % (name, surname)
print(Greetings)

for grades in student_grades1:
    print(round(grades))

for temp in student_grades1:
    print(weather(temp))

for names in student_grades.keys():
    print(names)

#username = ""
#while username != "pie":
 #   username = input("Enter your username:")

def sentence(phrase):
    interrogatives = ("How", "When", "What", "Why", "Who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#print(sentence("Who darkness"))

results = []
while True:
    avatar = input("Say something:")
    if avatar == "/end":
        break
    else:
        results.append(sentence(avatar))
print(" ".join(results))

temps = [223, 345, 778, -9999, 234]
new_temps = [tempest / 10 if tempest != -9999 else 0 for tempest in temps]
print(new_temps)

#while True:
 #   if os.path.exists("fruits.txt"):
   #     with open("fruits.txt") as myfile:
   #         print(myfile.read())
    #else:
  #      print("file does not exist")
   # time.sleep(10)

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean())
    else:
        print("file does not exist")
    time.sleep(10)