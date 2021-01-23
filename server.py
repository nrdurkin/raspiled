import logging,json, sys, _thread
device = sys.argv[1]
if device == 'PI':
    from controller import blockColor, rgb, initCrossFade, initFairy, initStripe, main

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

    if device == "PI":
        blockColor(rgb(color))

    return "Success"

@app.route("/fade",methods=['POST'])
def handleFade():
    if device == "PI":
        initCrossFade()
    return "Success"

@app.route("/fairy",methods=['POST'])
def handleFairy():
    data = request.get_data().decode()
    data = json.loads(data)
    min_speed = float(data['minSpeed'])
    max_speed = float(data['maxSpeed'])
    count = int(data['count'])
    if device == "PI":
        initFairy(min_speed, max_speed, count)
    return "Success"

@app.route("/stripe", methods=['POST'])
def handleStripe():
    data = request.get_data().decode()
    data = json.loads(data)
    interval = float(data['interval'])
    colors = data['colors']
    if device == "PI":
        initStripe(colors, interval)
    return "Success"

if device == 'PI':
    _thread.start_new_thread(main, (0,))
app.run(host="0.0.0.0", port="8000")