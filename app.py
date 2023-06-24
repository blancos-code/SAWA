from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = ""
    if request.method == 'POST':
        text = request.form['text']
        analysis = TextBlob(text)
        sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
    return render_template('index.html', sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
