#Chapter 5 Playing With Sets And Probability

#A set is a collection of distinct objects often called elements or members.  No two members of a set are the same.  In mathematical notation, a set is enclosed in curly brackets; e.g. {2, 4, 6}
from sympy import FiniteSet
from fractions import Fraction
firstset = FiniteSet(2, 4, 6)
print(firstset) #print {2, 4, 6}
secondset = FiniteSet(1, 1.5, Fraction(1, 5))
print(secondset) #print {1/5, 1, 1.5}
thirdset = FiniteSet(1, 1.5, 3)
print(len(thirdset)) #print 3
print(3 in thirdset) #print True
print(568 in thirdset) #print False
fourthset = FiniteSet()
print(fourthset) #print EmptySet()
numberslist = [1, 99, 840]
fifthset = FiniteSet(*numberslist)
print(fifthset) #print {1, 99, 840}
print(set(numberslist)) #print {840, 1, 99}
#sets ignore repeats of a member and don't keep track of the order
numberslist2 = [1, 99, 7392, 99]
sixthset = FiniteSet(*numberslist2)
print(sixthset) #print {1, 99, 7392}
for eachsixthset in sixthset:
	print(eachsixthset) #print 1\n 99\n 7392

#A set is a subset of another set if all the members are also members of the other set.  Remember, all.
seventhset = FiniteSet(999, 439, 20984)
eigthset = FiniteSet(999, 69, 48)
ninthset = FiniteSet(999, 69)
print(seventhset.is_subset(eigthset)) #print False
print(eigthset.is_subset(seventhset)) #print False
print(ninthset.is_subset(eigthset)) #print True
#A set is a superset if the set contains all of the members.  Remember, contains.
print(ninthset.is_superset(eigthset)) #print False
print(eigthset.is_superset(ninthset)) #print True

#The power set is the set of all possible subsets
tenthset = FiniteSet(20, 55, 41, 98)
print(tenthset.powerset()) #print {EmptySet(), {20}, {41}, ..., {20, 55, 98}, {41, 55, 98}, {20, 41, 55, 98}}

seventhset = FiniteSet(999, 439, 20984)
eigthset = FiniteSet(999, 69, 48)
ninthset = FiniteSet(999, 69)
print(seventhset.is_proper_subset(eigthset)) #print False
print(eigthset.is_proper_subset(seventhset)) #print False
print(ninthset.is_proper_subset(eigthset)) #print True
print(ninthset.is_proper_superset(eigthset)) #print False
print(eigthset.is_proper_superset(ninthset)) #print True

tenthset = FiniteSet(1, 2, 3)
eleventhset = FiniteSet(2, 4, 6)
print(tenthset.union(eleventhset)) #print {1, 2, 3, 4, 6}
print(tenthset.intersect(eleventhset)) #print {2}
#we can apply union and intersect to more than two sets.
tenthset = FiniteSet(1, 2, 3)
eleventhset = FiniteSet(2, 4, 6)
twelthset = FiniteSet(3, 5, 7)
print(tenthset.union(eleventhset).union(twelthset)) #print {1, 2, 3, 4, 5, 6, 7}
print(tenthset.intersect(eleventhset).intersect(twelthset)) #print EmptySet()
#The cartesian product creates a set that consists of all possible pairs made by taking an element from each set.
print(tenthset*eleventhset) #print {1, 2, 3} x {2, 4, 6}
tentheleventh = tenthset*eleventhset
for eachtentheleventh in tentheleventh:
	print(eachtentheleventh)
'''
(1, 2)
(1, 4)
(1, 6)
(2, 2)
(2, 4)
(2, 6)
(3, 2)
(3, 4)
(3, 6)
'''
#If we apply the exponential operator to a set, we get the Cartesian product of the set times itself the specified number of times.
tenthsetpowerthree = tenthset**3
print(tenthsetpowerthree) #print {1, 2, 3} x {1, 2, 3} x {1, 2, 3}
for eachtenthsetpowerthree in tenthsetpowerthree:
	print(eachtenthsetpowerthree)
'''
(1, 1, 1)
(1, 1, 2)
(1, 1, 3)
(1, 2, 1)
(1, 2, 2)
(1, 2, 3)
(1, 3, 1)
(1, 3, 2)
(1, 3, 3)
(2, 1, 1)
(2, 1, 2)
(2, 1, 3)
(2, 2, 1)
(2, 2, 2)
(2, 2, 3)
(2, 3, 1)
(2, 3, 2)
(2, 3, 3)
(3, 1, 1)
(3, 1, 2)
(3, 1, 3)
(3, 2, 1)
(3, 2, 2)
(3, 2, 3)
(3, 3, 1)
(3, 3, 2)
(3, 3, 3)
'''
print("\n")

#Uniform probability all outcomes equally likely
#Probability terms.  An experiment is the test.  An experiment is called a trial.  A sample space is all possible outcomes denoted S.  An event is a set of outcomes denoted E.  RM:  An event is the number of experiments based on the sample size.
def uniformdistributionprobability(event, samplespace):
	return len(event)/len(samplespace)
