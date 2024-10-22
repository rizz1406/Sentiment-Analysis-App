# model/sentiment_model.py
from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route to predict sentiment
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text')
    
    if text:
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity
        
        if sentiment > 0:
            return jsonify({"sentiment": "positive"})
        elif sentiment < 0:
            return jsonify({"sentiment": "negative"})
        else:
            return jsonify({"sentiment": "neutral"})
    
    return jsonify({"error": "No text provided!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
