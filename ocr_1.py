## video link https://www.youtube.com/watch?v=u3FLVbNn9Os

## LOADING THE DATA
import tensorflow as tf
mnist=tf.keras.datasets.mnist
(X_train,y_train),(X_test,y_test)=mnist.load_data()

## CHECKING THE SHAPE.
X_train.shape

import matplotlib.pyplot as plt
plt.imshow(X_train[0])
plt.show()
plt.imshow(X_train[0],cmap=plt.cm.binary)

print(X_train[0]) #Printing the binaraies insted of the image.

# Normalizing the values.
X_train=tf.keras.utils.normalize(X_train,axis=1)
X_test=tf.keras.utils.normalize(X_test,axis=1)
plt.imshow(X_train[0],cmap=plt.cm.binary)

print(X_train[0]) #Printing the binaraies insted of the image after normalization.

print(y_train[0]) #Checking the corresponding label.

# rehshaping into a two dimensional array for numpy.
import numpy as np
IMG_SIZE=28
X_trainr=np.array(X_train).reshape(-1,IMG_SIZE,IMG_SIZE,1)
X_testr=np.array(X_test).reshape(-1,IMG_SIZE,IMG_SIZE,1)
print(X_trainr.shape)  #Checking the shape now
print(X_testr.shape)   #Checking the shape now

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPooling2D

model=Sequential()
#FIRST CONVUTIONAL LAYER
# model.add(Conv2D(64,(3,3),input_shape=X_trainr.shape[1:]))
model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=X_trainr.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

#SECOND CONVUTIONAL LAYER
model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=X_trainr.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

#THIRD CONVUTIONAL LAYER
model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=X_trainr.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

#FLATTENING
model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))

model.add(Dense(32))
model.add(Activation("relu"))

model.add(Dense(10))
model.add(Activation("softmax"))

model.summary() #Checking out the summary.

print(len(X_trainr)) #Checking the length of the list.

model.compile(loss ="sparse_categorical_crossentropy",optimizer="adam",metrics=['accuracy'])

model.fit(X_trainr,y_train,epochs=5,validation_split=0.3) #training the data model

test_loss,test_acc=model.evaluate(X_testr,y_test)
print(test_loss) #the loss
print(test_acc)  #the accuracy

predictions=model.predict([X_testr])

print(predictions)

print(np.argmax(predictions[0]))

plt.imshow(X_test[0])

import cv2

img=cv2.imread('images.png')

plt.imshow(img)

img.shape

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

resized=cv2.resize(gray,(28,28),interpolation= cv2.INTER_AREA)

resized.shape

newimg= tf.keras.utils.normalize(resized,axis=1)

newimg = np.array(resized).reshape(-1,IMG_SIZE,IMG_SIZE,1)

newimg.shape

predictions=model.predict(newimg)

print(np.argmax(predictions))
