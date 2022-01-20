
from flask import Flask,render_template,url_for,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import random

#Initialize the app
app = Flask(__name__)
#Config the app to coonect to database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Some Junk"
db = SQLAlchemy(app)

#create a table for all the posts to be stored
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(1000),unique=False,nullable=False)

    def __repr__(self) -> str:
        return f'<Book{self.title}>'
#create table 
db.create_all()
db.session.commit()

#
@app.route("/",methods=['GET','POST'])
def index():
    #if the user publishe's a new post it gets added to database
    if request.method == "POST":
        if request.form['post'] == "":
            # flash("Dont leave post space Empty!!")
            return redirect('/')
        new_post = Post(
            post = request.form['post']
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    #gets all the rows from data base and randomly selects one and displays
    data = db.session.query(Post).all()
    d = random.choice(data)
    return render_template("index.html",data=d)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
