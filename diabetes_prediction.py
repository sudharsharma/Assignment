import streamlit as st
import joblib
import numpy as np

# from sklearn import datasets

st.title("Diabetes Prediction")
st.write("Enter health metrics to predict diabetes risk.")

loaded_model = joblib.load("logestic_regression_model.joblib")
scaler = joblib.load("diabetes_scaler.joblib")

Age = st.number_input("Age", min_value=0)
Pregnancy = st.number_input("Pregenancy", min_value = 0)
BMI = st.number_input("BMI", min_value=0.0)
Glucose = st.number_input("Glucose", min_value=0.0)
BloodPressure = st.number_input("BloodPressure", min_value=0)
HbA1c = st.number_input("HbA1c", min_value=0)
LDL = st.number_input("LDL", min_value=0.0)
HDL = st.number_input("HDL", min_value=0.0)
HipCircumference = st.number_input("HipCircumference", min_value=0.0)
Triglycerides = st.number_input("Triglycerides", min_value=0.0)
WaistCircumference = st.number_input("WaistCircumference", min_value=0.0)
WHR = st.number_input("WHR", min_value=0.0)

features = np.array([[Age, Pregnancy, BMI, Glucose, BloodPressure, HbA1c, LDL,HDL,
                      Triglycerides, WaistCircumference, HipCircumference, WHR]])

scaled_features = scaler.transform(features)

button = st.button("Predict diabetes")
if button:
    pred = loaded_model.predict(scaled_features)[0]
    if pred == 1:
        st.error("Diabetic")
    else:
        st.success("Non‑Diabetic")
