from flask import Flask,render_template,request,g
from flask import jsonify
from flask_mail import Mail,Message
import os
from flask import Flask, flash, request, redirect, url_for
app = Flask(__name__, static_url_path='/static')
app.config['TRACK_USAGE_USE_FREEGEOIP']= False
app.config['TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS']= 'include'











app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465 
app.config['MAIL_USERNAME'] = "koolvishruth@gmail.com"
app.config['MAIL_PASSWORD'] = "vishruth123456"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
picFolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
	img_girl = os.path.join(app.config['UPLOAD_FOLDER'], 'img_girl.jpg')
	return render_template("home.html", user_image = img_girl)


@app.route('/send_message', methods=['GET','POST'])
def send_message():
	if request.method == "POST":
		email = request.form['email']
		subject = request.form['subject']
		msg = request.form['message']
		img_girl = os.path.join(app.config['UPLOAD_FOLDER'], 'img_girl.jpg')
		a= render_template("test.html", user_image = img_girl)
		message = Message(subject,sender = "koolvishruth@gmail.com",recipients=[email])
		message.html = a
	 
		mail.send(message)
		success = "Message Sent"


		return render_template("result.html", success=success)




@app.route('/img')
def img_ss():
	img_girl = os.path.join(app.config['UPLOAD_FOLDER'], 'img_girl.jpg')
	return render_template("img.html", user_image = img_girl)


@app.route('/ss')



@app.route("/F") 
def image_upload():  
    msg = Message(subject = "hello", body = "hello", sender = "koolvishruth@gmail.com", recipients = ["vishruth0601@gmail.com"])  
    with app.open_resource("/Users/Vishruth/Desktop/Flask/static/pics/img_girl.jpg") as fp:  
        msg.attach("img_girl.jpg","image/png",fp.read())  
        mail.send(msg)  
    return "sent"
	
	

if __name__ == "__main__":
	app.run(debug=True)