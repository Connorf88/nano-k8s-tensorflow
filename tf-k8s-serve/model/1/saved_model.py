import tensorflow as tf
import numpy as np

# Build and train a simple model
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(4,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Dummy training data
x_dummy = np.random.rand(100, 4)
y_dummy = np.random.randint(0, 3, 100)
model.fit(x_dummy, y_dummy, epochs=2)

# Export to correct path
model.save("/Users/connorfleming/tf-k8s-serve/model/1")

