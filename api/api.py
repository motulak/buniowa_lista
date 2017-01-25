from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

lista_buni = [
    { "name" : "recznik", "group" : "higiena"},
    { "name" : "szczoteczka do zębów", "group" : "higiena"}
    ]

def return_element(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': lista_buni[key].name
    }

@app.route("/", methods=['GET', 'POST'])
def test():
    """
    List or create notes.
    """
    if request.method == 'GET':
        return lista_buni

    # request.method == 'POST'
    return {'no hello': ' no world'}





if __name__ == "__main__":
    app.run(debug=True)