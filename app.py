from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form["amount"]
    category = request.form["category"]
    date = request.form["date"]
    description = request.form["description"]
    print(amount,category,date,description)
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)