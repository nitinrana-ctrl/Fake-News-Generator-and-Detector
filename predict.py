import joblib
from preprocess import preprocess_text

# Load saved model and vectorizer
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_news(news_text):
    # Clean text
    cleaned_text = preprocess_text(news_text)

    # Convert to TF-IDF
    vector = vectorizer.transform([cleaned_text])

    # Predict
    prediction = model.predict(vector)[0]

    # Confidence score
    confidence = model.predict_proba(vector).max() * 100

    if prediction == 0:
     label = "⚠️ Fake News Detected"
    else:
     label = "✅ Real News Detected"

    return label, confidence


# Test
if __name__ == "__main__":
    news = input("Enter News:\n\n")

    result, confidence = predict_news(news)

    print("\nPrediction :", result)
    print(f"Confidence : {confidence:.2f}%")