from bottle import route, run
from bottle import response
from json import dumps

#obtencion de la IP del sistema
import socket
ip4 = socket.gethostbyname_ex(socket.gethostname())
ip4 = ip4[2][-1]

#API hello {name}
@route('/hello/:name')
def index(name='World'):
    resp = { "message":"Hello "+name}
    return dumps(resp)

#Iniciando el servidor en la ip del sistema
run(host=ip4, port=8080)