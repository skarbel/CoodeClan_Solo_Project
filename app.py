from flask import Flask, render_template
from controllers.champions_controller import champions_blueprint

app = Flask(__name__)

app.register_blueprint(champions_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title = "Home")

if __name__ == '__main__':
    app.run(debug=True)
