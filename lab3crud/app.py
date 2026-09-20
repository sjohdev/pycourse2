# CRUD webapp example: 

# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/") # decorator for function get_transactions()
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if (request.method == 'POST'):
        transaction  = {'id': len(transactions)+1, 'date': request.form['date'], 'amount': float(request.form['amount'])
                    }
        transactions.append(transaction)
        return redirect(url_for("get_transactions"))
    else:
        return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if (request.method == 'POST'):
        date = request.form['date']
        amount = float(request.form['amount'])
        
        for i in range(0, len(transactions)):
            item = transactions[i]
            if (item['id'] == transaction_id):
                item['date'] = date
                item['amount'] = amount
                transactions[i] = item
                return redirect(url_for("get_transactions"))
        
        # If the user inputs an id is not in the list: 
        return ({"message": "Transaction not found"}, 404)
    else:
        for transaction in transactions:
            if (transaction['id'] == transaction_id):
                return render_template('edit.html', transaction=transaction)
            
        # If the user inputs an id thats not in the list: 
        return ({"message": "Transaction not found"}, 404)
    
# Delete operation
@app.route('/delete/<int:transaction_id>', methods=['GET'])
def delete_transaction(transaction_id):
    for i in range(0, len(transactions)):
        item = transactions[i]
        if (item['id'] == transaction_id):
            transactions.pop(i)
            return redirect(url_for("get_transactions"))
    return ({"message": "Transaction not found"}, 404)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
