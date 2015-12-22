### Laura Buchanan
### lcb402

#from restaurant_grades import *
from clean_data import *
from grade_funcs import *
import os.path
import sys

if __name__ == "__main__":
	try:
		# Load clean data
		if os.path.exists('../clean_data.csv') == True:
			data = pd.read_csv('../clean_data.csv',sep=',',header=0,low_memory=False)
	else:
		clean_data()
		data = pd.read_csv('../clean_data.csv',sep=',',header=0,low_memory=False)

	# Look at trends in grade changes and plot region by grade and year 
	regions = ['NYC','STATEN ISLAND', 'QUEENS', 'MANHATTAN', 'BRONX', 'BROOKLYN']
	for region in regions:
		grade = grades(data,region)
		grade.improve_over_region()	
		grade.count_for_bargraph()	
		grade.make_bargraph()

	except KeyboardInterrupt:
		print "\nProgram ended by user."
		sys.ext(1)

