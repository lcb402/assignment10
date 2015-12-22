### Laura Buchanan
### lcb402

# This class performs analysis on restaurant grade data
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

class grades(object):
	
	def __init__(self,data,region):
		self.region = region
		if region == "NYC":
			self.data = data
		else:
			self.data = data.loc[data['BORO'] == region]
		self.restaurants = self.data['CAMIS'].unique()
		
	# The fuction sum of improvement over a region
	def improve_over_region(self):
                trend = 0
                for restaurant in self.restaurants:
			self.camis_slice = self.data.loc[self.data['CAMIS'] == restaurant]
			improve = self.test_restaurant_grades()
                        trend = trend + improve
                print "Trend in " + self.region + ":"
                print str(trend)

	# This function finds the first and last grade of a restaurant for comparison
	def test_restaurant_grades(self):
                valid_grades = ['A','B','C']
                first = self.camis_slice.iloc[0]['GRADE']
                last = self.camis_slice.iloc[-1]['GRADE']
                self.first = valid_grades.index(first)
                self.last = valid_grades.index(last)
                return self.test_grades()

	# This function compares the first and last grade for a restaurant
	def test_grades(self):
		if self.first == self.last:
			improve = 0
		elif self.first < self.last:
			improve = 1
		else:
			improve = -1
		return improve


	# This function gets values for the histogram
	def count_for_bargraph(self):
		year_list = []
		grade_list = []
		for restaurant in self.restaurants:
                        self.camis_slice = self.data.loc[self.data['CAMIS'] == restaurant]
			unique_dates = self.camis_slice['GRADE DATE'].unique()
			for d in unique_dates:
				wanted_row = self.camis_slice.loc[self.camis_slice['GRADE DATE']==d]
				wanted_row = wanted_row.head(n=1)
				grade = str(wanted_row['GRADE'])
				grade = grade[-28]
				year = str(d)
				year = year[:4]
				year_list.append(year)
				grade_list.append(grade)
		
		years = range(2011,2016)
		bar_matrix = []
		for year in years:
			year_count = 0
			my_list = []
			for i in range(len(grade_list)):
				if year_list[i] == str(year):
					my_list.append(grade_list[i])
			bar_matrix.append(my_list.count('A'))
			bar_matrix.append(my_list.count('B'))
			bar_matrix.append(my_list.count('C'))

		self.bar_matrix = bar_matrix
	


	# This function makes and saves bar graph
	def make_bargraph(self):
		# Code borrowed from: http://emptypipes.org/2013/11/09/matplotlib-multicategory-barchart/
		dpoints = np.array([['A', '2011', self.bar_matrix[0]],
           		['A', '2012', self.bar_matrix[3]],
           		['A', '2013', self.bar_matrix[6]],
           		['A', '2014', self.bar_matrix[9]],
           		['A', '2015', self.bar_matrix[12]],
			['B', '2011', self.bar_matrix[1]],	
			['B', '2012', self.bar_matrix[4]],
			['B', '2013', self.bar_matrix[7]],
			['B', '2014', self.bar_matrix[10]],
			['B', '2015', self.bar_matrix[13]],
			['C', '2011', self.bar_matrix[2]],
			['C', '2012', self.bar_matrix[5]],
			['C', '2013', self.bar_matrix[8]],
			['C', '2014', self.bar_matrix[11]],
			['C', '2015', self.bar_matrix[14]]])

		space = 0.3

		conditions = np.unique(dpoints[:,0])
		categories = np.unique(dpoints[:,1])

		n = len(conditions)

		width = (1 - space) / (len(conditions))

		for i,cond in enumerate(conditions):
    			vals = dpoints[dpoints[:,0] == cond][:,2].astype(np.float)
    			pos = [j - (1 - space) / 2. + i * width for j in range(1,len(categories)+1)]
    			plt.bar(pos, vals, width=width)
		plt.ylabel("# Grades")
		plt.xlabel("Year")
		plt.bar(pos, vals, width=width, label=cond) 
		plt.title('Grades By Year in {}'.format(self.region))
		plt.savefig('grade_improvement_{}.pdf'.format(self.region.lower()))
		plt.close()


