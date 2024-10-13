import joblib

class TextToLabelModel:
    def __init__(self):
        # Load the trained model from a specified file
        self.model = joblib.load("app/ml/train/trained/text2label.pkl")

    def predict(self, text) -> int:
        # Make a prediction for the given text and return the predicted label
        return self.model.predict([text])[0]

if __name__ == "__main__":
    # Create an instance of the TextToLabelModel
    model = TextToLabelModel()
    
    # Test the model by predicting the label for a sample text
    print(model.predict("протянуть нам 15 вагонов."))
