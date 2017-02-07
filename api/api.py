from flask import request, url_for, Response, json
from flask.ext.api import FlaskAPI, status, exceptions
from data_logic import OldList
from flask_cors import CORS, cross_origin

app = FlaskAPI(__name__)
CORS(app)

users = [
    {'id': 1, 'login': 'aaa', 'pass': '123', 'name': 'Adam'},
    {'id': 1, 'login': 'bbb', 'pass': '123', 'name': 'Barbara'},
    {'id': 1, 'login': 'aaa', 'pass': '123', 'name': 'Celina'},
]


@app.route("/", methods=['GET', 'POST'])
def return_all_elements():
    """
    List or create notes.
    """
    if request.method == 'GET':
        js = json.dumps(master_list.return_elements())
        resp = Response(js,status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    # request.method == 'POST'
    return {'no hello': ' no world'}


@app.route("/get/<who>/", methods=['GET', 'PUT', 'DELETE'])
def user_elements(who):
    if request.method == 'PUT':
        return "OK"

    elif request.method == 'DELETE':
        # notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENTH

    # request.method == 'GET
    if request.headers['token']=='123':
        js = json.dumps([
            {'id': 1, 'name': 'szczoteczka do zebów', 'cat': 'kosmetyki', 'have': True, "packed": False},
            {'id': 2, 'name': 'pasta do zębów', 'cat': 'kosmetyki', 'have': True, "packed": False},
            {'id': 3, 'name': 'żel pod prysznic', 'cat': 'kosmetyki', 'have': True, "packed": False},
            {'id': 4, 'name': 'szampon', 'cat': 'kosmetyki', 'have': True, "packed": False},
            {'id': 5, 'name': 'krem do twarzy', 'cat': 'kosmetyki', 'have': True, "packed": False},
            {'id': 6, 'name': 'balsam do ciała', 'cat': 'kosmetyki', 'have': True, "packed": False},
            {'id': 7, 'name': 'antyperspirant', 'cat': 'kosmetyki', 'have': True, "packed": False},
            {'id': 8, 'name': 'szczoteczka do zebów', 'cat': 'kosmetyki', 'have': True, "packed": False},

        ])
        resp = Response(js,status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    else:
        return Response(status=403)




if __name__ == "__main__":
    app.run(debug=True)