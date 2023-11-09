from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request
import json
app = Flask("Emotion Detection")

def format(response):
    dominant = response["dominant_emotion"]
    del response["dominant_emotion"]
    return ("For the given statement, the system response is " + 
        json.dumps(response)[1:-1] + ". The dominant emotion is " + dominant + ".")


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.route("/emotionDetector")
def run():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"
    else:
        return format(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)