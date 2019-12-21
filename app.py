from flask import Flask, request, jsonify, make_response
import os
from src.classifier.predict import predict as pd
from src.classifier.config import class_names
import numpy as np
import calendar
import time

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = os.path.basename('data')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
H = 28
W = 28

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return 'Boy Fashion!'

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    ts = calendar.timegm(time.gmtime())
    filename = os.path.join(app.config['UPLOAD_FOLDER'], '{0}_{1}'.format(ts, file.filename))
    file.save(filename)
    predicted_class = pd(filename)
    print(predicted_class)
    response = make_response(jsonify({'class_name': list(predicted_class)}), 200)
    return response

if __name__ == '__main__':
    app.run()
