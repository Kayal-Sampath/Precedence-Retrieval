import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
#import keras.backend as K
import numpy as np
data_train = np.loadtxt('r_cnn_input.csv', delimiter=',')
    #print(type(data))
#    x_train, y_train = mmr_fea_train()
x_train=data_train[:,0:3774]
#data_train1 = np.loadtxt('datalabel_cnn_train.csv', delimiter=',')
y_train=data_train[:,3774]
data_test = np.loadtxt('ir_cnn_input.csv', delimiter=',')
#    x_train, y_train = mmr_fea_train()
x_test=data_test[:,0:3774]
#data_test1 = np.loadtxt('datalabel_cnn_test.csv', delimiter=',')
y_test=data_test[:,3774]
x_train = np.expand_dims(x_train, axis=2) # reshape (569, 30) to (569, 30, 1) 
x_test = np.expand_dims(x_test, axis=2) # reshape (569, 30) to (569, 30, 1) 
    
model = Sequential()
model.add(Conv1D(32, 6, activation='relu', input_shape=(3774,1), use_bias=True,kernel_initializer='random_normal', 
                    bias_initializer='zeros',name="conv1"))
    
model.add(Conv1D(32, 6, activation='relu', use_bias=True,kernel_initializer='random_normal', 
                    bias_initializer='zeros',name="conv2"))
    
model.add(MaxPooling1D(6,name="max_pool"))
model.add(Conv1D(64, 6, activation='softmax', use_bias=True,kernel_initializer='random_normal', 
                    bias_initializer='zeros',name="conv3"))
    
model.add(Conv1D(64, 6, activation='softmax', use_bias=True,kernel_initializer='random_normal', 
                    bias_initializer='zeros',name="conv4"))
model.add(GlobalAveragePooling1D(name="avg_pool"))
model.add(Dropout(0.3,name="dropout"))
model.add(Dense(1, activation='relu',name="relu_dense"))
#model.add(Dense(1 , activation = 'softmax',name="softmax_dense"))
#model.add(Dense(1, activation='sigmoid',name="sigmoid_dense"))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
    
model_train=model.fit(x_train, y_train, batch_size=12, epochs=10, validation_data=(x_test,y_test))
score = model.evaluate(x_train, y_train, batch_size=10)
print('Training Loss:', score[0])
print('Training Accuracy:', score[1])
model_json=model.to_json()
with open("model14.json","w") as json_file:
    json_file.write(model_json)
model.save_weights('model14.h5')
print("Saved model")
        
    # later...
score = model.evaluate(x_test, y_test, batch_size=12)
print ('')
print('Test Score: ', score[0])
print('Test Accuracy:', score[1])

import numpy
from keras.models import Model
intermediate_layer_model=Model(inputs=model.input,outputs=model.get_layer('conv4').output)
intermediate_output = intermediate_layer_model.predict(x_train)
intermediate_output1 = intermediate_layer_model.predict(x_test)
file1=open("intermediate_relevant.txt","w")
numpy.set_printoptions(threshold=numpy.nan)
file1.write(str(intermediate_output))
file2=open("intermediate_relevant.txt","w")
file2.write(str(intermediate_output1))


