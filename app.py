import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    target = os.environ.get('TARGET', 'HELLO THIS IS')
    return 'Hello {}!\n'.format(target)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
