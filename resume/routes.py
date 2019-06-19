import os
from flask import render_template, url_for, request, flash
from resume import app
#from resume.forms import ContactForm

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/about')
def about():
	return render_template('about.html', title="About")

'''@app.route('/contact', methods = ['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required')
			return render_template('contact.htm', form=form)
		else:
			msg = Message(form.subject.data,sender =form.email.data, recipients=[os.environ.get('EMAIL_USER')])
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			return render_template('contact.htm', success=True)
	elif request.method == 'GET':
		return render_template('contact.htm', form=form)'''