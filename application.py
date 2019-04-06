from flask import Flask,render_template, request, session
from flask_session import Session
app=Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)
notes=[]
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
     note =request.form.get("note")
     notes.append(note)
    return render_template("index.html",notes=notes)
    return f"Hello, {notes}"
@app.route("/more")
def more():
    return render_template('more.html')
@app.route("/yemi")
def yemi():
    username= "WELCOME TO WAL_MIKE CONSTRUCTION COMPANY"
    return render_template("index.html",username=username)
@app.route("/mikel")
def mikel():
    names=['mikel','yemi','sumbo']
    return render_template("index.html",names=names)
@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method=="GET":
        return "Please fill the form"
    else:
        name = request.form.get("name")
    return render_template("hello.html",name=name)
@app.route("/<string:name>")
def play(name):
  name = name.capitalize()
  return f"Hello,{name}"

