from bottle import *
import os

@route('/')
def index():
  return "Hallo bottlepy!"
  
run(host="0.0.0.0", port=os.environ.get('PORT'))
#run(host="localhost", port=8080)
