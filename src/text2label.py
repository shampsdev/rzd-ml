import joblib
from .label2id import label2id


class TextToLabelModel:
    def __init__(self):
        self.model = joblib.load("app/ml/src/text2attr.pkl")

    def predict(self, text) -> int:
        return label2id(self.model.transcript([text])[0])


if __name__ == "__main__":
    model = TextToLabelModel()
    print(model.predict("протянуть нам 15 вагонов."))
