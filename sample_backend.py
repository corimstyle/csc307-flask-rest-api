from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

users = {
    'users_list':
    [
        {
            'id': 'xyz789',
            'name': 'Charlie',
            'job': 'Janitor',
        },
        {
            'id': 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id': 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id': 'yat999',
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id': 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        return _get_user(request)
    elif request.method == 'POST':
        return _post_user(request)
    elif request.method == 'DELETE':
        return _delete_user(request)

def _get_user(request):
    # accessing the value of parameter 'name'
    search_username = request.args.get('name')
    search_job = request.args.get('job')
    if search_username:
        subdict = {'users_list': []}
        for user in users['users_list']:
            if user['name'] == search_username:
                if search_job:
                    if user['job'] == search_job:
                        subdict['users_list'].append(user)
                else:
                    subdict['users_list'].append(user)
        return subdict
    return users

def _post_user(request):
    user_to_add = request.get_json()
    users['users_list'].append(user_to_add)
    resp = jsonify(success=True)
    # resp.status_code = 200 # optionally, you can set a response code
    # 200 is the default code for a normal response
    return resp

def _delete_user(request):
    user_to_delete = request.get_json()
    try:
        users['users_list'].remove(user_to_delete)
        resp = jsonify(success=True)
    except ValueError:
        resp = jsonify(success=False)
        resp.status_code = 404
    return resp

@app.route('/users/<id>')
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})
    return users
