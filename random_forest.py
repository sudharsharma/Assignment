import numpy as np
import streamlit as st
import joblib 


model = joblib.load("random_forest.joblib")

st.title("Titanic Survival Prediction")
st.write("Enter the details to predict the survival rate of the passengers")

Pclass = st.number_input("Passenger class", min_value=1, max_value=3)
Sex = st.selectbox("Gender", ("Male", "Female", "Others"))
Age = st.number_input("Age", min_value=0)
SibSp = st.number_input("Siblings", min_value=0)
Parch = st.number_input("Parent and children", min_value=0)
Fare = st.number_input("Ticket fair", min_value= 0.0, format= "%.2f")

sex_map = {"Male": 1, "Female": 0}
sex_num = sex_map.get(Sex, 0)

features = np.array([[Pclass, sex_num, Age, SibSp, Parch, Fare]])

button = st.button("Predict")
if button:
    pred = model.predict(features)[0]
    probablity = model.predict_proba(features)[0][pred]
    if pred == 0:
        st.success(f"this person survived, Probality:, {probablity:.2f}")
    else:
        st.error(f"This person has drowned, Probability: {probablity:.2f}")