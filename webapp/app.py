from flask import Flask, render_template, jsonify, request
import cv2
import base64
import numpy as np
from keras.models import model_from_json
import json as js
import os
from preProcessor import get_face as gf

json_file = open('..\\model\\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("..\\model\\model_weights.h5")

# Loading prediction class indices
try:
    with open(os.path.join('..', 'model', 'class indices')) as f:
        classLabel = js.load(f)
except:
    print("failed")

classLabel = {str(value): key for key, value in classLabel.items()}

with open(os.path.join("..", "config.json"), 'r') as f:
    name = js.load(f)

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def ImgData():
    dict = {}
    if request.method == "POST":
        all_data = request.get_json(force=True)
        data_url = str(all_data["image"])

        # Decoding the base64 image to cv image
        data_url = data_url.replace("data:image/png;base64,", "")
        png_original = base64.b64decode(data_url)
        png_as_np = np.frombuffer(png_original, dtype=np.uint8)
        img = cv2.imdecode(png_as_np, flags=1)

        # Decoded the imgae
        img, ans = ProcImage(img)
        string = base64.b64encode(cv2.imencode('.png', img)[1]).decode()
        dict['img'] = string
        dict['name'] = ans
    return jsonify(dict)


def ProcImage(frame):

    _, image, face = gf(frame)
    if _:
        face = face.reshape((1, 100, 100, 3))
        face = face/255
        pred = np.round(loaded_model.predict(face))
        ind = np.where(pred[0] == 1.)
        if(len(ind[0])) > 0:
            pred = name[classLabel[str(ind[0][0])]]
        if not type(pred) is str:
            pred = "Unknown"
    else:
        pred = "None"
    return (image, pred)


if __name__ == "__main__":
    app.run()
