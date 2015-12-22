### Laura Buchanan
### lcb402

import unittest
from grade_funcs import *
import os.path 

class test_grade_funcs(unittest.Testcare):
	
	test load_restaurant_data(self):
		self.assertTrue(os.path.isfile('../clean_data.csv')
		self.assertFalse(os.path.isfile('./clean_data.csv')

	test_year(self):
		self.assertTrue(len(year)==4)
		self.assrtFalse(len(year)!=4)

if __name__=='__main__':
	unittest.main()
