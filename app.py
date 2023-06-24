from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from textblob import TextBlob
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
db = SQLAlchemy(app)


class HistoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    sentiment = db.Column(db.String(50), nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods=['GET', 'POST'])
def index():
    text = request.form.get('text')
    if request.method == 'POST' and text:
        # Perform sentiment analysis
        analysis = TextBlob(text)
        sentiment_score = analysis.sentiment.polarity
        sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"

        # Save to database
        history_item = HistoryItem(text=text, sentiment=sentiment, sentiment_score=sentiment_score)
        db.session.add(history_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/history', methods=['GET'])
def get_history():
    history_items = HistoryItem.query.order_by(HistoryItem.timestamp.desc()).all()
    return jsonify([{
        'id': item.id,
        'text': item.text,
        'sentiment': item.sentiment,
        'sentiment_score': item.sentiment_score,
        'timestamp': item.timestamp
    } for item in history_items])


@app.route('/clear', methods=['POST'])
def clear_history():
    HistoryItem.query.delete()
    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/delete/<int:id>', methods=['POST'])
def delete_history_item(id):
    item = HistoryItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'status': 'success'})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
