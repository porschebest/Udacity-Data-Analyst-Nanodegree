import csv
import numpy as np
import matplotlib.pyplot as plt
"""
This script first use the csv library to run through the weather data extracted by sql queries and
calculate the moving averages then visualize the data through matplotlib Library
"""
year = []
temp = []
mov_avg = []

#   open global weather data
f = open('global_data_1840-2013.csv')

#   Extract data from csv to arrays
for line in f.readlines():
    if(line.split(',')[0] != 'year'):
        temp1 = line.split(',')[1]
        temp1 = temp1.replace('\n','')
        year1 = line.split(',')[0]
        year1 = year1.replace("\'","")
        temp.append(temp1)
        year.append(year1)

#   calculate moving averages
i = 0
avg_temp = 0
last_num = len(year) - 10
while i < last_num:
    avg_temp = (float(temp[i]) + float(temp[i+1]) + float(temp[i+2]) + float(temp[i+3])
    + float(temp[i+4]) + float(temp[i+5]) + float(temp[i+6]) + float(temp[i+7]) + float(temp[i+8]) + float(temp[i+9]))/9
    avg_temp = round(avg_temp, 2)
    mov_avg.append('\"'+year[i+9]+'\"'+','+'\"'+str(avg_temp)+'\"'+','+'\n')
    i += 1

#   save the file to new csb
f = open('moving_avg_global.csv', 'w')
f.writelines(mov_avg)
print("write success")
f.close()

#   plot line chart
year_int = []
temp_float = []
for item in year:
    year_int.append(int(item))
print(year_int)
for item in temp:
    temp_float.append(float(item))
plt.xticks(np.arange(min(year_int)-1,max(year_int)+7,20.0))
plt.yticks(np.arange(min(temp_float),max(temp_float)+1,0.5))
plt.plot(year_int,temp_float)
plt.ylabel('temperature')
plt.xlabel('year')
plt.title('Global Temperature Data 1840-2013')
plt.show()
