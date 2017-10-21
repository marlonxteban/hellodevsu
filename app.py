from bottle import route, run
from bottle import response
from json import dumps

@route('/hello/:name')
def index(name='World'):
    resp = { "message":"Hello "+name }
    return dumps(resp)

run(host='localhost', port=8080)