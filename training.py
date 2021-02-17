import os
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from datetime import datetime

%load_ext tensorboard

dataset_base="C:/Users/User/Desktop/face_tensorflow/human&wild/"

human_face_train = os.path.join(dataset_base,"train/","human/")
human_face_val = os.path.join(dataset_base,"val/","human/")
human_face_test = os.path.join(dataset_base,"test/","human/")

wild_face_train = os.path.join(dataset_base,"train/","wild/")
wild_face_val = os.path.join(dataset_base,"val/","wild/")
wild_face_test = os.path.join(dataset_base,"test/","wild/")

human_train=len(os.listdir(human_face_train))
human_val=len(os.listdir(human_face_val))
human_test=len(os.listdir(human_face_test))
wild_train=len(os.listdir(wild_face_train))
wild_val=len(os.listdir(wild_face_val))
wild_test=len(os.listdir(wild_face_test))
print("Number of Total Train Images= %2d" % (human_train+wild_train)) 
print("Number of Total Validation Images=%2d" % (human_val+wild_val))
print("Number of Total Test Images=%2d" % (human_test+wild_test))

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), input_shape=(128, 128, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

model.compile(optimizer=RMSprop(lr=0.001), loss='binary_crossentropy', metrics=['acc','AUC'])

TRAINING_DIR = os.path.join(dataset_base,"train/")
train_datagen = ImageDataGenerator(
    rescale=1 / 255
)
train_generator = train_datagen.flow_from_directory(
    TRAINING_DIR,
    batch_size=8,
    class_mode='binary',
    target_size=(128, 128),
    classes = ['human','wild']
)

VALIDATION_DIR =os.path.join(dataset_base,"val/")
validation_datagen = ImageDataGenerator(
    rescale=1 / 255
)
validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    batch_size=8,
    class_mode='binary',
    target_size=(128, 128),
    classes = ['human','wild']
)

logdir="logs\\model\\"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)

history = model.fit_generator(train_generator,
                              epochs=10,
                              verbose=1,
                              validation_data=validation_generator,
                              callbacks=[tensorboard_callback])
                              
%tensorboard --logdir logs
