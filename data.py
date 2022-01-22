import csv
import statistics as st
import pandas as pd
f=pd.read_csv("height-weight.csv")
height_list=f["Height(Inches)"].to_list()
mean=st.mean(height_list)
print("mean is :",mean)
mode=st.mode(height_list)
print("mode is :",mode)
median=st.median(height_list)
print("median is :",median)
standard_deviation=st.stdev(height_list)
print("Standard deviation is :",standard_deviation)

std1_start,std1_end=mean-standard_deviation,mean+standard_deviation
std2_start,std2_end=mean-(2*standard_deviation),mean+(2*standard_deviation)
std3_start,std3_end=mean-(3*standard_deviation),mean+(3*standard_deviation)
print(std1_start,std1_end)
data_with_std1_deviation=[result for result in height_list if result >std1_start and
result<std1_end]

data_with_std2_deviation=[result for result in height_list if result > std2_start and
result<std2_end]

data_with_std3_deviation=[result for result in height_list if result>std3_start and
result<std3_end]
print(data_with_std1_deviation)

print("{}% of data for height lies within 1st standard deviation"
.format(len(data_with_std1_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2nd standard deviation"
.format(len(data_with_std2_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3rd standard deviation"
.format(len(data_with_std3_deviation)*100.0/len(height_list)))


