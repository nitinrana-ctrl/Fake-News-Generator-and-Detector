import pandas as pd
import joblib
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from preprocess import preprocess_text

print("Loading datasets...")

# Load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Keep only text column
fake = fake[["text"]]
true = true[["text"]]

# Create labels
fake["label"] = 0   # Fake
true["label"] = 1   # Real

# Merge datasets
data = pd.concat([fake, true], ignore_index=True)

print(f"Total Articles : {len(data)}")

# Preprocess text
print("Cleaning text...")
data["text"] = data["text"].apply(preprocess_text)

# Features and Labels
X = data["text"]
y = data["label"]

# Convert text into TF-IDF vectors
print("Creating TF-IDF vectors...")
vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
print("Training Naive Bayes Model...")

model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL TRAINED SUCCESSFULLY")
print("==============================")

print(f"\nAccuracy : {accuracy*100:.2f}%")

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, y_pred))

# Create models folder
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("\nModel Saved Successfully!")
print("models/model.pkl")
print("models/vectorizer.pkl")