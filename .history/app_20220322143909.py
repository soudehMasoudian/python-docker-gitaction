#!/usr/bin/python

import time
from flask import Flask
app = Flask(__name__)

class app:
    
    def sum(arg):
        total = 0
        try:
            for val in arg:
                total += val
        except Exception:
            return "Error occured!", 500
        return total


    @app.route('/')
    def root():
        return "Hello World (Python)! (up %s)\n"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
