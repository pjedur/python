import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
from flask import Flask,render_template,request,redirect, url_for
from werkzeug import secure_filename
import difflib
import time

app = Flask(__name__)

#save submissions in an upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(),'uploads')#'/Users/BH/Desktop/verk5/MiniMooshak/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORRECT_OUTPUT = os.path.join(os.getcwd(),'correct.txt')
app.config['CORRECT_OUTPUT'] = CORRECT_OUTPUT

with open(CORRECT_OUTPUT,'r') as f:
	correct_answer = f.read()
	#print('correct', correct_answer)

@app.route("/",methods=['GET','POST'])
def index():
	#print(os.getcwd())
	#print('in index correct', correct_answer)
	if request.method =='POST':

		file = request.files['file']
		filename = secure_filename(file.filename)

		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		#store uploaded c++ program in uploads folder
		path_to_cpp_program = os.path.join(app.config['UPLOAD_FOLDER'],filename)

		#compile with g++ path to .cpp file compile and put executable file program in the same folder
		subprocess.call(['g++', path_to_cpp_program,'-o',os.path.join(app.config['UPLOAD_FOLDER'],'program')])
		path_to_program = os.path.join(app.config['UPLOAD_FOLDER'],'program')
		#print('progarm path: ', path_to_program)
		#delay execution to make sure the program has compiled
		time.sleep(7)
		user_answer = subprocess.check_output(os.path.join('./',path_to_program))
		#user_answer = user_answer.decode('utf-8')
		#print('user_answer:', answer)
		#print('correct_answer', correct_answer)
		
		
		


	return render_template('index.html')

if __name__ == "__main__":
    app.run()