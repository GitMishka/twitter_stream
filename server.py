from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(get_latest_data())

def get_latest_data():
    # TODO: 
    pass

if __name__ == '__main__':
    app.run(debug=True)
