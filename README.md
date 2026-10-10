# AI-Based Dropout Prediction and Counseling System

**Smart India Hackathon 2025**

| | |
|---|---|
| **Problem Statement ID** | SIH25102 |
| **Problem Statement Title** | AI-based drop-out prediction and counseling system |
| **Theme** | Smart Automation |
| **PS Category** | Software |
| **Team ID** | 91089 |
| **Team Name** | ChangeMakerss |

---

## 📌 Overview

An AI-powered system that predicts student dropout risk (**High / Medium / Low**) and provides personalized counseling recommendations to enable early intervention — helping institutions improve student retention and academic success.

---

## 🚀 Proposed Solution

- AI-powered prediction system to classify students as **High / Medium / Low** risk
- Uses a **Kaggle dataset** + **Logistic Regression** model
- Provides **personalized counseling recommendations**
- **Streamlit-based web app** for faculty with CSV upload & risk reports
- Enables **early detection** before failure or dropout occurs
- **Unique value:** Combines prediction + counseling in a single platform

### System Architecture

```
User Uploads Data (CSV/Excel)
        ↓
Web App & Data Pre-processing (Cleaning, Feature Engineering, Normalization)
        ↓
ML Model Training (Logistic Regression / Random Forest / Deep Learning)
        ↓
Risk Category Prediction
        ↓
   Low / Medium / High Risk
        ↓
Personalized Counseling Advice (Academic Support, Mental Health,
Financial Aid, Career Guidance, Feedback Surveys)
        ↓
Export Results (PDF, CSV, Dashboard)
```

---

## 🛠️ Technical Approach

### Technologies
- Python, Pandas, Scikit-learn
- Machine Learning
- Streamlit (Web App)
- Matplotlib (Visualization)
- Dataset: Kaggle – Student Dropout & Academic Success

### Methodology
1. **Data Preprocessing** – Cleaning, encoding, and scaling data
2. **Model Training** – Training a Logistic Regression model
3. **Evaluation** – Accuracy, classification report, confusion matrix
4. **Deployment** – Streamlit app for predictions & counseling support

---

## ✅ Feasibility and Viability

**Feasibility**
- Works with real student datasets (tested on Kaggle)
- Scalable to integrate with ERP/LMS systems
- Low-cost (uses open-source tools)

**Challenges & Risks**
- Data quality & availability
- Privacy & ethics of student data
- Selecting a suitable ML model

**Mitigation Strategies**
- Retrain models with updated data
- Clean and validate datasets
- Use the most accurate model available

---

## 🌟 Impact and Benefits

**Potential Impact**
- Identify at-risk students early
- Provide timely counseling and support
- Improve academic success and retention
- Reduce dropout rate

**Benefits**
- Better student engagement, reduced failure rates
- Saves resources on repeated courses, improves institutional efficiency
- Data-driven decisions for mentoring and interventions

---

## 📄 License

This project was developed as part of Smart India Hackathon 2025.
