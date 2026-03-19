from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # 1. Get the text
    text_to_analyze = request.args.get('textToAnalyze')
    
    # 2. Get the dictionary from your package
    response = emotion_detector(text_to_analyze)

    # 3. IMMEDIATELY check if it's the "Error Dictionary" (all Nones)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # 4. ONLY IF IT IS NOT NONE, create the success string
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)