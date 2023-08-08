from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def perform_multiplication(num1, num2):
    return num1 * num2

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = perform_multiplication(num1, num2)
    requests.post('http://localhost:5000/insert', json={
        'num1': num1,
        'num2': num2,
        'operation': 'multiply',
        'result': result
    })
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=5003)