#probability roll a 3 on a six-sided die
samplespace = [1, 2, 3, 4, 5, 6]
event = [3]
print(uniformdistributionprobability(event, samplespace)) #print 0.16666666666666666
#probability roll a prime number or an odd number
samplespace = [1, 2, 3, 4, 5, 6]
primenumber = {2, 3, 5}
oddnumber = {1, 3, 5}
event = primenumber.union(oddnumber)
print(event) #print {1, 2, 3, 5}
print(uniformdistributionprobability(event, samplespace)) #print 0.6666666666666666
#probability roll a prime number and an odd number
samplespace = [1, 2, 3, 4, 5, 6]
primenumber = FiniteSet(2, 3, 5)
oddnumber = [1, 3, 5]
oddnumber = FiniteSet(*oddnumber)
event = primenumber.intersect(oddnumber)
print(event) #print {3, 5}
print(uniformdistributionprobability(event, samplespace)) #print 0.3333333333333333
#random numbers
from random import randint
print(randint(1,6)) #prints random number between 1 and 6 inclusive
def rolladicetototalscore(totalscore):
	diceroll = 0
	rollnumber = 1
	while diceroll <= totalscore:
		diceroll = diceroll + randint(1,6)
		if diceroll >= totalscore:
			return rollnumber, diceroll
		else:
			rollnumber += 1
totalscore = 20
print("Score of {} reached in {} rolls.".format(rolladicetototalscore(totalscore)[1],rolladicetototalscore(totalscore)[0])) #print Score of 20 reached in 6 rolls.  RM:  number of rolls is random diceroll = diceroll + randint(1,6)
def targetscoreprobability(sidedie, numberofrolls, targetscore):
	diesides = [n for n in range(1,sideddie+1)]
	diesides = FiniteSet(*diesides)
	#print("Dice sides",diesides)
	samplesize = diesides**numberofrolls
	#print("Sample Size",samplesize)
	successfulrolls = []  #RM:  I could use a counter for successfulrolls.  I choose to count the targetscores in a list to comprehend.
	for eachsamplesize in samplesize:	
		#print(eachsamplesize, sum(eachsamplesize))
		if sum(eachsamplesize) == targetscore:
			#print(eachsamplesize, sum(eachsamplesize))
			successfulrolls.append(eachsamplesize)
	successfuloutcomescount = len(successfulrolls)
	samplesizecount = len(samplesize)
	probability = successfuloutcomescount/samplesizecount
	return probability
sideddie = 6
numberofrolls = 5
targetscore = 25
print("Probability of exact target score {} rolling a {}-sided die {} times is {}.".format(targetscore, sideddie, numberofrolls, targetscoreprobability(sideddie,numberofrolls,targetscore)))  #print Probability of exact target score 25 rolling a 6-sided die 5 times is 0.016203703703703703.
sideddie = 20
numberofrolls = 4
targetscore = 80
print("Probability of exact target score {} rolling a {}-sided die {} times is {}.".format(targetscore, sideddie, numberofrolls, targetscoreprobability(sideddie,numberofrolls,targetscore)))  #print Probability of exact target score 80 rolling a 20-sided die 4 times is 6.25e-06.

#Nonuniform probability outcomes nonequally likely.  Draw a probability number line representing the possible outcomes.
from random import random
print(random())  #prints random floatingpoint number between 0 and 1 exclusive
#probability a coin is heads 2/3 and tails 1/3
def flipcoin():
	#2/3 heads, 1/3 tails
	coinflip = random()
	if coinflip < 2/3:
		return "Heads"
	else:
		return "Tails"
for n in range(0,19):
	print(flipcoin())
'''
Heads
Heads
Heads
Heads
Heads
Tails
Heads
Heads
Heads
Heads
Heads
Heads
Tails
Heads
Heads
Heads
Tails
Heads
Heads
'''
# dollarbills = [5, 10, 20, 50]
# probabilities = [1/6, 1/6, 1/3, 1/3]
# dollarbillsprobability = []
# initializeprobability = 0
# for p in probabilities:
# 	initializeprobability+=p
# dollarbillsprobability.append(initializeprobability)
# print(dollarbillsprobability)

def fictionalfreeatm():
	dollarbills = [5, 10, 20, 50]
	probabilities = [1/6, 1/6, 1/3, 1/3]
	dollarbillsprobability = []
	initializeprobability = 0
	for p in probabilities:
		initializeprobability+=p
		dollarbillsprobability.append(initializeprobability)
	#print(dollarbillsprobability)
	probability = random()
	for index, eachdollarbillsprobability in enumerate(dollarbillsprobability):
		#print(index, eachdollarbillsprobability)
		if probability < eachdollarbillsprobability:
			return probability, index, dollarbills[index]
atmvisits = 20
counter = 1
amountwithdrawn = 0
while counter <= atmvisits:
	withdrawal = fictionalfreeatm()
	print(withdrawal)
	amountwithdrawn+=withdrawal[2]
	counter+=1
print(amountwithdrawn)
'''
(0.10568177477900953, 0, 5)
(0.6719005340142075, 3, 50)
(0.24341150124107103, 1, 10)
(0.4094235719966657, 2, 20)
(0.6714461798290673, 3, 50)
print(amountwithdrawn)-->135
'''

