from flexflow.keras.models import Sequential
from flexflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation
import flexflow.keras.optimizers
from flexflow.keras.datasets import cifar10

import flexflow.core as ff
import numpy as np

def top_level_task():
  
  num_classes = 10
  
  num_samples = 40000
  
  (x_train, y_train), (x_test, y_test) = cifar10.load_data(num_samples)
  
  x_train = x_train.astype('float32')
  x_train /= 255
  y_train = y_train.astype('int32')
  print("shape: ", x_train.shape)
  
  model = Sequential()
  model.add(Conv2D(filters=32, input_shape=(32,32,3), kernel_size=(3,3), strides=(1,1), padding=(1,1), activation="relu"))
  model.add(Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), padding=(1,1), activation="relu"))
  model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding="valid"))
  model.add(Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding=(1,1), activation="relu"))
  model.add(Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding=(1,1), activation="relu"))
  model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding="valid"))
  model.add(Flatten())
  model.add(Dense(512, activation="relu"))
  model.add(Dense(num_classes))
  model.add(Activation("softmax"))

  opt = flexflow.keras.optimizers.SGD(learning_rate=0.01)
  model.compile(optimizer=opt)

  model.fit(x_train, y_train, epochs=10)

if __name__ == "__main__":
  print("alexnet keras")
  top_level_task()