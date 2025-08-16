from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# This is what Elastic Beanstalk expects
application = app

if __name__ == '__main__':
    app.run()
