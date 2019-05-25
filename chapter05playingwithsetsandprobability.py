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
#RM:  start page 131 Probability.