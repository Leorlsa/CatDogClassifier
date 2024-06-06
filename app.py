from flask import Flask, request, render_template, redirect, url_for
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
import os
import socket

app = Flask(__name__)
model = tf.keras.models.load_model('cats_dogs_model.h5')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            if not os.path.exists('uploads'):
                os.makedirs('uploads')
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            prediction = classify_image(filepath)
            return render_template('result.html', prediction=prediction)
    return render_template('upload.html')

def classify_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    if classes[0] > 0.5:
        return "É um cachorro"
    else:
        return "É um gato"


if __name__ == "__main__":
    app.run(debug=True)
