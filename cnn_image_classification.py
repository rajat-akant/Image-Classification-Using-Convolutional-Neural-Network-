# -*- coding: utf-8 -*-
"""CNN - Image Classification.ipynb

Automatically generated by Colaboratory.

"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
# %matplotlib inline
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import tensorflow as tf

"""Specifying the training and testing data directories"""

train_dir = "/content/drive/MyDrive/Dataset/train"
validation_dir = "/content/drive/MyDrive/Dataset/test"

from tensorflow.keras.preprocessing.image import ImageDataGenerator
# All images will be rescaled by 1./255.
train_datagen = ImageDataGenerator( rescale = 1.0/255. )
test_datagen  = ImageDataGenerator( rescale = 1.0/255. )

train_generator = train_datagen.flow_from_directory(directory=train_dir, 
                                                    target_size=(180, 180), 
                                                    color_mode='rgb', 
                                                    class_mode='binary', 
                                                    batch_size=32, 
                                                    shuffle=True, 
                                                    seed=2022)

validation_generator = test_datagen.flow_from_directory(directory=validation_dir, 
                                                        target_size=(180, 180), 
                                                        color_mode='rgb', 
                                                        class_mode='binary', 
                                                        batch_size=32, 
                                                        shuffle=True, seed=2022)

model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 150x150 with 3 bytes color
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(180, 180, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(), 
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'), 
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(1, activation='sigmoid')  
])

model.summary()

from tensorflow import keras
keras.utils.plot_model(model, "my_cnn_model.png")

from tensorflow.keras.callbacks import EarlyStopping
monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, patience=5, 
                        verbose=1, mode='auto',restore_best_weights=True)
model.compile(optimizer='adam',loss='binary_crossentropy', metrics = ['accuracy'])

history = model.fit(train_generator, validation_data=validation_generator,epochs=30,
                              verbose=2, callbacks=[monitor])

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()

test2_datagen  = ImageDataGenerator( rescale = 1.0/255. )
test_dir = "/content/drive/MyDrive/Dataset/Unclassified"
test_generator =  test2_datagen.flow_from_directory(test_dir, class_mode  = None,
                                                    target_size = (180, 180),
                                                    color_mode='rgb',
                                                    batch_size = 32,
                                                    shuffle=False)

y_prob = model.predict(test_generator,callbacks=[monitor])
print(y_prob)
y_pred = ["AS" if probs > 0.5 else "AF" for probs in y_prob]
y_pred

"""## **Saving the Model**"""

#Saving a keras model

model.save("/content/drive/MyDrive/Dataset/img_cls_cnn")
