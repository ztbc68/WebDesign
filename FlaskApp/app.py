#This is the entry file, like index.html
#First we should import Flask
#Next we import render_template to manage templates (need a templates/ folder)
from flask import Flask, render_template
#Import flask-bootstrap
from flask_bootstrap import Bootstrap

app = Flask(__name__) #__name__ = Placeholder for current module
#attach bootstap
Bootstrap(app)

#Use routes to define directories
@app.route('/')
def index():
	# return 'Index' Normally don't return a string
	return render_template('index.html') #Normally return a template

#Run the app
if __name__ == '__main__':
	app.run(debug=True) #Deubug is set to true

