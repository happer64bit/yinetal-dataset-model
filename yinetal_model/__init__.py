from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import os

class RudeWord:
    def __init__(self, data_path='../dataset/words.txt'):
        self.data_path = self.get_full_path(data_path)
        self.vectorizer = CountVectorizer(tokenizer=self.burmese_tokenizer)
        self.model = LogisticRegression()

    def get_full_path(self, relative_path):
        base_path = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(base_path, relative_path))

    def burmese_tokenizer(self, text):
        tokens = text.split()
        return tokens

    def load_data(self):
        try:
            with open(self.data_path, 'r', encoding='utf-8') as file:
                rude_words = [line.strip() for line in file.readlines() if line.strip()]
            return rude_words
        except FileNotFoundError:
            raise FileNotFoundError(f"Dataset not found at {self.data_path}. Please check the path.")
        except Exception as e:
            raise RuntimeError(f"Error loading dataset: {e}")

    def train(self, df):
        raise NotImplementedError("Training not implemented for this example.")

    def predict_rude_word(self, text):
        text_vec = self.vectorizer.transform([text])
        prediction = self.model.predict(text_vec)
        return prediction[0] == 1
