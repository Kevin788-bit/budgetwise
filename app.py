from flask import Flask, jsonify, request
from models import init_db, add_transaction, get_transactions, get_balance

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return "Bienvenue sur BudgetWise"

@app.route('/transactions', methods=['GET'])
def list_transactions():
    return jsonify(get_transactions())

@app.route('/balance', methods=['GET'])
def balance():
    return jsonify({'balance': get_balance()})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    add_transaction(
        type=data['type'],
        amount=data['amount'],
        category=data.get('category'),
        tags=data.get('tags'),
        description=data.get('description'),
        date=data.get('date')
    )
    return jsonify({'message': 'Transaction ajoutée avec succès !'})

