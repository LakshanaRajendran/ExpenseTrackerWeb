from flask import Flask, render_template, request, redirect, url_for
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)

# Temporary storage (replace with DB later)
expenses = []

@app.route("/")
def home():
    return redirect(url_for("view_expenses"))

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        description = request.form["description"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        date = request.form["date"] or datetime.today().strftime("%Y-%m-%d")

        expenses.append({
            "description": description,
            "amount": amount,
            "category": category,
            "date": date
        })

        return redirect(url_for("view_expenses"))

    return render_template("add_expense.html")

@app.route("/view")
def view_expenses():
    # Calculate total
    total_spent = sum(e["amount"] for e in expenses)

    # Aggregate totals by category
    category_totals = defaultdict(float)
    for e in expenses:
        category_totals[e["category"]] += e["amount"]

    return render_template(
        "view_expenses.html",
        expenses=expenses,
        total_spent=total_spent,
        category_labels=list(category_totals.keys()),
        category_data=list(category_totals.values())
    )

if __name__ == "__main__":
    app.run(debug=True)
