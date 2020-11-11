from flask import Flask, render_template, request, redirect
from flask.helpers import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<int:pincode>')
def hello(pincode):
    return render_template('hello.html', area_code=pincode) 

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        first_name = request.values.get('first_name')
        last_name = request.values.get('last_name')
        return redirect(url_for('registered'))
    return render_template('form.html')

@app.route('/thank_you')
def registered():
    return 'Thank You!'
