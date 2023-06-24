from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sentiments.db'
db = SQLAlchemy(app)

class Sentiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = ""
    if request.method == 'POST':
        text = request.form['text']
        analysis = TextBlob(text)
        sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
        new_sentiment = Sentiment(text=text, sentiment=sentiment)
        db.session.add(new_sentiment)
        db.session.commit()
    return render_template('index.html', sentiment=sentiment)

@app.route('/history', methods=['GET'])
def history():
    sentiments = Sentiment.query.order_by(Sentiment.timestamp).all()
    return jsonify([{'text': s.text, 'sentiment': s.sentiment, 'timestamp': s.timestamp} for s in sentiments])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

