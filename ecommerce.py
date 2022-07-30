import requests
from flask import*
import requests
import json
import random as ran

url = 'https://fakestoreapi.com/products'

req = requests.get(url)
resp = req.json()

p = "/storage/emulated/0/Flask_T/template/"
p2 = "/storage/emulated/0/Flask_T/template/static/"

num = ran.randint(123455,997655)

app=Flask(__name__, template_folder=p, static_folder=p2)

app.secret_key = f"4tgvvt{num}"

@app.route('/')
def view():
	return render_template('home.html', data=resp)
	
@app.route('/product', methods=['POST', 'GET'])
def product():
	if request.method == 'POST':
		title = request.form['title']
		return render_template('view.html', name=title)
	return '<h4>An error occured</h4>'
	
if __name__=='__main__':
	app.run()