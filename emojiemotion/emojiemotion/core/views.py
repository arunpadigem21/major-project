from django.shortcuts import render

# Simple emoji to emotion mapping
emoji_dict = {
    "😀": "Happy", "😃": "Happy", "😄": "Happy", "😁": "Happy", "😊": "Happy", "😆": "Happy",
    "😢": "Sad", "😭": "Sad", "😿": "Sad", "😞": "Sad", "😔": "Sad",
    "😡": "Angry", "🤬": "Angry", "👿": "Angry",
    "😱": "Surprised", "😲": "Surprised", "😯": "Surprised",
    "😍": "Loving", "😘": "Loving", "🥰": "Loving", "❤️": "Loving",
    "😴": "Sleepy", "🥱": "Sleepy",
    "🤢": "Disgusted", "🤮": "Disgusted",
    "😨": "Scared", "😰": "Scared", "👻": "Scared",
    "🤔": "Thinking", "😐": "Neutral", "😶": "Speechless"
}

def home(request):
    emotion = None
    if request.method == "POST":
        emoji = request.POST.get("emoji_input")
        emotion = emoji_dict.get(emoji, "Emotion not recognized")
    return render(request, "index.html", {"emotion": emotion})
