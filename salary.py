import numpy
import re

from scipy.stats import ttest_ind
f = open('cleaned.csv').readlines()

def average(lst):
	return sum(lst)/len(lst)

datapoints = []

for line in f[1:]: #throw out header line
	point = line.split(',')[1:]
	point[-1] = re.sub('\n', '', point[-1])
	point[-1] = point[-1].strip('\r')
	point[1] = float(point[1])
	datapoints.append(point)


#now lets do things with our datapoints


#Salaries as a funciton of Age
salariesPerGroup = {}

for point in datapoints:
	if point[0] in salariesPerGroup:
		salariesPerGroup[point[0]].append(point[1])
	else:
		salariesPerGroup[point[0]] = [point[1]]


for group in sorted(salariesPerGroup, key= lambda x: int(x[:2])):
	print str(group) + ": " + "\n\tAverage: " +\
	 	  str(average(salariesPerGroup[group])) + "\n\t Standard Deviation: " +\
	 	  str(numpy.std(salariesPerGroup[group])) + "\n\t" + "Num Datapoints: " +\
	 	  str(len(salariesPerGroup[group])) + "\n"

#Salaries as a funciton of Gender
salariesPerGroup = {}
for point in datapoints:
	if point[4] in salariesPerGroup:
		salariesPerGroup[point[4]].append(point[1])
	else:
		salariesPerGroup[point[4]] = [point[1]]


for group in sorted(salariesPerGroup):
	print str(group) + ": " + "\n\tAverage: " +\
	 	  str(average(salariesPerGroup[group])) + "\n\t Standard Deviation: " +\
	 	  str(numpy.std(salariesPerGroup[group])) + "\n\t" + "Num Datapoints: " +\
	 	  str(len(salariesPerGroup[group])) + "\n"

print 't-statistic = %6.3f pvalue = %6.4f' % ttest_ind(salariesPerGroup['Male'], salariesPerGroup['Female'])

#Salaries as a funciton of full time status
salariesPerGroup = {}

for point in datapoints:
	if point[2] in salariesPerGroup:
		salariesPerGroup[point[2]].append(point[1])
	else:
		salariesPerGroup[point[2]] = [point[1]]


for group in sorted(salariesPerGroup):
	print str(group) + ": " + "\n\tAverage: " +\
	 	  str(average(salariesPerGroup[group])) + "\n\t Standard Deviation: " +\
	 	  str(numpy.std(salariesPerGroup[group])) + "\n\t" + "Num Datapoints: " +\
	 	  str(len(salariesPerGroup[group])) + "\n"

#Salaries as a funciton of degree completed
salariesPerGroup = {}

for point in datapoints:
	if point[3] in salariesPerGroup:
		salariesPerGroup[point[3]].append(point[1])
	else:
		salariesPerGroup[point[3]] = [point[1]]


for group in sorted(salariesPerGroup):
	print str(group) + ": " + "\n\tAverage: " +\
	 	  str(average(salariesPerGroup[group])) + "\n\t Standard Deviation: " +\
	 	  str(numpy.std(salariesPerGroup[group])) + "\n\t" + "Num Datapoints: " +\
	 	  str(len(salariesPerGroup[group])) + "\n"



#Salaries as a funciton of company size
salariesPerGroup = {}

for point in datapoints:
	if point[5] in salariesPerGroup:
		salariesPerGroup[point[5]].append(point[1])
	else:
		salariesPerGroup[point[5]] = [point[1]]


for group in sorted(salariesPerGroup):
	print str(group) + ": " + "\n\tAverage: " +\
	 	  str(average(salariesPerGroup[group])) + "\n\t Standard Deviation: " +\
	 	  str(numpy.std(salariesPerGroup[group])) + "\n\t" + "Num Datapoints: " +\
	 	  str(len(salariesPerGroup[group])) + "\n"

#Salaries as a funciton of location
salariesPerGroup = {}

for point in datapoints:
	if point[7] in salariesPerGroup:
		salariesPerGroup[point[7]].append(point[1])
	else:
		salariesPerGroup[point[7]] = [point[1]]


for group in sorted(salariesPerGroup):
	print str(group) + ": " + "\n\tAverage: " +\
	 	  str(average(salariesPerGroup[group])) + "\n\t Standard Deviation: " +\
	 	  str(numpy.std(salariesPerGroup[group])) + "\n\t" + "Num Datapoints: " +\
	 	  str(len(salariesPerGroup[group])) + "\n"

#Salaries as a funciton of satisfaction
salariesPerGroup = {}

for point in datapoints:
	if point[6] in salariesPerGroup:
		salariesPerGroup[point[6]].append(point[1])
	else:
		salariesPerGroup[point[6]] = [point[1]]


for group in sorted(salariesPerGroup, key = lambda x: int(x)):
	print str(group) + ": " + "\n\tAverage: " +\
	 	  str(average(salariesPerGroup[group])) + "\n\t Standard Deviation: " +\
	 	  str(numpy.std(salariesPerGroup[group])) + "\n\t" + "Num Datapoints: " +\
	 	  str(len(salariesPerGroup[group])) + "\n"
