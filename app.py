import os
from flask import Flask
app = Flask(__name__)

@app.route('/')   # URL '/' to be handled by main() route handler
def index():
    return 'Hello World!'

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=8000, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp