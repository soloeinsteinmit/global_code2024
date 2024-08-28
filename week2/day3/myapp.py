from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return 'Name: Florence Oforiwaa Anarfi Age: 20 Hobby: Coding'


@app.route('/whereami')
def whereami():
    return 'Ghana!'

@app.route('/thename/<name>')
def thename(name):
    #print(name)
    return render_template('myname.html', thename = name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
