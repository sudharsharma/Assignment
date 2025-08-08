import streamlit as st
import joblib
import numpy as np

st.title("Breast Cancer Prediction")
st.write("Enter the details for the prediction")

loaded_model = joblib.load("KNN.joblib")
scaler = joblib.load("breast_cancer.joblib")

feature_names = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
    "compactness_mean", "concave_points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se", "compactness_se",
    "concavity_se", "concave_points_se", "symmetry_se", "fractal_dimension_se",
    "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst",
    "compactness_worst", "concavity_worst", "concave_points_worst", "symmetry_worst",
    "fractal_dimension_worst"
]

user_data = []

cols = st.columns(3)
for i, feature in enumerate(feature_names):
    with cols[i % 3]:  
        value = st.number_input(feature, value=0.0, format="%.4f")
        user_data.append(value)

features = np.array([user_data])

scaled_features = scaler.transform(features)

button = st.button("Predict")
if st.button():
    pred = loaded_model.predict(scaled_features)[0]
    if pred == 1:
        st.error("Cancer positive")
    else:
        st.success("Cancer negative")
