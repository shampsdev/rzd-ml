class Prediction:
    def __init__(self, text, label, attribute):
        self.text = text
        self.label = label
        self.attribute = attribute


class Model:
    def __init__(self):
        pass

    def predict(self, audio_path) -> Prediction:
        return Prediction("420", 6, 9)
