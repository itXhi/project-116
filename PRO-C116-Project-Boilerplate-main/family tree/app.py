# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Noah" # write your name
    age = "15" # write your age
    
    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route('/father')
def flask_father():
    name1 = "bill gates"
    age1 = "-"
    return render_template('father.html', name= name1 , age =age1)
# define the route to mother webpage
@app.route('/mother')
def flask_mother():
    name2 = "enma"
    age2="-"
    return render_template("mother.html", name =name2 , age=age2)

# define the route to friends webpage
@app.route('/friend')
def flask_friend():
    name4 = "oliver"
    age4 = "15"
    return render_template("friend.html",name =name4 , age= age4) 




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
