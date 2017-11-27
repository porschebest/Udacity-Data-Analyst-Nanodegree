import csv
import numpy as np
import matplotlib.pyplot as plt
"""
This script first use the csv library to run through the weather data extracted by sql queries and
calculate the moving averages then visualize the data through matplotlib Library
"""


#   global_data
year = []
temp = []
mov_avg = []

#   open csv and extract data
def extract_csv(filepath=''):
    #   open global weather data
    f = open(filepath)
    #   Extract data from csv to arrays
    for line in f.readlines():
        if(line.split(',')[0] != 'year'):
            temp1 = line.split(',')[1]
            temp1 = temp1.replace('\n','')
            year1 = line.split(',')[0]
            year1 = year1.replace("\'","")
            temp.append(temp1)
            year.append(year1)
    print("extract csv success")
extract_csv('global_data_1841-2013.csv')

#   calculate moving averages
def moving_average(year=[],temp=[]):
    i = 0
    avg_temp = 0
    last_num = len(year) - 10
    while i < last_num:
        avg_temp = (float(temp[i]) + float(temp[i+1]) + float(temp[i+2]) + float(temp[i+3])
        + float(temp[i+4]) + float(temp[i+5]) + float(temp[i+6]) + float(temp[i+7]) + float(temp[i+8]) + float(temp[i+9]))/9
        avg_temp = round(avg_temp, 2)
        mov_avg.append('\"'+year[i+9]+'\"'+','+'\"'+str(avg_temp)+'\"'+','+'\n')
        i += 1
moving_average(year,temp)

#   save the moving average to csv
def save_csv(filepath):
    f = open(filepath, 'w')
    f.writelines(mov_avg)
    print("save csv success")
    f.close()
save_csv('moving_avg_global.csv')

#   city_data_Taipei




#   plot line chart
year_int = []
temp_float = []
for item in year:
    year_int.append(int(item))
for item in temp:
    temp_float.append(float(item))
plt.xticks(np.arange(min(year_int)-1,max(year_int)+7,20.0))
plt.yticks(np.arange(min(temp_float),max(temp_float)+1,0.5))
plt.plot(year_int,temp_float)
plt.ylabel('temperature')
plt.xlabel('year')
plt.title('Global Temperature Data 1840-2013')
plt.show()
