""" Importing the emotion detection function from the EmotionDetection package 
    Importing flask, render_template, and request to run the server
    Importing json to process json data """

import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

def format_output(response):
    """ Function to properly format the emotion data for output """

    dominant = response["dominant_emotion"]
    del response["dominant_emotion"]
    return ("For the given statement, the system response is " +
        json.dumps(response)[1:-1] + ". The dominant emotion is " + dominant + ".")


@app.route("/")
def render_index_page():
    """ Function to render index.html """
    return render_template("index.html")


@app.route("/emotionDetector")
def run():
    """ Function that runs the emotion detector and returns the proper output """

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"
    return format_output(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
