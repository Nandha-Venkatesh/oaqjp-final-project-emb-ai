import requests
import json

def format_output(text):
    data = json.loads(text)
    output = data["emotionPredictions"][0]["emotion"]
    dominant = max(output, key=output.get)
    output["dominant_emotion"] = dominant
    return output

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    resp = requests.post(url, headers=headers, json=data)

    if resp.status_code == 200:
        print(resp)
        return format_output(resp.text)

    else:
        print("An error occurred. Status code: " + resp.status_code)

if __name__ == "__main__":
    text = input("Write some text to analyze and press enter.\n")
    result = emotion_detector(text)
    print(result)