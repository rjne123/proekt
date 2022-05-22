from flask import Flask, render_template, request
import os

folder = os.getcwd()
print("templates надо создать здесь:", folder)
app = Flask(__name__, template_folder=folder)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('templates/Untitled-1.html')

@app.route('/program', methods=['GET', 'POST'])
def index2():
    return render_template('templates/Untitled-2.html') 
@app.route('/program1', methods=['GET', 'POST'])
def index3():
    return render_template('templates/Untitled-3.html') 
@app.route('/program2', methods=['GET', 'POST'])
def index4():
    return render_template('templates/Untitled-4.html') 
@app.route('/program3', methods=['GET', 'POST'])
def index5():
    return render_template('templates/Untitled-5.html') 
@app.route('/program4', methods=['GET', 'POST'])
def index6():
    return render_template('templates/Untitled-6.html')

app.run(host="192.168.0.28")
