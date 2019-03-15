from flask import Flask, render_template,request,abort

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/r',methods = ['POST','GET'])
def home1():
	if request.method == 'GET':
	    return render_template("registration.html")
	elif request.method == 'POST':
		aa = {
			'email': request.form['email'],
			'firstname':request.form['firstname'],
			'lastname':request.form['lastname'],
		}
		return render_template('formo.html', **aa)

@app.route('/err')
def home2():
    abort(401)


if __name__ == '__main__':
    app.run(debug=True)