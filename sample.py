from flask import Flask
app =Flask(__name__)
@app.route('/')
def sample():
  return"welcome to my world"
if__name__=='__main__':
  app.run(debug=True)
