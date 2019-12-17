import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import matplotlib.pyplot as plt

from src.classifier.model import create_model
from src.classifier.config import *
from src.classifier.utils import *

def predict(path):

    test_image = load_image(path)
    print(test_image.shape)
    test_image = np.expand_dims(test_image, 0)
    test_image /= img_bis
    print(test_image.shape)
    model = create_model()
    model.load_weights(saved_model_filename)

    predictions = model.predict(test_image)
    print(class_names[np.argmax(predictions[0])])

    # test_images = test_image
    # test_labels = [0]
    # i = 0
    # plt.figure(figsize=(6,3))
    # plt.subplot(1,2,1)
    # plot_image(i, predictions[i], test_labels, test_images)
    # plt.subplot(1,2,2)
    # plot_value_array(i, predictions[i],  test_labels)
    # plt.show()

    return np.argmax(predictions[0])

# predict('img_predict/yundongxie.jpeg')