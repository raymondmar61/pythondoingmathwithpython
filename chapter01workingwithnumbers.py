#Chapter 1 Working With Numbers
division = 3 / 2
floordivision = 3 // 2
print(division) #print 1.5
print("floor division //",floordivision) #print floor division // 1
modulo = 9 % 2
print("modulo for remainder",1) #print modulo for remainder 1
exponential = 2 ** 10
print("exponential",exponential) #print exponential 1024
cuberoot = 8 ** (1/3)
print("cuberoot",cuberoot) #print cuberoot 2.0
print(type(3)) #print <class 'int'>
print(type(3.5)) #print <class 'float'>
print(type(3.0)) #print <class 'float'>
print(int(3.8)) #print 3
print(int(3.0)) #print 3
from fractions import Fraction
fraction34 = Fraction(3,4)
print(fraction34) #print 3/4
print(Fraction(3,4)+1+1.5) #print 3.25
print(Fraction(3,4)+1+Fraction(1,2)) #print 9/4
print(Fraction(3,4)+1+Fraction(1,4)) #print 2
complexa = 2 + 3j
print(complexa) #print (2+3j)
print(type(complexa)) #print <class 'complex'>
#RM:  scanned complex numbers page 6-7
print("\n")

#Handling Exceptions and Invalid Input
try:
	integera = int("I'm a string")
except ValueError:
	print("ValueError a is not an integer")
try:
	dividebyzeroerror = 55/0
except ZeroDivisionError:
	print("ZeroDivisionError dividebyzeroerror divided by zero")
print("\n")

def factorfunction(factor, number):
	if number % factor == 0:
		return True
	else:
		return False
print(factorfunction(20,1000)) #return True
print(factorfunction(7,95)) #return False
for i in range(1,10,2):
	print(i) #print 1\n 3\n 5\n 7\n 9
def factors(number):
	for divisior in range(1,number+1):
		if number % divisior == 0:
			print(divisior)
factors(25) #print 1\n 5\n 25
print("\n")

fruit1 = "apples"
fruit2 = "bananas"
fruit3 = "grapes"
print("The grocery store sells {}, {}, and {}.".format(fruit1, fruit2, fruit3)) #print The grocery store sells apples, bananas, and grapes.
print("Another grocery store sells {1}, {2}, and {0}.".format(fruit1, fruit2, fruit3)) #print Another grocery store sells bananas, grapes, and apples.
print("{}".format(1.25456)) #print 1.25456
print("{0:.2f}".format(1.25456)) #print 1.25
print("{0:.2f}".format(1.25556)) #print 1.26
print("{0:.2f}".format(1)) #print 1.00
print("\n")

def print_menu():
	print("1. Kilometers to Miles")
	print("2. Miles to Kilometers")
def km_miles():
	km = float(input("Enter distance in kilometers: "))
	miles = km / 1.609
	print("Distance in miles: {0}".format(miles))
def miles_km():
	miles = float(input("Enter distance in miles: "))
	km = miles * 1.609
	print("Distance in kilometers: {0}".format(km))
# print_menu()
# choice = int(input("Which conversion would you like to do?: "))
# if choice == 1:
# 	km_miles()
# if choice == 2:
# 	miles_km()
a = 1
b = 2
c = 3
quadraticequation = (b**2 - 4*a*c)**0.5
print(quadraticequation)
print("\n")

#1: Even-Odd Vending Machine
def evenorodd(evenoddnumber):
	if evenoddnumber % 2 == 0:
		print("Even")
		for counter in range(1,11):
			print(evenoddnumber)
			evenoddnumber = evenoddnumber + 2
	else:
		print("Odd")
		for counter in range(1,11):
			print(evenoddnumber)
			evenoddnumber = evenoddnumber + 2
evenorodd(2)
'''
Even
2
4
6
8
10
12
14
16
18
20
'''
evenorodd(1)
'''
Odd
1
3
5
7
9
11
13
15
17
19
'''

#2: Enhanced Multiplication Table Generator
def multiplicationtable(number,multiples):
	for eachmultiples in range(1,multiples+1):
		print("{} X {} = {}".format(number,eachmultiples,number*eachmultiples))
multiplicationtable(9,15)
'''
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81
9 X 10 = 90
9 X 11 = 99
9 X 12 = 108
9 X 13 = 117
9 X 14 = 126
9 X 15 = 135
'''

#3: Enhanced Unit Converter
def temperature(unit,temperature):
	if unit == "c":
		celsius = (temperature - 32) * (5 / 9)
		return celsius
	if unit == "f":
		fahrenheit = temperature * (9 / 5) + 32
		return fahrenheit
print(temperature("c",98.6)) #print 37.0
print(temperature("f",37)) #print 98.60000000000001

#4: Fraction Calculator
from fractions import Fraction
print(Fraction(3/4)) #print 3/4
def fractioncalculator(operation, fraction1, fraction2):
	if operation == "add":
		return fraction1 + fraction2
	elif operation == "subtract":
		return fraction1 - fraction2
	elif operation == "multiply":
		return fraction1 * fraction2
	elif operation == "divide":
		return fraction1 / fraction2
print(fractioncalculator("add",Fraction(3,4),Fraction(1,2))) #print 5/4
print(fractioncalculator("subtract",Fraction(3,4),Fraction(1,2))) #print 1/4
print(fractioncalculator("multiply",Fraction(3,4),Fraction(1,2))) #print 3/8
print(fractioncalculator("divide",Fraction(3,4),Fraction(1,2))) #print 3/2
print(fractioncalculator("subtract",Fraction(3,4),Fraction(1,4))) #print 1/2

#RM:  skip last question #5: Give Exit Power to the User about while loop