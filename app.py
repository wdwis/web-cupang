import os
import uuid
import flask
import urllib
import numpy as np 
from PIL import Image
from tensorflow.keras.models import load_model
from flask import Flask , render_template  , request , jsonify
from tensorflow.keras.preprocessing.image import load_img , img_to_array

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = load_model('model.h5')
modell = load_model('model_2.h5')

ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'JPG'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT
classes = ['HMPK', 'crowntail', 'crowntail betina', 'doubletail', 
            'doubletail betina', 'halfmoon', 'halfmoon betina', 'plakat betina', 'plakat']

def prediksi(filename, modell):
    img = load_img(filename , target_size = (224 , 224))
    img = img_to_array(img)
    img = img.reshape(1 , 224 ,224 ,3)
    img = img/255.
    h = modell.predict(img)
    if(np.argmax(h) > 3 and np.argmax(h) < 6 ):
        hasil = "cupang"
    else:
        hasil = "bukan ikan cupang"
    return hasil

def predict(filename , model):
    img = load_img(filename , target_size = (224 , 224))
    img = img_to_array(img)
    img = img.reshape(1 , 224 ,224 ,3)

    img = img/255.
    result = model.predict(img)

    pred_result = {}
    for i in range(9):
        pred_result[result[0][i]] = classes[i]

    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:3]
    
    prob_result = []
    class_result = []
    for i in range(3):
        prob_result.append((prob[i]*100).round(2))
        class_result.append(pred_result[prob[i]])

    return class_result , prob_result

@app.route('/')
def home():
        return render_template("index.html")

@app.route('/hasil' , methods = ['GET' , 'POST'])
def success():
    error = ''
    target_img = os.path.join(os.getcwd() , 'static/images')
    if request.method == 'POST':
            file = request.files["file"]
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename

                hasil = prediksi(img_path , modell)
                if(hasil == "cupang"):
                    class_result , prob_result = predict(img_path , model)

                    predictions = {
                        "class1":class_result[0],
                            "class2":class_result[1],
                            "class3":class_result[2],
                            "prob1": prob_result[0],
                            "prob2": prob_result[1],
                            "prob3": prob_result[2],
                    }
                else:
                    error = "ini bukan gambar ikan cupang"
            else:
                error = "upload gambar ikan cupang dengan format .jpg , .jpeg atau .png"

            if(len(error) == 0):
                return  render_template('hasil.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)