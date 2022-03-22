from flask import Flask
app = Flask(__name__)
    
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
    app.run()
