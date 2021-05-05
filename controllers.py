import random
from app import app
from flask import render_template, request
from models import QueueM
from datetime import datetime
from form import QueueF, DeleteForm
from flask import make_response


@app.route('/novbe', methods=['GET', 'POST'])
def delete():
    data = request.form
    print(data)

    
    user = QueueM.query.filter_by(delete_number=data).first()

    if user and request.method == 'POST':
        # if request.method == 'POST':
        form = DeleteForm(data=data, obj=user)
        if form.validate_on_submit():
            QueueM.delete(user)
            QueueM.commit()

    return render_template('novbeal.html', form=data)
    
# @app.route('/novbe', methods=['GET', 'POST'])
# def novbe():

#     return render_template('novbeal.html')

@app.route('/novbe_al', methods = ['GET', 'POST'])
def home():
    random_number = random.randint(1000000, 9999999)
    data = request.form
    form = QueueF()
    if request.method == 'POST':
        form = QueueF(data=data)
        if form.validate_on_submit():
            m = QueueM(name = form.name.data, firstname = form.firstname.data, number = form.number.data, email = form.email.data, date = form.date.data, oclock = form.oclock.data, delete_number=str(random_number))
            m.save()
    context = {
        'form': form,
        'random_number': random_number
    }

    return render_template('novbe.html', **context)
