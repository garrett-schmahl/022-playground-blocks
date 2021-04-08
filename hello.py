from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/')          
def index():
    return render_template('index.html', phrase="hello", times=5)

    
@app.route('/dojo')
def success():
  return "Dojo!"


@app.route('/say/<name>')
def hello(name):
    return f"Hi {name}!"


@app.route('/repeat/<int:value>/<word>')
def show_user_profile(value, word):
    return int(value) * word

@app.route('/play')
def playground_squares():
  return render_template('playground.html', box_count = 3)


@app.route('/play/<int:value>')
def playground_squares_level_2(value):
  return render_template('playground.html', box_count = value)


@app.route('/play/<int:value>/<string:color>')
def playground_squares_level_3(value, color):
  return render_template('playground.html', box_count = value, box_color = color)


@app.errorhandler(404)
def function_name(error):
    return 'Sorry! No response. Try again.'


if __name__=="__main__":
    app.run(debug=True) 