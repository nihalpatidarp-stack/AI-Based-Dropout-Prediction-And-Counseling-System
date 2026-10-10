import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


@st.cache_data
def load_and_process_data():
    data = pd.read_csv("students_dropout_academic_success.csv")
    data['target'] = LabelEncoder().fit_transform(data['target'])
    data.drop(data[data['target'] == 1].index, inplace=True)  # Filter unwanted class if needed
    data['Dropout'] = data['target'].apply(lambda x: 1 if x == 0 else 0)
    return data


def risk_category(prob):
    if prob >= 0.6:
        return "High Risk"
    elif prob >= 0.3:
        return "Medium Risk"
    else:
        return "Low Risk"


def counseling_message(risk):
    if risk == "High Risk":
        return "Immediate intervention required: schedule one-on-one counseling sessions and monitor academic progress weekly."
    elif risk == "Medium Risk":
        return "Preventive measures advised: offer group counseling and academic support workshops."
    else:
        return "Maintain regular support and encourage engagement with academic resources."


def train_model(data):
    X = data.iloc[:, :34].values
    y = data['Dropout'].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=500)
    model.fit(x_train, y_train)
    return model, scaler, x_test, y_test


# Function to color cells in Risk Category column based on value
def color_risk(val):
    if val == "High Risk":
        return 'background-color: red; color: white;'
    elif val == "Medium Risk":
        return 'background-color: orange; color: black;'
    elif val == "Low Risk":
        return 'background-color: green; color: white;'
    else:
        return ''


def main():
    st.title("Smart India Hackathon - Student Dropout Prediction & Counseling")

    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("Choose Activity",
                                    ["About", "Train Model & Evaluate", "Upload New Data for Prediction"])

    data = load_and_process_data()

    if app_mode == "About":
        st.markdown("""
        ## Student Dropout Prediction System
        This app predicts dropout risks for students using logistic regression.
        Upload student data or explore model evaluation on academic dataset.
        """)

    elif app_mode == "Train Model & Evaluate":
        st.subheader("Model Training and Evaluation")

        st.write(f"Dataset shape: {data.shape}")
        st.write("Sample data:")
        st.dataframe(data.head())

        model, scaler, x_test, y_test = train_model(data)

        y_pred_prob = model.predict_proba(x_test)[:, 1]
        y_pred_class = (y_pred_prob >= 0.5).astype(int)
        risk_labels = [risk_category(p) for p in y_pred_prob]

        st.subheader("Test Set Predictions with Risk Categories")
        results = pd.DataFrame({
            'Dropout Probability': y_pred_prob,
            'Risk Category': risk_labels,
            'Predicted Label': y_pred_class
        })
        st.dataframe(results)

        st.subheader("Model Performance Metrics")
        report = classification_report(y_test, y_pred_class, target_names=['Non-Dropout', 'Dropout'], output_dict=True)
        report_df = pd.DataFrame(report).transpose()
        st.dataframe(report_df)

        st.subheader("Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred_class)
        disp = ConfusionMatrixDisplay(cm, display_labels=['Non-Dropout', 'Dropout'])
        fig, ax = plt.subplots()
        disp.plot(ax=ax)
        st.pyplot(fig)

    elif app_mode == "Upload New Data for Prediction":
        st.subheader("Upload new student data CSV")
        uploaded_file = st.file_uploader("Upload CSV file with 34 feature columns", type=["csv"])
        color_map = {
                    "High Risk": "red",
                    "Medium Risk": "orange",
                    "Low Risk": "green"
                    }

        if uploaded_file is not None:
            try:
                new_data = pd.read_csv(uploaded_file)
                if new_data.shape[1] != 34:
                    st.error(f"Uploaded data must have exactly 34 feature columns; found {new_data.shape[1]}")
                else:
                    model, scaler, _, _ = train_model(data)  # Train model for prediction
                    new_data_scaled = scaler.transform(new_data.values)
                    new_probs = model.predict_proba(new_data_scaled)[:, 1]
                    new_risks = [risk_category(p) for p in new_probs]

                    prediction_df = pd.DataFrame({
                        'Dropout Probability': new_probs,
                        'Risk Category': new_risks
                    })

                    st.write("Predictions and Counseling Recommendations:")
                    for i, risk in enumerate(new_risks):
                        color = color_map.get(risk, "black")
                        st.markdown(f"**Student {i+1} (<span style='color:{color};'>{risk}</span>):**", unsafe_allow_html=True)
                        st.write(f"Dropout Probability: {new_probs[i]:.2f}")
                        st.info(counseling_message(risk))
                        note = st.text_area(f"Add counselors note for Student {i+1}", key=f"note_{i}")
                        # Notes can be stored or processed as needed, here just displayed

                    st.subheader("Summary Table")

                    # Apply color styling to Risk Category column
                    styled_df = prediction_df.style.applymap(color_risk, subset=['Risk Category'])
                    st.dataframe(styled_df)

                    csv = prediction_df.to_csv(index=False).encode()
                    st.download_button("Download Predictions as CSV", data=csv,
                                       file_name="dropout_risk_predictions.csv", mime="text/csv")
            except Exception as e:
                st.error(f"Error processing uploaded file: {e}")


st.markdown("<h1 style='color:deepskyblue;'>Smart India Hackathon</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    .sidebar .sidebar-content {
        background-color: #4682b4;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if __name__ == "__main__":
    main()

