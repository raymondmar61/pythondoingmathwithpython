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
#customize graphs
from pylab import plot, show, legend, title, xlabel, ylabel
xyears = [2014, 2015, 2016, 2017, 2018]
ytotalexpenses = [17509.48, 19553.29, 10438.07, 10563.54, 10496.11]
plot(xyears, ytotalexpenses)
title("title() Title")
xlabel("xlabel() X Label inside quotes")
ylabel("ylabel() Y Label inside quotes")
legend(["legend() if not chart junk"])
show()
#Set minimum and maximum x-axis and y-axis
from pylab import plot, show, legend, title, xlabel, ylabel, axis
nycavgtemps20002012 = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)
plot(years, nycavgtemps20002012, marker="*")
title("New York Average Temperatures")
xlabel("Years")
ylabel("Average Temperature (F)")
legend(["legend() if not chart junk"])
axis(ymin=0, ymax=60) #RM:  no need to set xmin and xmax because x-axis is years.
show()
#If you’re changing all four values, you may find it easier to call the axis() function with all four range values entered as a list, such as axis([0, 10, 0, 20]). This would set the range of the x-axis to (0, 10) and that of the y-axis to (0, 20).

#pyplot
import matplotlib.pyplot
def create_graph():
	x_numbers = [1, 2, 3]
	y_numbers = [2, 4, 6]
	matplotlib.pyplot.plot(x_numbers, y_numbers)
	matplotlib.pyplot.title("import matplotlib.pyplot")	
	matplotlib.pyplot.show()
if __name__ == '__main__':
	create_graph()
import matplotlib.pyplot as plt
def create_graph():
	x_numbers = [1, 2, 3]
	y_numbers = [2, 4, 6]
	plt.plot(x_numbers, y_numbers)
	plt.title("import matplotlib.pyplot as plt")	
	plt.show()
	plt.savefig("mygraph.png") #save graph save chart.  Can also save graph save chart pressing Save button on window from show().
if __name__ == '__main__':
	create_graph()
#we’ll use pylab in the interactive shell and pyplot otherwise.

#Plotting With Formulas Newton's Law Of Universal Gravitation.  Use functions.
#Force F = ((Gravitational Constant G)*(First Body Mass m1)*(Second Body Mass m2))/((Distance between the two bodies r)**2)
import matplotlib.pyplot as plt
def newtondrawgraph(x, y):
	plt.plot(x, y, marker="o")
	plt.xlabel("Distance in meters")
	plt.ylabel("Gravitational force in Newtons")
	plt.title("Gravitational force and distance")
	plt.show()
def newtongeneratepoints():
	r = range(100, 1001, 50)
	F = []
	G = 6.674*(10**-11)
	m1 = 0.5
	m2 = 1.5
	for distance in r:
		force = (G*m1*m2)/(distance**2)
		F.append(force)
	newtondrawgraph(r,F)  #plot chart with r as x-values and F as y-values
if __name__ == '__main__':
	newtongeneratepoints()  #call function newtongeneratepoints() to create the x-axis points and y-axis points and graph them newtondrawgraph(x, y)