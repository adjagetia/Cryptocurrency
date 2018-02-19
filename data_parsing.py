import numpy
import pandas
import math
import csv
import os

# fix random seed for reproducibility
numpy.random.seed(7)
dataset = []

# load the dataset
eth = pandas.read_csv('eth-usd-max.csv', usecols=[1], engine='python')
data_eth = eth.values
data_eth = data_eth.astype('float32')
# print(len(data_eth))
# print(data_eth.shape)
t1 = data_eth

ltc = pandas.read_csv('ltc-usd-max.csv', usecols=[1], engine='python')
data_ltc = ltc.values
data_ltc = data_ltc.astype('float32')
# print(len(data_ltc[(len(data_ltc)-len(data_eth)):]))
t2 = data_ltc[(len(data_ltc)-len(data_eth)):]

btc = pandas.read_csv('btc-usd-max.csv', usecols=[1], engine='python')
data_btc = btc.values
data_btc = data_btc.astype('float32')
# print(len(data_btc[(len(data_btc)-len(data_eth)):]))
t3 = data_btc[(len(data_btc)-len(data_eth)):]

xrp = pandas.read_csv('xrp-usd-max.csv', usecols=[1], engine='python')
data_xrp = xrp.values
data_xrp = data_xrp.astype('float32')
# print(len(data_xrp[(len(data_xrp)-len(data_eth)):]))
t4 = data_xrp[(len(data_xrp)-len(data_eth)):]

# dataset = list(zip(t1, t2, t3, t4))
dataset = numpy.column_stack((t1,t2,t3,t4))
# dataset = numpy.reshape(dataset, (len(data_eth),4))
# dataset = numpy.ndarray.tolist(dataset)
print(numpy.shape(dataset))

with open("dataset.csv", "w") as f:
    writer = csv.writer(f)
    for row in dataset:
        writer.writerow(row)
