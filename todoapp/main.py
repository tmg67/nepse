from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('index.html')


@app.route('/template')
def template_example():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)