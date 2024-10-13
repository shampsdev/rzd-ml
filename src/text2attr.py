import joblib

class TextToAttributeModel:
    def __init__(self):
        # Load the trained model from a specified file
        self.model = joblib.load("app/ml/train/trained/text2attr.pkl")

    def predict(self, text) -> int:
        # Make a prediction for the given text and return the predicted attribute
        return self.model.predict([text])[0]

if __name__ == "__main__":
    # Create an instance of the TextToAttributeModel
    model = TextToAttributeModel()
    
    # Test the model by predicting the attribute for a sample text
    print(model.predict("протянуть на пять вагонов"))
