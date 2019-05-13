#Chapter 2 Visualizing Data With Graphs
ineednumberslist = []
ineednumberslist.append(193)
ineednumberslist.append(481)
print(ineednumberslist) #print [193, 481]
getmesecondindextuples = (5,4,8,7,6,2,19,64)
print(getmesecondindextuples[2]) #print 8
print(getmesecondindextuples[-2]) #print 19
#there's no append method for tuples.  Can't add values to an empty tuple.
rememberenumerate = [1, 2, 3]
for index, value in enumerate(rememberenumerate):
	print(index, value) #print 0 1\n 1 2\n 2 3
rememberenumerate = (1, 2, 3)
for index, value in enumerate(rememberenumerate):
	print(index, value) #print 0 1\n 1 2\n 2 3

#Matplotlib
from pylab import plot, show, legend
#three points (1,2), (2,4), (3,6)
xnumbers = [1, 2, 3]
ynumbers = [2, 4, 6]
#plot(xnumbers, ynumbers) #plot() function returns an object.
plot(xnumbers, ynumbers, marker="o") #marker= argument graphs the points
show() #show() function displays plot() function object
nycavgtemps20002012 = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nycavgtemps20002012, "*")
show() #scatterchart plotting nycavgtemps20002012 as the y-axis coordinates
# plot(nycavgtemps20002012, marker="*")
# show() #line chart plotting nycavgtemps20002012 as the y-axis coordinates
#plotting the x-axis coordinates is easy using range() function
nycavgtemps20002012 = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)
plot(years, nycavgtemps20002012, marker="*")
show()
#plot three lines on one chart
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
legend([2000, 2006, "year 2012 string"]) #legend() function shows legend
show()
#start page 40