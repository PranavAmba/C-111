import pandas as pd
import csv
import random
import statistics as stx
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('studentMarks.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([data],['Math_score'],show_hist=False)
fig.show()

mean=stx.mean(data)
standard_deviation=stx.stdev(data)

print('Mean of data: ',mean)
print('Standard deviation of data: ',standard_deviation)


dataset=[]
for i in range (0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)

mean= stx.mean(dataset)
std_dev=stx.stdev(dataset)

print('mean_of_sample',mean)
print('standard_deviation_of_sample',std_dev)

#go to find the mean of 100 datapoints 1000 times and plot it

def ramdom_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean= stx.mean(dataset)
    return mean