import cv2
import pandas
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os
import csv

look_back = 1
dataframe = pandas.read_csv('dataset.csv', engine='python')
dataset = dataframe.values
print(len(dataset))
# def create_dataset(dataset, look_back=1):
# 	dataX = []
# 	for i in range(len(dataset)-look_back):
# 		a = dataset[i:(i+look_back), :]
# 		dataX.append(a)
# 	return numpy.array(dataX)
# data = create_dataset(dataset)
# print(len(data))
data = dataset[(len(dataset)-1),:]
print(data)
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.predict(data)
print('Given data')
print('ETH',data[0])
print('LTC',data[1])
print('BTC',data[2])
print('XRP',data[3])
print('\nPredictions')
print('ETH',score[0][0])
print('LTC',score[1][0])
print('BTC',score[2][0])
print('XRP',score[3][0])
