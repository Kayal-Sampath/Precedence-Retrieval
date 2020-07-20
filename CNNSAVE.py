#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 08:45:46 2018

@author: pglab1-uni2
"""

import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
#import keras.backend as K
import numpy as np
#from keras.models import model_from_json
#import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('Agg')


def cnn():
    data_train = np.loadtxt('data_cnn_train.csv', delimiter=',')
    #print(type(data))
#    x_train, y_train = mmr_fea_train()
    x_train=data_train[:,0:1023]
#data_train1 = np.loadtxt('datalabel_cnn_train.csv', delimiter=',')
    y_train=data_train[:,1023]
    data_test = np.loadtxt('data_cnn_test.csv', delimiter=',')
#    x_train, y_train = mmr_fea_train()
    x_test=data_test[:,0:1023]
#data_test1 = np.loadtxt('datalabel_cnn_test.csv', delimiter=',')
    y_test=data_test[:,1023]
    

    x_train = np.expand_dims(x_train, axis=2) # reshape (569, 30) to (569, 30, 1) 
    x_test = np.expand_dims(x_test, axis=2) # reshape (569, 30) to (569, 30, 1) 
    
    model = Sequential()
    model.add(Conv1D(32, 6, activation='relu', input_shape=(1023,1), use_bias=True,kernel_initializer='random_normal', 
                    bias_initializer='zeros'))
    
    model.add(Conv1D(32, 6, activation='relu', use_bias=True,kernel_initializer='random_normal', 
                    bias_initializer='zeros'))
    
    model.add(MaxPooling1D(6))
    model.add(Conv1D(64, 6, activation='relu', use_bias=True,kernel_initializer='random_normal', 
                    bias_initializer='zeros'))
    
    model.add(Conv1D(64, 6, activation='relu', use_bias=True,kernel_initializer='random_normal', 
                    bias_initializer='zeros'))
   
    model.add(GlobalAveragePooling1D())
    model.add(Dropout(0.3))
    model.add(Dense(1, activation='sigmoid'))
    #model.add(Dense(2 , activation = 'softmax'))
    model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
    
    model_train=model.fit(x_train, y_train, batch_size=12, epochs=10, validation_data=(x_test,y_test))
    score = model.evaluate(x_train, y_train, batch_size=12)
    print('Training Loss:', score[0])
    print('Training Accuracy:', score[1])
        
    # later...
    score = model.evaluate(x_test, y_test, batch_size=12)
    print ('')
    print('Test Score: ', score[0])
    print('Test Accuracy:', score[1])
model1 = cnn()
