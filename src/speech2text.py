import whisper

model = whisper.load_model("base")

class SpeechToTextModel:
    def __init__(self):
        pass

    def predict(self, audio_path) -> str:
        
        result = model.transcribe(audio_path)
      
        return result['text']