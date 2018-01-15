from bottle import *
import os

@route('/')
def index():
  return "Hallo bottlepy!"
  
run(host=localhost", port=os.environ.get('PORT'))
#run(host="localhost", port=8080)
