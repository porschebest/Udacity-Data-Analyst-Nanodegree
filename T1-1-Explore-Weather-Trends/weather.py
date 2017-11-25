import csv
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
        temp.append(temp1)
        year.append(line.split(',')[0])

#   calculate moving averages
i = 0
avg_temp = 0
last_num = len(year) - 10
while i < last_num:
    avg_temp = (float(temp[i]) + float(temp[i+1]) + float(temp[i+2]) + float(temp[i+3])
    + float(temp[i+4]) + float(temp[i+5]) + float(temp[i+6]) + float(temp[i+7]) + float(temp[i+8]) + float(temp[i+9]))/9
    mov_avg.append(year[i+9] + ',' + str(avg_temp))
    i += 1

#   save the file to new csb
f = open('moving_avg.csv', 'w')
f.writelines(mov_avg)
print("write success")
f.close()
