from flask import Flask 
app = Flask(__name__)

@app.route('/')  # url 
def home():
    return "Hii this is home page"



if __name__ == "__main__":
    app.run(debug=True)