import tensorflow as tf
from  tensorflow.keras.models import Sequential
from  tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

input_shape = (28, 28, 1)

model =  Sequential([
    Conv2D(28, kernel_size=(3, 3), input_shape = input_shape),
    MaxPooling2D(pool_size = (2, 2)),
    Flatten(),
    Dense(128, activation=tf.nn.relu),
    Dropout(0.2),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10)