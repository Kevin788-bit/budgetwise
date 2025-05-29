from flask import Flask, request, jsonify
from models import init_db, add_transaction, get_balance, get_transactions


app = Flask(__name__)
init_db()


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    add_transaction(
        data['type'],
        data['amount'],
        data['category'],
        data.get('tag')
    )
    return jsonify({'message': 'Transaction ajoutée'}), 201


@app.route('/balance', methods=['GET'])
def balance():
    return jsonify({'balance': get_balance()})


@app.route('/transactions', methods=['GET'])
def transactions():
    return jsonify(get_transactions())


if __name__ == '__main__':
    app.run(debug=True)
