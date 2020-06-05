from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta
app = Flask(__name__)
@app.route('/')
def home():
   return render_template('index.html')
## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def write_order():
    name = request.form['name']
    numb = request.form['numb']
    adre = request.form['adre']
    tele = request.form['tele']
    order = {'name': name, 'numb': numb,'adre': adre, 'tele': tele}
    db.orders.insert_one(order)
    return jsonify({'result': 'success'})

@app.route('/order', methods=['GET'])
def read_order():
    result = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': result})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
