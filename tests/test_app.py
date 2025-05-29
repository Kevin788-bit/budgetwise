from app import app


def test_balance_empty():
    client = app.test_client()
    res = client.get('/balance')
    assert res.status_code == 200
    assert 'balance' in res.get_json()
