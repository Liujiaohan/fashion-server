from flask import Flask, request, jsonify, make_response
import os
from src.classifier.predict import predict as pd
from src.classifier.config import class_names
import numpy as np
import calendar
import time
import src.dao.dao as dao

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

@app.route('/cloth/predict', methods=['POST'])
def predict():
    file = request.files['file']
    uid = request.form['uid']
    ts = calendar.timegm(time.gmtime())
    data = {}
    filename = os.path.join(app.config['UPLOAD_FOLDER'], '{0}_{1}'.format(ts, file.filename))
    data['url'] = filename
    file.save(filename)
    predicted_class, class_index = pd(filename)
    print(predicted_class)
    data['class_name'] = int(class_index)
    id = dao.add_clothes(uid, filename, int(class_index)).inserted_id
    data['_id'] = str(id)
    response = make_response(jsonify({'status': 'ok', 'data': data}), 200)
    return response

@app.route('/cloth/update', methods=["POST"])
def update_cloth_class():
    #params = request.json if request.method == "POST" else request.args
    id = request.form['id']
    class_name = int(request.form['class_name'])
    dao.update_cloth_class(id, class_name)
    response = make_response(jsonify({'status': 'ok'}), 200)
    return response

@app.route('/cloth/delete', methods=["POST"])
def delete_cloth():
    #params = request.json if request.method == "POST" else request.args
    id = request.form['id']
    dao.delete_cloth(id)
    response = make_response(jsonify({'status': 'ok'}), 200)
    return response

@app.route('/cloth/findall', methods=["POST"])
def find_all_cloth():
    #params = request.json if request.method == "POST" else request.args
    uid = request.form['uid']
    data = []
    for class_name in range(0, len(class_names)):
        data.append({'class': class_name, 'list': dao.find_all_clothes_by_classname(uid, class_name)})
    response = make_response(jsonify({'status': 'ok', 'data': data}), 200)
    return response

if __name__ == '__main__':
    app.run()
