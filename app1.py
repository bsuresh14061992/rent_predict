import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import catboost

app = Flask(__name__)
model = pickle.load(open('99acres.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('99acres.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    lr=[]
    a=request.form.get("city").lower()
    b=request.form.get("deposit")
    c=request.form.get("bed")
    d=request.form.get("wash")
    e=request.form.get("area").lower()
    f=request.form.get("sq")
    g=request.form.get("type").lower()
    h=request.form.get("a1").lower()

    print(a,b,c,d,e,f,g)
    b=np.log(int(b))
    c=np.log(int(c))
    d=np.log(int(d))
    f=np.log(int(f))
    lr=[a,b,c,d,e,f,g,h]

    prediction = model.predict(lr)
    print(prediction)

    output = round(prediction, 6)
    output=np.exp(output)

    return render_template('99acres.html', prediction_text='Predicted Price {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)