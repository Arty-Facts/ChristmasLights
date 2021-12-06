from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "use /set to set RGB colors and /clear turn of all"

@app.route("/clear", methods=['GET', "POST"])
def clear():
    return "All clear"


@app.route('/set', methods=['POST'])
def set():
    return "\n".join((f"{k}->{v}" for k,v in request.form.items()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

