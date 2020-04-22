from flask import Flask, render_template
app=Flask(__name__)
app.run(debug=True)
@app.route("/")
def home_function():
    return render_template("home.html")
