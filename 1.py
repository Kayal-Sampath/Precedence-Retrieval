import tensorflow as tf
tf.reset_default_graph()
import pandas as pd
import numpy as np
from tensorflow.contrib import rnn
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score
data = pd.read_csv('data_cnn_train.csv', skiprows=[0], header=None)
features = data.iloc[:, 1:1023]
labels = data.iloc[:, 1023]
X_train,X_test,y_train,y_test = train_test_split(features, labels, test_size=0.2, shuffle=False, random_state=42)
epochs = 3
n_classes = 1
n_units = 200
n_features = 1022
batch_size = 35
xplaceholder= tf.placeholder('float',[None,n_features])
yplaceholder = tf.placeholder('float')
f1=0.0
accuracy=0.0
recall=0.0
precision=0.0
def recurrent_neural_network_model():
    layer ={ 'weights': tf.Variable(tf.random_normal([n_units, n_classes])),'bias': tf.Variable(tf.random_normal([n_classes]))}
    x = tf.split(xplaceholder, n_features, 1)
    #print(x)
    lstm_cell = rnn.BasicLSTMCell(n_units)
    outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)
    output = tf.matmul(outputs[-1], layer['weights']) + layer['bias']
    return output

logit = recurrent_neural_network_model()
logit = tf.reshape(logit, [-1])
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit, labels=yplaceholder))
optimizer = tf.train.AdamOptimizer().minimize(cost)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    tf.local_variables_initializer().run()
    for epoch in range(epochs):
        epoch_loss = 0
        i = 0
        for i in range(int(len(X_train) / batch_size)):
            start = i
            end = i + batch_size
            batch_x = np.array(X_train[start:end])
            batch_y = np.array(y_train[start:end])
            f={xplaceholder: batch_x, yplaceholder: batch_y}
            _, c = sess.run([optimizer, cost], f)
            epoch_loss += c
            i += batch_size
        print('Epoch', epoch, 'completed out of', epochs, 'loss:', epoch_loss)
    lr=tf.round(tf.nn.sigmoid(logit))
    pred =lr.eval({xplaceholder: np.array(X_test), yplaceholder: np.array(y_test)})
    f1 = f1_score(np.array(y_test), pred, average='macro')
    accuracy=accuracy_score(np.array(y_test), pred)
    recall = recall_score(y_true=np.array(y_test), y_pred= pred)
    precision = precision_score(y_true=np.array(y_test), y_pred=pred)

    print("F1 Score:", f1)
    print("Accuracy Score:",accuracy)
    #print("Recall:", recall)
    #print("Precision:", precision)