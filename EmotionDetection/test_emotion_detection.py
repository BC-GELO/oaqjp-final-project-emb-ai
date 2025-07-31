import unittest
from emotion_detection import emotion_detector

class Testing (unittest.TestCase):
    def test_emotion_detection(self):
        answer = emotion_detector("I am glad this happened")
        self.assertEqual(answer["dominant_emotion"], "joy")

        answer = emotion_detector("I am really mad about this")
        self.assertEqual(answer["dominant_emotion"], "anger")

        answer = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(answer["dominant_emotion"], "disgust")

        answer = emotion_detector("I am so sad about this")
        self.assertEqual(answer["dominant_emotion"], "sadness")

        answer = emotion_detector("I am really afraid that this will happend")
        self.assertEqual(answer["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()
