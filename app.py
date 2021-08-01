from flask import Flask, render_template, request, redirect
from saveData import main
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/login/", methods = ['POST'])
def login():
    if request.method == 'POST':
        form_data = request.form
        user = main(form_data['Username'], form_data['Password'], is_signup=True)
        if user:
            return user
        else:
            return redirect("/", code=302)

        #return render_template('data.html',form_data = form_data)