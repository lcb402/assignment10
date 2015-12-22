### Laura Buchanan
### lcb402

# This modelue cleans and saves data for easy upload later

import pandas as pd

def clean_data():
	data = pd.read_csv('../DOHMH_New_York_City_Restaurant_Inspection_Results.csv',sep=',',header=0,low_memory=False)
	extra_fields = ['DBA','BUILDING','STREET','ZIPCODE','PHONE','CUISINE DESCRIPTION','ACTION',
		'VIOLATION CODE','VIOLATION DESCRIPTION','CRITICAL FLAG','SCORE','RECORD DATE','INSPECTION TYPE']
	for i in range(len(extra_fields)):
		data = data.drop(extra_fields[i],1)
	data = data.dropna(subset = ['GRADE'])
	no_grade = ['Not Yet Graded', 'P', 'Z']
	for j in range(len(no_grade)):
		data = data[~data['GRADE'].str.contains(no_grade[j])]
	new_dates = pd.to_datetime(data['GRADE DATE'])
	data.loc[:,'GRADE DATE'] = new_dates
	data = data.sort(['GRADE DATE'])    	
	data = data.reset_index()
	data.to_csv('../clean_data.csv')
	

clean_data()
		
