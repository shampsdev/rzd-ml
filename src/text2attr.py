import joblib


class TextToAttributeModel:
    def __init__(self):
        self.model = joblib.load("src/text2attr.pkl")
        pass

    def predict(self, text) -> int:
        return self.model.predict([text])[0]


if __name__ == "__main__":
    model = TextToAttributeModel()
    print(model.predict("протянуть на пять вагонов"))
