# AI-Based Instagram Spam Detection System

## Project Title

AI-Based Instagram Spam Detection Using NLP and Machine Learning

---

# Project Overview

This project is a web-based AI application that detects whether an Instagram comment is spam or genuine using Natural Language Processing (NLP) and Machine Learning techniques.

Spam comments on social media platforms often contain:

* fake promotions
* malicious links
* scam offers
* bot-generated advertisements

This system automatically analyzes comments and predicts whether the comment is:

* SPAM COMMENT
* NOT SPAM

The project uses:

* Python
* Flask
* TF-IDF Vectorization
* Logistic Regression
* NLP preprocessing techniques

---

# Features

* AI-based spam detection
* Modern Instagram-style UI
* NLP text preprocessing
* Spam probability score
* Real-time prediction
* Responsive design
* Flask web application

---

# Technologies Used

| Technology          | Purpose              |
| ------------------- | -------------------- |
| Python              | Backend Programming  |
| Flask               | Web Framework        |
| Scikit-learn        | Machine Learning     |
| NLP                 | Text Processing      |
| TF-IDF              | Feature Extraction   |
| Logistic Regression | Classification Model |
| HTML/CSS            | Frontend Design      |

---

# Project Structure

```text
Instagram-Spam-Detection-Ready/
│
├── app.py
├── requirements.txt
├── spam_dataset.csv
├── spam_model.pkl
├── vectorizer.pkl
├── README.txt
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    └── result.html
```

---

# Required Software

Install the following before running the project:

## 1. Python

Recommended version:

* Python 3.11 or above

Download:
https://www.python.org/downloads/

---

## 2. VS Code

Download:
https://code.visualstudio.com/

---

# Required VS Code Extensions

Install these extensions in VS Code:

1. Python
2. Pylance

---

# Required Python Libraries

The following libraries are used:

* flask
* pandas
* numpy
* scikit-learn
* joblib
* nltk

Install all libraries using:

```bash
pip install -r requirements.txt
```

---

# How To Run The Project

## Step 1

Open the project folder in VS Code.

---

## Step 2

Open terminal in VS Code.

---

## Step 3

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Step 4

Run the Flask application:

```bash
python app.py
```

---

## Step 5

Open browser and go to:

```text
http://127.0.0.1:5000
```

---

# Sample Test Comments

## Spam Comments

```text
DM me for free followers and likes
```

```text
Click this link and earn money fast
```

```text
Guaranteed crypto profits message me now
```

```text
Free iPhone giveaway click here now
```

```text
Earn $5000 per day from home easy money
```

```text
Visit my profile for instant followers
```

---

## Genuine Comments

```text
Your editing skills are amazing
```

```text
This reel was really helpful
```

```text
Bro this meme is hilarious 😂
```

```text
Amazing photography work
```

```text
Nice tutorial thanks for sharing
```

---

# Machine Learning Workflow

```text
Input Comment
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Logistic Regression Model
      ↓
Spam / Not Spam Prediction
```

---

# NLP Techniques Used

* Lowercase conversion
* Punctuation removal
* Stopword removal
* Tokenization
* Stemming
* TF-IDF vectorization

---

# Advantages

* Fast spam detection
* Improves social media safety
* Reduces fake promotional comments
* Simple and user-friendly interface
* Lightweight ML model

---

# Future Enhancements

* BERT/ALBERT integration
* Real-time Instagram API connection
* Multi-language support
* Deep learning implementation
* Admin dashboard

---

# Conclusion

The AI-Based Instagram Spam Detection System successfully classifies spam and genuine comments using NLP and Machine Learning techniques. The system provides an efficient solution for detecting harmful and promotional comments on social media platforms.

---

# Developed By

K NISHANTH

AI & Machine Learning Mini Project
