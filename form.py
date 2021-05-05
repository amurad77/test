from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, TextAreaField, StringField,IntegerField

from wtforms.validators import DataRequired, Email, Length


class QueueF(FlaskForm):
    name = StringField(label='Enter Your Name:', validators=[DataRequired(), Length(min=3, max=20)]) 
    firstname = StringField(label='Enter Your Firstname:', validators=[DataRequired(), Length(min=3, max=30)]) 
    number = StringField(label='Enter Your Number: ', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField(label='Enter Your Email: ', validators=[DataRequired(), Length(min=3, max=50)])
    date = StringField(label='Enter the date: ', validators=[DataRequired(), Length(min=3, max=50)])
    oclock = StringField(label='Enter the clock: ', validators=[DataRequired(), Length(min=3, max=50)])

class DeleteForm(FlaskForm):
    delete_number = IntegerField(label='individual nömrəni daxil edin: ', validators=[DataRequired(), Length(min=7, max=7)])

