import logging,json

from controller import blockColor, rgb

from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='',static_folder='public', template_folder='public')

logging.getLogger('werkzeug').setLevel(logging.ERROR)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/color", methods=['POST'])
def handleColor():
    data = request.get_data().decode()
    data = json.loads(data)
    color = data['color']

    blockColor(rgb(color))

    return "Success"

app.run(host="0.0.0.0", port="8000")
