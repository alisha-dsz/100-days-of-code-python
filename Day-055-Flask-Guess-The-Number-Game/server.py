from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home_page():
    return "<body style='background-color:#E5CD82'>"\
    "<h1 style='text-align:center; font-family:Arial'>Guess a number between 0 and 9</h1>"\
    "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjdyaGQ4ajR3OTV6NmNvcjV4bDYxZjdxZmlmajg0bGFyNWd2M3NrYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/nTZt1E0IM8sKSEVirG/giphy.webp' style='display:block; margin:auto; width:400'>"\
    "</body>"

random_number = random.randint(0,9)

@app.route('/<int:number>')
def guess(number):
    if number > random_number:
        return "<body style='background-color:#FFA97B'>"\
        "<h2 style='text-align:center; font-family:Arial; color:red'>Too high, try again :(</h2>"\
        "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGxhZ3BoZWR1d3k0bHkyZ2dtajlxNm04eXRxdDl5Mm44MHVxMTBrZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/28UMYUOhdbOzAVtKiK/giphy.webp' style='display:block; margin:auto; width:400'>"\
        "</body>"
    elif number < random_number:
        return"<body style='background-color:#FFA97B'>"\
        "<h2 style='text-align:center; font-family:Arial; color:red'>Too low, try again :(</h2>"\
        "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWRpeWV2NTRmaXQxbmg1dXB2b3c3ZTd6ZWJ0b21lOTRtNmdzZmZ1dSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qzTEbvfPgBOR8nvEUn/giphy.webp' style='display:block; margin:auto; width:400; height:420'>"\
        "</body>"
    else:
        return "<body style='background-color:#9FED72'>"\
        f"<h2 style='text-align:center; font-family:Arial; color:green'>Hurray, {number} is the correct answer!</h2>"\
        "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzU0M2JmemJzcjZuMmhhaWV6ZXowajBna3A3MTI2emdydjYybGZ3ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/AhskBO7JKGNY93IzVt/giphy.webp' style='display:block; margin:auto; width:400; height:420'>"\
        "</body>"

if __name__ == "__main__":
    app.run(debug=True)