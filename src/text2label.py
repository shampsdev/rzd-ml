import joblib
from .label2id import label2id


class TextToLabelModel:
    def __init__(self):
        self.model = joblib.load("src/text2label.pkl")

    def predict(self, text) -> int:
        return label2id(self.model.predict([text])[0])


if __name__ == "__main__":
    model = TextToLabelModel()
    print(model.predict("протянуть нам 15 вагонов."))
