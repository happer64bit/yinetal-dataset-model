import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample

class RudeWord:
    def __init__(self, data_path='../dataset/words.csv'):
        self.data_path = data_path
        self.vectorizer = CountVectorizer()
        self.model = LogisticRegression()

    def load_data(self):
        try:
            df = pd.read_csv(self.data_path)
            df['label'] = df['label'].round().astype(int)
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"Dataset not found at {self.data_path}. Please check the path.")
        except Exception as e:
            raise RuntimeError(f"Error loading dataset: {e}")

    def train(self, df):
        X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)
        
        if len(y_train.unique()) < 2:
            raise ValueError("Training set needs at least two classes to train the model.")

        vectorizer = self.vectorizer.fit(X_train)
        X_train_vec = vectorizer.transform(X_train)
        X_test_vec = vectorizer.transform(X_test)

        model = self.model.fit(X_train_vec, y_train)
        return model, vectorizer, X_test_vec, y_test

    def evaluate(self, model, X_test_vec, y_test):
        y_pred = model.predict(X_test_vec)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return accuracy, report

    def predict(self, sample_text):
        sample_vec = self.vectorizer.transform([sample_text])
        prediction = self.model.predict(sample_vec)
        return prediction[0]