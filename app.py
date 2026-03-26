import streamlit as st
from src.predict import predict

st.set_page_config(page_title="Loan Approval Predictor", layout="centered")

st.title("🏦 Loan Approval Prediction System")
st.write("Enter applicant details to check loan approval status")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

app_income = st.number_input("Applicant Income", min_value=0)
coapp_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term", min_value=1)
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Button
if st.button("Predict"):

    input_data = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': app_income,
        'CoapplicantIncome': coapp_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': credit_history,
        'Property_Area': property_area
    }

    result = predict(input_data)

    st.subheader(f"Result: {result}")