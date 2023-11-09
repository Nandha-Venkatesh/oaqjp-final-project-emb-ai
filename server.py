from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request
import json
app = Flask("Emotion Detection")

def format(result):
    dominant = result["dominant_emotion"]
    del result["dominant_emotion"]
    return ("For the given statement, the system response is " + 
        json.dumps(result)[1:-1] + ". The dominant emotion is " + dominant + ".")


@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def run():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Error. Please enter valid text."
    else:
        return format(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)