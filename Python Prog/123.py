from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('yarick.html')

@app.route('/alice')
def alice():
    return render_template('alice.html')

@app.route('/java')
def java():
    return render_template('java.html')


if __name__ == '__main__':
    app.run(debug=True)