"""
This is the server
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")
"""
this is the Flask app
"""
@app.route("/")
def index():
    """
    This display the webpage
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def display_emotion_detection():
    """
    This run the emotion program and display the response
    """
    text = request.args.get('textToAnalyze')
    if not text or text.strip() == "":
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'Invalid text! Please try again!'
        })


    text_emotion = emotion_detector(text)
    return jsonify(text_emotion)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5013)
