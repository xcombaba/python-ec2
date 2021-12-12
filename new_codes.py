#first_name = "Albert"
#last_name = "Einstein"
#full_name = f'{first_name} {last_name} once said, "A person who never made a mistake never tried anything new." '
#print(full_name)

#names = ["Peter", "Paul", "John", "Jade", "Josh"] 
#for name in names:
    #print(name)
#names.insert(0, "Pete")
#names.append("Dre")
#names.append("Bola")
#del names[3]

#print(names)
#print(names[2].lower()) 
#print(10 > 2)
#print(10 < 2)
#print((10 > 2) and (9 < 4))

#course = 'Python for Me'
#print(course.replace ('for', "4"))
#print(not("Python" in course))

#number = 0

#if number > 4:
    #print(f"{number} is positive")
#elif number ==0:
    #print(f"{number} is zero")
#else:
    #print(f"{number} is negative")
    
#numbers = [1, 2, 3, 4, 5, 200, 400]
#numbers.append(100)
#numbers.remove(2)
#print(numbers.pop())

#result = 0
#numbers = [1, 2, 3, 4, 5, 6, 7]
#for number in numbers:
    #result += number
#print(result)

#number = 0

#while number < 10:
    #print(number)
    #number +=1
    
#Function
#def greet():
    #print("Hello how are you?")
#greet()

#great = "Hello how una dey?"
#print(great)

#Argument
#def holla(name):
    #print(f"Hello {name}, how was your night")
#holla("Peter")
#holla("Paul")

#import math
#print(math.pi)
#print(math.isqrt(125))

#file = open("./data.txt", "r")
#file.write("id, name, add\n")
#file.write("1, Josh, Skokie\n")
#file.write("2, Paul, Chicago\n")
#file.write("3, Pete, Evaston\n")
#print(file.read())
#file.close()

#students = ["Paul", "Josh", "Raul", "Bola"]
#for name in students:
    #print(f"Hello {name.title()}, you are all invited to my party")
    #print(f"I cant wait having you {name.title()}!\n")
#print("Thank you all for coming, it was great fun")

#cars = ["Toyota", "Benz", "Audi", "Telsa", "Range"]
#print(sorted(cars))
#print(len(cars))

#for value in range(0, 10, 2):
    #print(value)

#squares = [value**2 for value in range(1, 11)]
#print(squares)

#digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(sum(digits))

#players = ["Rashford", "CR7", "Pogba", "Cavani", "Burno", "Degea"]
#print("Here are the list of our first three players")
#for player in players[0: 3]:
    #print(player)
#players.append("Nani")
#print("My favorite players are:")
#print(players)
#united_players = players[:]
#united_players.append("Carrick")
#print("My favorite players are:")
#print(united_players)

#dimensions = (200, 50)
#print(dimensions[0])

#dimension = [200, 50]
#dimension[0] = 150
#print(dimension)

#age = int(input("What is your age: "))
#if age >= 18:
    #print("You are eligible to vote, Congrats!!!")
    #print("Have you registered yet?")   
#else:
    #print("You are not eligible to vote, sorry!!!!")
    #print("Wait till you are Age 18 to register")
    
#age = int(input("Entrance fee age: "))
#if age < 4:
    #print("Your admission fee is $0")
#elif age < 8:
    #print("Your admission fee is $25")
#else:
    #print("Your admission fee is $40")

age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
print(f"Your admission cost is ${price}")
    
    
    