from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Open = float(request.form.get('Open'))
        High = float(request.form.get('High'))
        Low = float(request.form.get('Low'))
        Volume = float(request.form.get('Volume'))
    prediction = utils.preprocess(Open, High, Low, Volume)
    return render_template('prediction.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=33507)