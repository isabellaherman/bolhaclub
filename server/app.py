from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/js/scripts.js')
def javascript():
    return send_from_directory(app.static_folder, 'js/scripts.js')

@app.route('/css/styles.css')
def css():
    return send_from_directory(app.static_folder, 'css/styles.css')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)