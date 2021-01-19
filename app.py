from flask import Flask,render_template,request
from flask import jsonify
from flask_mail import Mail,Message
app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465 
app.config['MAIL_USERNAME'] = "Sender mail"
app.config['MAIL_PASSWORD'] = "Sender Password"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
	return render_template("home.html")

@app.route('/send_message', methods=['GET','POST'])
def send_message():
	if request.method == "POST":
		email = request.form['email']
		subject = request.form['subject']
		#msg = request.form['message']
		a= render_template("test.html")

		message = Message(subject,sender = "koolvishruth@gmail.com",recipients=[email])
		#message.body = msg 
		message.html = a
		mail.send(message)
		success = "Message Sent"
		

		return render_template("result.html", success=success)



if __name__ == "__main__":
	app.run(debug=True)