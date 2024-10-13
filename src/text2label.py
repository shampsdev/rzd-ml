import joblib


class TextToLabelModel:
    def __init__(self):
        self.model = joblib.load("train/trained/text2label.pkl")

    def predict(self, text) -> int:
        return self.model.predict([text])[0]


if __name__ == "__main__":
    model = TextToLabelModel()
    print(model.predict("протянуть нам 15 вагонов."))
