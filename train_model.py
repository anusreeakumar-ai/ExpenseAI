import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Load data
df = pd.read_csv("expense_data.csv")

# ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# Train
model.fit(df["item"], df["category"])

# Save model
joblib.dump(model, "expense_category_model.pkl")

print("Model trained and saved!")
