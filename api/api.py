from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

lista_buni = [
    { "key" :  1 , "name" : "recznik", "group" : "higiena"},
    { "key" : 2 , "name" : "szczoteczka do zębów", "group" : "higiena"},
    { "key" : 3 , "name" : "mydło w płynie", "group" : "higiena"},
    { "key" : 4 , "name" : "szampon", "group" : "higiena"},
    { "key" : 5 , "name" : "pasta do zębów", "group" : "higiena"},
]

users = [
    { "id": 1 , "user" : "darek" , "lista": lista_buni}
]


@app.route("/", methods=['GET', 'POST'])
def test():
    """
    List or create notes.
    """
    if request.method == 'GET':
        return lista_buni.sort()

    # request.method == 'POST'
    return {'no hello': ' no world'}


@app.route("/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def user(id):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        # notes[key] = note
        return "a"

    elif request.method == 'DELETE':
        # notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if id not in users:
        raise exceptions.NotFound()
    return "a"




if __name__ == "__main__":
    app.run(debug=True)