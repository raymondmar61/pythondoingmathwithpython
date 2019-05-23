#Chapter 3 Describing Data With Statistics
#Statistics mean, median, mode, range, variance, standard deviation, correlation of coefficient which allows quantifying the relationship between two sets of data, scatter plots.
#Author keeps simple using a population set of data.

shortlist = [1, 2, 3]
print(sum(shortlist)) #print 6
print(len(shortlist)) #print 3
average = sum(shortlist)/len(shortlist)
print(average) #print 2.0

def calculatemean(listofnumbers):
	total = sum(listofnumbers)
	count = len(listofnumbers)
	return total/count
donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
print(calculatemean(donations)) #print 477.75

#Median.  If the sorted count is odd, the middle numbers is the median.  If the sorted count is even, the middle number is the average of the two middle numbers.
donations = sorted(donations)
print(donations) #print [60, 70, 100, 100, 200, 500, 500, 503, 600, 900, 1000, 1200]
print(len(donations)) #print 12.  RM:  even sorted count.  Average the two middle numbers.
donationscount = len(donations)//2
donationscountminusone = donationscount-1
print([donations[donationscountminusone], donations[donationscount]]) #print [500, 503]
print("Median for sorted even is even", calculatemean([donations[donationscountminusone], donations[donationscount]])) #print Median for sorted even is even 500.0
donationstwo = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200, 800]
donationstwo = sorted(donationstwo)
print(donationstwo) #print [60, 70, 100, 100, 200, 500, 500, 503, 600, 800, 900, 1000, 1200]
print(len(donationstwo)) #print 13.  RM:  odd sorted count.
donationstwocount = len(donationstwo)
print("Median for sorted count is odd",donationstwo[round(donationstwocount//2)])  #print Median for sorted count is odd 500

#mode
mathscores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
from collections import Counter
print(Counter(mathscores)) #print Counter({9: 5, 6: 3, 7: 2, 8: 2, 10: 2, 5: 2, 1: 2, 2: 1, 4: 1})
mathscorescounter = Counter(mathscores)
#most_common(rank number) method returns a tuple.  First element is the number occuring.  Second element is the number of times it occurs.
print(mathscorescounter.most_common(1)) #print [(9, 5)]
print(mathscorescounter.most_common(1)[0]) #print (9, 5)
print("Mode most common number",mathscorescounter.most_common(1)[0][0]) #print Mode most common number 9
mathscores2 = [5, 5, 5, 4, 4, 4, 9, 1, 3]
print(Counter(mathscores2)) #print Counter({5: 3, 4: 3, 9: 1, 1: 1, 3: 1})
mathscores2counter = Counter(mathscores2)
print(mathscores2counter.most_common(1)) #print [(5, 3)]
print(mathscores2counter.most_common(1)[0][1]) #print 3
for n in mathscores2counter.most_common():
	print(n) #print (5, 3)\n (4, 3)\n (9, 1)\n (1, 1)\n (3, 1)
for n in mathscores2counter.most_common():
	if n[1] == mathscores2counter.most_common(1)[0][1]:
		print(n[0]) #print 5\n 4
def calculatemode(listofnumbers):
	modelist = []
	listofnumberscounter = Counter(listofnumbers)
	maximumnumberoftimes = listofnumberscounter.most_common(1)[0][1]
	for eachlistofnumberscounter in listofnumberscounter.most_common():
		if eachlistofnumberscounter[1] == maximumnumberoftimes:
			modelist.append(eachlistofnumberscounter[0])
	return modelist
print(calculatemode(mathscores2)) #print [5, 4]
mathscores3 = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
mathscores3 = Counter(mathscores3)
mathscores3 = mathscores3.most_common()
mathscores3.sort()
print("Frequency Table sorted")
print("Number\t Frequency")
for eachmathscores3 in mathscores3:
	print("{}\t {}".format(eachmathscores3[0], eachmathscores3[1]))
'''
Frequency Table sorted
Number	 Frequency
1	 2
2	 1
4	 1
5	 2
6	 3
7	 2
8	 2
9	 5
10	 2
'''

#Disperson.  Tells us how far away the numbers in a set of data are from the mean of the data set.  Three different measurements of dispersion:   range, variance, standard deviation.
#The range is the difference between the highest number and the lowest number.
donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
def calculaterange(listofnumbers):
	lowest = min(listofnumbers)
	highest = max(listofnumbers)
	rangenumber = highest - lowest
	return lowest, highest, rangenumber
print(calculaterange(donations)) #print (60, 1200, 1140)
print("Lowest {}, highest {}, range {}".format(calculaterange(donations)[0],calculaterange(donations)[1],calculaterange(donations)[2])) #print Lowest 60, highest 1200, range 1140
#The variance is the average of the squares of the difference of each number from the mean.  A high variance means the numbers are far from the mean.  A low variance means the numbers are close to the mean.
#variance = sigma((each data set - average data)**2)/count of data in the set.  The standard deviation is the square root of the varaince or variance**1/2  Standard deviation within one standard deviation of the mean is fairly typical.  Remember, we're working with population data.  There is an adjustment working with sample data for which I don't know at the moment.
#variance = sigma((each data set - average data)**2)/count of data in the set.
#standard deviation = variance**1/2
def calculate_mean(numbers):
	sumnumbers = sum(numbers)
	countnumbers = len(numbers)
	meannumbers = sumnumbers/countnumbers
	return meannumbers
def find_differences(numbers):
	meannumbers = calculate_mean(numbers)
	differencesfrommeanlist = []
	for eachnumbers in numbers:
		differencesfrommeanlist.append(eachnumbers-meannumbers)
	return differencesfrommeanlist
def calculate_variance(numbers):
	#find the list of differences
	differences = find_differences(numbers)
	#find the squared differences
	squaredifferences = []
	for eachdifferences in differences:
		squaredifferences.append(eachdifferences**2)
	#find the variance
	sumsquareddifferences = sum(squaredifferences)
	variance = sumsquareddifferences/len(numbers)
	return variance
donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
variance = calculate_variance(donations)
print(donations) #print [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
print("Donations mean is",calculate_mean(donations)) #print Donations mean is 477.75
print("Donations variance is",variance) #print Donations variance is 141047.35416666666
standarddeviation = variance**0.5
print("Donations standard deviation is",standarddeviation) #print Donations standard deviation is 375.5627166887931
donations2 = [382, 389, 377, 397, 396, 368, 369, 392, 398, 367, 393, 396]
variance = calculate_variance(donations2)
print(donations2) #print [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
print("Donations2 mean is",calculate_mean(donations2)) #print Donations mean is 477.75
print("Donations2 variance is",variance) #print Donations variance is 141047.35416666666
standarddeviation = variance**0.5
print("Donations2 standard deviation is",standarddeviation) #print Donations standard deviation is 375.5627166887931
#plot chart
from pylab import plot, show, legend
x1 = donations
y1 = [calculate_mean(donations) for n in range(0,len(donations))]
x2 = donations2
y2 = [calculate_mean(donations2) for n in range(0,len(donations2))]
# plot(x1)
# plot(y1)
# plot(x2)
# plot(y2)
# legend(["Donations 1","Mean 1","Donations 2","Mean 2"]) #legend() function shows legend
# show()

#Pearson correlation coefficient or correlation coefficient.  It measures the strength of the linear relationship and not a nonlinear relationship.  The coefficient is between -1 and 1 inclusive.  A 0 indicates there's no linear correlation between the two quantities; however, there could be a nonlinear relationship.  A coefficient of 1 indicates a strong positive linear correlation.  A coefficient of -1 indicates a strong negative correlation.
#Correlation doesn't imply causation.
ziplist1 = [1, 2, 3]
ziplist2 = [4, 5, 6]
for x, y in zip(ziplist1, ziplist2):
	print(x, y)
'''
1 4
2 5
3 6
'''
def correlationcoefficient(x, y):
	n = len(x)
	#find the sum of the products
	products = []
	for x1, y1 in zip(x, y):
		products.append(x1*y1)
	sumproducts = sum(products)
	sumx = sum(x)
	sumy = sum(y)
	squaredsumx = sumx**2
	squaredsumy = sumy**2

	xsquare = []
	for eachx in x:
		xsquare.append(eachx**2)
	#find the sum
	xsquaresum = sum(xsquare)
	ysquare = []
	for eachy in y:
		ysquare.append(eachy**2)
	#find the sum
	ysquaresum = sum(ysquare)

	#calculate correlation
	numerator = (n*sumproducts)-(sumx*sumy)
	denominatorterm1 = (n*xsquaresum) - squaredsumx
	denominatorterm2 = (n*ysquaresum) - squaredsumy
	denominator = (denominatorterm1*denominatorterm2)**0.5
	correlation = numerator/denominator
	return correlation
highschoolgrades1 = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
collegeadmissiontestscores1 = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
print(correlationcoefficient(highschoolgrades1,collegeadmissiontestscores1)) #print 0.3183785775683751.  Some correlation, not a strong one.  Its scatter plot shows data points not a straight line.
highschoolmathgrades = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
collegeadmissiontestscores1 = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
print(correlationcoefficient(highschoolmathgrades,collegeadmissiontestscores1)) #print 0.9989633063220916.  Strong correlation.  Its scatter plot shows data points almost a straight line.

#Scatter Plot
import matplotlib.pyplot as plt
scatterx = [1, 2, 3, 4]
scattery = [2, 4, 6, 8]
print(correlationcoefficient(scatterx,scattery)) #print 1.0
plt.scatter(scatterx, scattery)
plt.show()

#Crash course Python code read data from a text file or import text file.
with open("mydata.txt") as f:
	for eachf in f:
		print(eachf, end="") #print the numbers in mydata.txt in its own line
print("\n")
with open("mydata.txt") as f:	
	print("second with open int(eachf) instead of eachf, end=""")
	for eachf in f:
		print(int(eachf)) #print the numbers in mydata.txt in its own line
def readfile(filename):
	numberslist = []
	with open(filename) as f:
		for eachf in f:
			numberslist.append(int(eachf))
	return numberslist
#print(readfile("mydata.txt")) #print ['100\n', '60\n', '70\n', '900\n', '100\n', '200\n', '500\n', '500\n', '503\n', '600\n', '1000\n', '1200'] when numberslist.append(eachf)
print(readfile("mydata.txt")) #print [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200] when numberslist.append(int(eachf))
averagedata = readfile("mydata.txt")
print(calculatemean(averagedata)) #print 411.75.  calculatemean function above at line 11

#Crash course Python code read csv file
import csv
with open("numbers.csv") as f:
	reader = csv.reader(f)
	print(reader) #print <_csv.reader object at 0x7fec02007d68>
	next(reader)
	print(next(reader)) #print ['10', '100']
	next(reader)
	print(next(reader)) #print ['22', '484']
with open("numbers.csv") as f:
	reader = csv.reader(f)
	next(reader)
	print(reader) #print <_csv.reader object at 0x7fec02007d68>
	print(next(reader)) #print ['10', '100']
	next(reader)
	print(reader) #print <_csv.reader object at 0x7fec02007d68>
	print(next(reader)) #print ['22', '484']
with open("numbers.csv") as f:
	reader = csv.reader(f)
	next(reader)
	for eachreader in reader:
		print(eachreader[0], eachreader[1]) #print 10 100\n 9 81\n 22 484
def readcsv(filename):
	xvalues = []
	yvalues = []
	with open(filename) as f:
		reader = csv.reader(f)
		next(reader)
		for eachreader in reader:
			xvalues.append(int(eachreader[0]))
			yvalues.append(int(eachreader[1]))
		return xvalues, yvalues
x, y = readcsv("numbers.csv")
plt.scatter(x, y)
plt.xlabel("plt.xlabel Number")
plt.ylabel("plt.ylabel Square")
plt.show()