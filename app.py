from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from config import sqlalchemy_connection

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_connection()
db = SQLAlchemy(app)

# database table creation
class student_data(db.Model):
    roll_no = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
    std = db.Column(db.Integer(),nullable=False)
    medium = db.Column(db.String(100),nullable=False)
    city = db.Column(db.String(100),nullable=False)

# get endpoint
@app.route('/', methods=['GET'])
def index():   
    # GET tha datas from Database
    data = student_data.query.all()

    # pass the datas from database to html file
    return render_template('index.html',data=data)

# post endpoint
@app.route('/post_data',methods=['GET','POST'])
def post_data():
    print("method",request.method)
    if request.method == 'POST':
        # get the datas from from in frontend
        name = request.form.get('name')
        std = request.form.get('std')
        medium = request.form.get('medium')
        city = request.form.get('city')

        # post the datas to database
        data = student_data(name=name,std=std,medium=medium,city=city)
        print("data", data)
        db.session.add(data)
        db.session.commit()
        return redirect('/')
    
    return render_template('post_data.html')

# update endpoint
@app.route('/update_data/<int:id>',methods=['GET','POST','PUT'])
def update_data(id):
    print("method",request.method)
    user_update = student_data.query.get_or_404(id)
    if request.method == "POST":
        name = request.form.get('name')
        std = request.form.get('std')
        medium = request.form.get('medium')
        city = request.form.get('city')
        user_update.name = name
        user_update.std = std
        user_update.medium = medium
        user_update.city = city
        db.session.commit()
        return redirect('/')
    return render_template('update_data.html',user_update=user_update)

# delete endpoint
@app.route('/delete_data/<int:id>',methods=['GET'])
def delete_data(id):
    print("method",request.method)
    user_delete = student_data.query.get_or_404(id)
    db.session.delete(user_delete)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)