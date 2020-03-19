import pandas as pd
import numpy as np


"""file_read = pd.read_csv('ak.csv')
df = pd.DataFrame(file_read )
print(df.isnull())

df4 = df.copy()
df4.fillna(0,inplace=True)

##rDroping the Empty Columns

#print(df4.columns)
#NUMBER UNIT CITY DISTRICT REGION ID 

file_new =  df4.drop(['NUMBER','UNIT', 'CITY', 'DISTRICT', 'REGION' ,'ID'],axis=1)
#print(file_new)
file_new.to_csv('final_data')

###################################

#importing the Final Data_csv File Which is clean of Nan's

"""
data = pd.read_csv('final_data', dtype = str)

##getting the longitude and latitude from the csv
Lat = []
for i in data['LAT']:
    Lat.append(i)
Long = []
for i in data['LON']:
    Long.append(i)
#print(Lat)
#print(Long)

#Converting two Lists using zip function and coverting it into a dictionary.

usable_dict_for = dict(zip(Lat,Long))
data_trial = pd.DataFrame(usable_dict_for,index = [0])
print(data_trial)
"""usable_list = list(usable_dict_for)
#print(usable_list)

#Unique Identification Numbers
list_of_Identification_numbers = []

for i in range(0,len(usable_list)-1):
    list_of_Identification_numbers.append(i)


list_to_use = dict(zip(list_of_Identification_numbers,usable_list))
#print(list_to_use)

data_bagu = pd.DataFrame(usable_list,index=list_of_Identification_numbers)
data_tri = pd.DataFrame(usable_list)
print(data_tri)
"""