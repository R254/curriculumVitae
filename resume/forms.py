from flask_wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
	name = TextField("Name", [validators.required("Please enter your Name")])
	email = TextField("Email", [validators.required("Please enter your Email"), validators.Email()])
	subject = TextField("Subject", [validators.required("Please enter a Subject")])
	message = TextAreaField("Message", [validators.required("Please enter a Message")])
	submit = SubmitField("Send")
