from flask import Flask, request

app = Flask(__name__)


user_list = [
  { "id": 34740842, "handle": "sawahh" },
  { "id": 89083932, "handle": "brianna10" },
  { "id": 84431295, "handle": "ronnie20" },
  { "id": 50487240, "handle": "jay3" },
]

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'POST':
        return create_user()
    return user_list

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id): 
    for  x in user_list:
        if x['id'] == id:
            return x
    return {'message': 'User not found'}, 404

@app.route('/users', methods=['POST'])
def create_user():
    request_data = request.get_json()
    user_list.append(request_data)
    return user_list

@app.route('/users/handle/<string:handle>', methods=['GET'])
def get_handle(handle):
    for x in user_list:
        if x['handle'] == handle:
            return x
        return {'message': 'Handle not found'}
        
app.run()