from .speech2text import SpeechToTextModel
from .text2label import TextToLabelModel


class Prediction:
    def __init__(self, text, label, attribute):
        self.text = text
        self.label = label
        self.attribute = attribute


class TextToAttributeModel:
    def __init__(self):
        pass

    def predict(self, text) -> int:
        return 10


class Model:
    def __init__(self):
        self.speech2text = SpeechToTextModel()
        self.text2label = TextToLabelModel()
        self.text2attr = TextToAttributeModel()

    def predict(self, audio_path) -> Prediction:
        text = self.speech2text.predict(audio_path)
        label = self.text2label.predict(text)
        attr = self.text2attr.predict(text)
        return Prediction(text, label, attr)
