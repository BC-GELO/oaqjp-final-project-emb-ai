from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", ["GET", "POST"])
def display_emotion_detection():
    text = request.args.get["testToAnalyze"]
    text_emotion = emotion_detector(text)

    show_response = {
    f'"anger": {text_emotion["anger"]},' 
    f'"disgust": {text_emotion["disgust"]},'
    f'"fear": {text_emotion["fear"]},'
    f'"joy": {text_emotion["joy"]},'
    f'"sadness": {text_emotion["sadness"]},'
    f'"dominant_emotion": {text_emotion["dominant_emotion"]}'
    }

    return show_response

if __name__ == '__main__':
    app.run(debug=True)