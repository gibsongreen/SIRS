import tensorflow as tf
from tensorflow import keras
import pathlib
import numpy as np
from shutil import copyfile

model = keras.models.load_model('THIS IS WHERE THE model.h5 FILE PATH GOES')

class_names = ['nonsprite', 'sprite']

#this is temporary, counts amount of sprites found in Raw_Data and it'll save it with this name
sprite_counter = 1

img_height = 180
img_width = 180

data_dir = pathlib.Path('THIS IS WHERE THE Raw_Data FILE PATH GOES')
for sprite in data_dir.glob('*.jpg'):

    img = keras.preprocessing.image.load_img(
    sprite, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
    
    #this is where the destination file path goes
    destination = "/home/gibsongreen/Desktop/Sprites_Found/{}.jpg".format(sprite_counter)
    
    if np.argmax(score) == 1:
    	x += 1
    	copyfile(sprite, destination)
        #copyfile(sprite, 'found_sprites' + str(sprite)[str(sprite).find('/'):])
