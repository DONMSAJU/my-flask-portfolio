from flask import Flask, render_template

app = Flask(__name__)
application = app  # Beanstalk looks for "application"

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Bind to 0.0.0.0 and port 8080 for Elastic Beanstalk
    application.run(host='0.0.0.0', port=8080)
