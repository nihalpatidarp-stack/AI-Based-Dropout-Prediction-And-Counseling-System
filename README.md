# 🎓 Student Dropout Prediction & Counseling Dashboard

An AI-based web application designed to predict student dropout risk using machine learning and provide personalized counseling recommendations to support academic success and improve student retention.

## 🚀 Features

- **Dropout Risk Prediction:** Classifies students into Low, Medium, and High risk categories.
- **Machine Learning:** Uses Logistic Regression to predict dropout risk based on academic data.
- **Model Evaluation:** Displays classification metrics and a confusion matrix to evaluate model performance.
- **CSV Upload:** Allows users to upload student data for batch predictions.
- **Personalized Counseling:** Provides recommendations based on predicted risk categories.
- **Result Export:** Enables users to download prediction results as a CSV file.
- **Interactive Dashboard:** Provides a user-friendly interface built with Streamlit.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas and NumPy
- Scikit-learn
- Matplotlib
- Logistic Regression

## ⚙️ Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/nihalpatidarp-stack/Dropout_Dashboard.git
   cd Dropout_Dashboard
   ```

2. Install the required libraries:

   ```bash
   pip install streamlit pandas numpy scikit-learn matplotlib
   ```

3. Run the application:

   ```bash
   streamlit run app_new.py
   ```

4. Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 📊 How It Works

1. Load and preprocess the student academic dataset.
2. Train a Logistic Regression model.
3. Evaluate model performance using classification metrics and a confusion matrix.
4. Upload new student data in CSV format.
5. Predict dropout probabilities and assign risk categories.
6. Display counseling recommendations and export the results.

## 🎯 Objective

The goal of this project is to support early identification of students who may be at risk of dropping out and help educators plan timely academic interventions and counseling support.

## ⚠️ Disclaimer

Predictions are intended to support educational decision-making and should not be treated as definitive judgments about individual students. Model performance and fairness should be evaluated before real-world use.
