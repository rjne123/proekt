from flask import Flask, render_template, request
import os

folder = os.getcwd()
print("templates надо создать здесь:", folder)
app = Flask(__name__, template_folder=folder)
@app.route('/1str', methods=['POST'])
def index():
    return render_template('templates/1str.html')
@app.route('/2str', methods=['POST'])
def index2():
    return render_template('templates/2str.html') 
@app.route('/3str', methods=['POST'])
def index3():
    return render_template('templates/3str.html') 
@app.route('/4str', methods=['POST'])
def index4():
    return render_template('templates/4str.html') 
@app.route('/5str', methods=['POST'])
def index5():
    return render_template('templates/5str.html') 
@app.route('/6str', methods=['POST'])
def index6():
    return render_template('templates/6str.html')
@app.route('/7str', methods=['POST'])
def index7():
    return render_template('templates/7str.html')

app.run()
