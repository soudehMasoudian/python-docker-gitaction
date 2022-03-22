#!/usr/bin/python

import time
from flask import Flask
app = Flask(__name__)

class app:
    def elapsed():
        running = time.time() - START
        minutes, seconds = divmod(running, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)

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
        return "Hello World (Python)! (up %s)\n" % elapsed()

# if __name__ == "__main__":
app.run()
