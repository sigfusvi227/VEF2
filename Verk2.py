from bottle import *
import os

@route('/stafir/<skra>')
def static_skrar(skra):
    return static_file(skra, root='stafir')

@route('/')
def index():
    return "<h2>Verkefni 2</h2> <br><a href=/a>Liður a</a> <a href='/b'>Liður b</a>"

@route('/a')
def index():
    return "<h2>Verkefni 2A </h2><br> <a href='/sida/1'>Síða 1</a> <a href='/sida/2'>Síða 2</a> <a href='/sida/2'>Síða 3</a>"

@route('/sida/<id>')
def index(id):
    return "Þetta er sida ", id, "<br> <a href='/a'>Til baka</a>"
@route('/b')
def index():
    return "<h2>Verkefni 2B</h2> <h3>Veldur þinn uppáhalds bókstaf</h3> <a href='/sida2?stafur=a'> <img src='stafir/a.png'></a> <a href='/sida2?stafur=b'><img src='stafir/b.png'></a> <a href='/sida2?stafur=c'><img src='stafir/c.png'></a>"

@route("/sida2")
def index():
    x = request.query.stafur
    if x == "a":
        return "<h2> Minn uppáhalds bókstafur er: <h2> <br> <img src='stafir/a.png'><img>"
    if x == "b":
        return "<h2> Minn uppáhalds bókstafur er: <h2> <br> <img src='stafir/b.png'><img>"
    if x == "c":
        return "<h2> Minn uppáhalds bókstafur er: <h2> <br> <img src='stafir/c.png'><img>"


@error(404)
def villa(error):
    return "<h2>Þessi síða er ekki til, reyndu aftur</h2>"

run(host="0.0.0.0", port=os.environ.get('PORT'))
#run(host="localhost", port=8080)
