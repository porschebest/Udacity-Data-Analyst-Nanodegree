import csv
"""
This script first use the csv library to run through the weather data extracted by sql queries and
calculate the moving averages then visualize the data through matplotlib Library
"""
year = []
temp = []
#   open global weather data
f = open('global_data_1840-2013.csv')

#   Extract data from csv to arrays
for line in f.readlines():
    year.append(line.split(',')[0])
    temp.append(line.split(',')[0])
index = 1
moving_average = [10]

for index in moving_average:
    moving_average[index] = temp[index]
