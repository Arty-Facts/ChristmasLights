from flask import Flask, request
from lights import Lights

app = Flask(__name__)
pixels = Lights()
num_pixels = len(pixels)

@app.route("/")
def home():
    return "use /set to set RGB colors and /clear turn of all"

@app.route("/clear", methods=['GET', "POST"])
def clear():
    pixels.clear_all()
    return "All clear"


@app.route('/set', methods=['POST'])
def set():
    for index, rgb in request.form.items():
        r, g, b = list(map(int, rgb.split(",")))
        pixels[int(index)] = (r, g, b)
    pixels.show()
    return "\n".join((f"{k}->{v}" for k,v in request.form.items()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

