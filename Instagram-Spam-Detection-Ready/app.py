
from flask import Flask, render_template, request
import joblib
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

app = Flask(__name__)

model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    filtered_words = []

    for word in words:
        if word not in stop_words:
            filtered_words.append(stemmer.stem(word))

    return ' '.join(filtered_words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    comment = request.form['comment']

    cleaned_comment = clean_text(comment)
    vectorized_comment = vectorizer.transform([cleaned_comment])

    prediction = model.predict(vectorized_comment)[0]
    probability = model.predict_proba(vectorized_comment)[0]

    spam_probability = round(max(probability) * 100, 2)

    if prediction == 1:
        result = "SPAM COMMENT"
        description = "This comment is likely promotional or bot-generated."
    else:
        result = "NOT SPAM"
        description = "This comment appears genuine and safe."

    return render_template(
        'result.html',
        comment=comment,
        result=result,
        probability=spam_probability,
        description=description
    )

if __name__ == '__main__':
    app.run(debug=True)
