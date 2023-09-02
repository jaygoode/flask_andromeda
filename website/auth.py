from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route("/login", methods = ["GET", "POST"])
def Authenticate():
    data = request.form
    return render_template("login.html", text="Testing", boolean=True)

@auth.route("/logout")
def logout():
    return "<p>logout</p>"

@auth.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method =="POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
    
        if len(email) <4: 
            flash("email must be greater than 4 characters.", category="error")
        elif len(firstName)<2:
            flash("first name must be greater than 2 characters.", category="error")
        elif password1 != password2:
            flash("passwords must match.", category="error")
        elif len(password1) < 7:
            flash("password must be greater than 7 characters.", category="error")
        else:
            #add user to DB
            flash("Account created.", category="success")

    return render_template("signup.html")