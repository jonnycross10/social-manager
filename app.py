from flask import Flask, render_template, request, redirect, url_for
from saveData import main
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('startup.html')

@app.route("/signup_page")
def signup():
    return render_template('signup.html')

@app.route("/login_page")
def to_login():
    return render_template('login.html')

@app.route("/signup/", methods = ['POST'])
def login_method():
    if request.method == 'POST':
        form_data = request.form
        user = main(form_data['Username'], form_data['Password'], is_signup=True)
        if user:
            return render_template('home.html')
        else:
            return redirect("/signup_page", code=302)

@app.route("/login/", methods = ['POST'])
def login():
    if request.method == 'POST':
        form_data = request.form
        user = main(form_data['Username'], form_data['Password'], is_signup=False)
        if user:
            return render_template('home.html')
        else:
            return redirect("/login_page", code=302)
        #return render_template('data.html',form_data = form_data)