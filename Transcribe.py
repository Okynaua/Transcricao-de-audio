import whisper
from playsound import playsound

#tiny, base, small, medium, large
model = whisper.load_model("large")
result = model.transcribe("audio.mp3", fp16=False)

with open("audio.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
print(result["text"])


playsound('Malandragem.mp3')