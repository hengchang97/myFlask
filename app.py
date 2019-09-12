from flask import Flask, render_template

app = Flask(__name__)
app.run(host='0.0.0.0', port = 5000)
@app.route('/')
def index():
    return render_template('hello.html')
