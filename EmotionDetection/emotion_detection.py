import json
import requests

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers=header)
    emotion_response = json.loads(response.text)
    emotions = emotion_response['emotionPredictions'][0]['emotion']

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    emotion = {
    'anger': emotions.get('anger', 0),
    'disgust': emotions.get('disgust', 0),
    'fear': emotions.get('fear', 0),
    'joy': emotions.get('joy', 0),
    'sadness': emotions.get('sadness', 0),
    }

    dominant_emotion = max(emotion, key=emotion.get)
    emotion['dominant_emotion'] = dominant_emotion
    return emotion
