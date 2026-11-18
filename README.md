# SentiMind — ML-Powered Sentiment Analysis

SentiMind is a Machine Learning project that analyzes written reviews and classifies their sentiment as **Positive** or **Negative**. It combines text processing and supervised learning to identify sentiment patterns in user reviews.

The project uses TF-IDF feature extraction and compares Logistic Regression with Multinomial Naive Bayes to identify a suitable classification model.

## ✨ Features

- Binary sentiment classification: Positive or Negative
- Text feature extraction using TF-IDF
- Unigram and bigram feature analysis
- Comparison of two Machine Learning algorithms
- Evaluation using accuracy, precision, recall, and F1-score
- Confidence score estimation using model probabilities
- Saved model pipeline for reuse in an application
- Custom website interface built with HTML and CSS

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Data Processing:** Pandas
- **Machine Learning:** Scikit-learn
- **Text Feature Extraction:** TF-IDF Vectorizer
- **Classification Algorithms:** Logistic Regression and Multinomial Naive Bayes
- **Model Persistence:** Joblib
- **Data Visualization:** Matplotlib
- **Frontend:** HTML5 and CSS3
- **Development Environment:** Jupyter Notebook

## 📊 Dataset

The training data is organized into separate files containing positive and negative reviews:

- `TrainingDataPositive.txt` — positive reviews
- `TrainingDataNegative.txt` — negative reviews
- `TestReviews.csv` — a separate review dataset containing review text and class labels

After cleaning and removing duplicate training reviews, the notebook contains **10,282 training examples**.

The training labels are encoded as:

- `1` — Positive
- `0` — Negative

## ⚙️ Machine Learning Workflow

1. **Data Collection:** Load positive and negative reviews from text files.
2. **Data Preprocessing:** Remove leading and trailing whitespace, empty reviews, and duplicate reviews.
3. **Train-Test Split:** Divide the training data into 80% training and 20% testing subsets using stratified sampling.
4. **Feature Extraction:** Convert text into numerical TF-IDF features using unigrams and bigrams.
5. **Model Training:** Train Logistic Regression and Multinomial Naive Bayes classifiers.
6. **Model Evaluation:** Compare model performance using accuracy, precision, recall, and F1-score.
7. **Model Saving:** Save the Logistic Regression pipeline using Joblib for subsequent use.

## 📈 Model Performance

The following results were recorded in the Jupyter Notebook:

| Metric | Logistic Regression | Multinomial Naive Bayes |
| Accuracy  | 94.70%           | 91.59%                  |
| Precision | 96.41%           | 90.46%                  |
| Recall    | 96.08%           | 98.49%                  |
| F1-score  | 96.25%           | 94.30%                  |

Based on this experiment, Logistic Regression achieved higher accuracy, precision, and F1-score. It was selected as the saved model pipeline.


## 🎯 Project Objective

The objective of SentiMind is to demonstrate the practical application of Machine Learning in text classification and build a foundation for an interactive sentiment analysis web application.

## 👨‍💻 Author

**Manav Saxena**

GitHub: [Add your GitHub profile link]

---

*Developed as a Machine Learning and Web Development project.*
