from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store expenses as a list of dicts
expenses = []

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# Add expense route
@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        expense = {
            "description": request.form["description"],
            "amount": request.form["amount"],
            "category": request.form["category"],
            "date": request.form["date"]
        }
        expenses.append(expense)
        return redirect(url_for("view_expenses"))
    return render_template("add_expense.html")

# View expenses route
@app.route("/view")
def view_expenses():
    return render_template("view_expenses.html", expenses=expenses)

if __name__ == "__main__":
    app.run(debug=True)
