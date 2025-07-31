from flask import flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/emotionDetector")
def display_emotion_detection():
    text = request.args.get["testToAnalyze"]
    text_emotion = emotion_detector(text)

    show_response = {
    "anger": text_emotion['anger'], 
    "disgust": text_emotion['disgust'], 
    "fear": text_emotion['fear'],
    "joy": text_emotion['joy'], 
    "sadness": text_emotion['sadness'], 
    "dominant_emotion": text_emotion['dominant_emotion']
    }

    return show_response