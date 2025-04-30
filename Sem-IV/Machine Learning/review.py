import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample product review dataset (Assume it has 'review_text' and 'sentiment' columns)
df = pd.read_csv('product_reviews.csv')  # Replace with your actual CSV path
df = df[['review_text', 'sentiment']]  # Assuming 'sentiment' is the target (binary: 0 = negative, 1 = positive)

# Initialize Porter Stemmer
porter_stemmer = PorterStemmer()

# Custom function to preprocess and stem text with word tokenization
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    # Tokenize text using word_tokenize
    words = word_tokenize(text.lower())  # Tokenizing and converting to lowercase
    # Stem each word if it's not in stopwords
    stemmed_words = [porter_stemmer.stem(word) for word in words if word.isalpha() and word not in stop_words]
    return " ".join(stemmed_words)

# Apply the preprocessing function to the review text
df['cleaned_review'] = df['review_text'].apply(preprocess_text)

# Features (X) and target (y)
X = df['cleaned_review']
y = df['sentiment']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data to numeric using TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=1000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Initialize and train the Naive Bayes (Multinomial) model
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)

# Predict on the test set
y_pred = nb_model.predict(X_test_tfidf)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


