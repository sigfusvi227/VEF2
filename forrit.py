from bottle import *
import *

@route('/')
def index():
  return "Hallo bottlepy!"
  
run(host=localhost", port=os.environ.get('PORT'))
#run(host="localhost", port=8080)
