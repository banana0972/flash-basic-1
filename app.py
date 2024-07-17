from flask import Flask, render_template
import random

app = Flask(__name__)

counter = 0
secret_text = "The potatoes aren't fresh"
secret_nums = [4, 29, 43, 66, 106]
secret_info = {"Hint": "Those potatoes are fresh", "Instructions": "Cook"}

@app.route('/')
def home():
    global counter
    counter *= random.randint(0, 4)
    if counter == 0:
        counter = 0.5
    return render_template("index.html", count = counter)

@app.route("/math")
@app.route("/computing")
def computing():
    return "Computed 1+1=2"

@app.route("/random")
def rand():
    return str(random.randint(0, 999))

@app.route("/secrets")
def secret():
    number = random.choice(secret_nums)
    
    return render_template("secrets.html", number=number, info=secret_info, text=secret_text)

if __name__ == "__main__":
    app.run(debug=True)

