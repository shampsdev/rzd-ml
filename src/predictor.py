import os
from .model import Model
from .label2id import parse_label


class Predictor:
    """Class for your model's predictions.

    You are free to add your own properties and methods
    or modify existing ones, but the output submission
    structure must be identical to the one presented.
    """

    def __init__(self):
        self.model = Model()

    def __call__(self, audio_path: str):
        prediction = self.model.predict(audio_path)
        prediction.text = parse_label(prediction.label, prediction.attribute)
        result = {
            "audio": os.path.basename(audio_path),  # Audio file base name
            "text": prediction.text,  # Predicted text
            "label": prediction.label,  # Text class
            "attribute": prediction.attribute,
        }
        return result
