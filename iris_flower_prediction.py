import streamlit as st
from sklearn import datasets
import joblib

iris  = datasets.load_iris()

petal_length = st.number_input("Enter the length pf petal")
petal_width = st.number_input("Enter the width of petal")
sepal_length = st.number_input("Enter the length of sepal")
sepal_width = st.number_input("Enter the width of sepal")

flower_btn = st.button("Predict flower")

loaded_model = joblib.load("D:\AI learning\Sk_learn\iris_classifier_knn_model.joblib")

sample = [[sepal_length,sepal_width,petal_length,petal_width]]
prediction = loaded_model.predict(sample)[0]

if flower_btn:
    st.success(f"predicted flower is {iris.target_names[prediction]}")