from flask import request, url_for, Response, json
from flask.ext.api import FlaskAPI, status, exceptions
from data_logic import OldList

app = FlaskAPI(__name__)

master_list = OldList()
master_list.initialize()





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


@app.route("/add/<id>/<group>/", methods=['GET', 'PUT', 'DELETE'])
def user(id,group):
    if request.method == 'PUT':
        master_list.add_element(id,group)
        # resp = Response('{OK}',status=200, mimetype='application/json')
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        return "OK"

    elif request.method == 'DELETE':
        # notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET
    if id not in users:
        raise exceptions.NotFound()
    return "a"




if __name__ == "__main__":
    app.run(debug=True)