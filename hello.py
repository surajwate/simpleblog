from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<int:pincode>')
def hello(pincode):
    return render_template('hello.html', area_code=pincode) 
