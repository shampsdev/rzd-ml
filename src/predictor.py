import os
from .model import Model


class Predictor:
    """Class for your model's predictions.

    You are free to add your own properties and methods
    or modify existing ones, but the output submission
    structure must be identical to the one presented.

    Examples:
        >>> python -m get_submission --src input_dir --dst output_dir
    """

    def __init__(self):
        self.model = Model()

    def __call__(self, audio_path: str):
        prediction = self.model.predict(audio_path)
        result = {
            "audio": os.path.basename(audio_path),  # Audio file base name
            "text": prediction.text,  # Predicted text
            "label": prediction.label,  # Text class
            "attribute": prediction.attribute,
        }
        return result
