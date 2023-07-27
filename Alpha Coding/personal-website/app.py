from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hobbies')
def hobbies():
    return "I like to swim and hike!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
