import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import matplotlib.pyplot as plt

from src.classifier.model import create_model
from src.classifier.config import *
from src.classifier.utils import *

model = load_model()

def predict(path):

    test_image = load_image(path)
    #test_image = np.expand_dims(test_image, 0)
    #test_image /= img_bis


    predictions = model.predict(test_image)

    sorted_rate = np.argsort(predictions[0])
    predict_class = []
    for i in range(1,predictions.size):
        predict_class.append(class_names[sorted_rate[-i]])

    print(predict_class)

    # test_images = test_image
    # test_labels = [6]
    # i = 0
    # plt.figure(figsize=(6,3))
    # plt.subplot(1,2,1)
    # plot_image(i, predictions[i], test_labels, test_images)
    # plt.subplot(1,2,2)
    # plot_value_array(i, predictions[i],  test_labels)
    # plt.show()

    return predict_class

#predict('img_predict/yundongxie.jpeg')