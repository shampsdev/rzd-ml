from huggingsound import SpeechRecognitionModel


class SpeechToTextModel:
    def __init__(self):
        self.model = SpeechRecognitionModel(
            "jonatasgrosman/wav2vec2-large-xlsr-53-russian"
        )

    def predict(self, audio_path) -> str:
        return self.model.transcribe([audio_path])[0]["transcription"]
