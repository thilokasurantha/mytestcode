from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login() :
    if request.method == "POST" :
        fname = request.form["finame"]
        lname = request.form["lname"]
        passw = request.form["pass"]

        return redirect(url_for("home", usr=fname, bsr=lname))

    else :
        return render_template("index.html")

@app.route("/<usr>%<bsr>")
def home(usr, bsr) :
    return f"<h1>Fname : {usr}, Lname : {bsr}</h1>" 

if __name__ == "__main__" :
    app.run(debug=True)