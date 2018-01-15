from bottle import *
import os

@route('/')
def index():
  return "<a href='/About'>About</a> <a href='/Biography'>Biography</a> <a href='/Pictures'>Pictures</a>"
@route('/About')
def index():
  return "Hér eru upplýsingar um Steve Jobs"
@route('/Biography')
def index():
  return "Hér er Biography frá Steve Jobs"
@route('/Pictures')
def index():
  return "Hérna eru myndir frá lífi Steve Jobs"


  
#run(host="0.0.0.0", port=os.environ.get('PORT'))
run(host="localhost", port=8080)
