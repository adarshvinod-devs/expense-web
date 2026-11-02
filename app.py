from flask import Flask, render_template, request, redirect
from database import setup_database, add_expense, get_expenses

app = Flask(__name__)
setup_database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense_route():
    amount = float(request.form["amount"])
    category = request.form["category"]
    date = request.form["date"]
    description = request.form["description"]
    add_expense(amount,category,date,description)
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)