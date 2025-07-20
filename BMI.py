import streamlit as st
import joblib

st.title("BMI CALCULATOR")

weight = st.number_input("Enter your weight in kg", min_value=0.00)
height_unit = st.radio("Select height unit:", ["centimeter", "inch", "meter", "feet"])
height = st.number_input("Enter your height""]", min_value = 0.00)

bmi_button = st.button("Calculate BMI")

if height_unit == "centimeter":
    height_meter = height/100

elif height_unit == "inch":
    height_meter = height/39.37

elif height_unit == "feet":
    height_meter = height/3.28

else:
    height_meter = height

if bmi_button:
    bmi = weight / (height_meter **2)
    st.success(f"Your BMI is {bmi:.2f}")

    if bmi < 16:
        st.error("You are extremly underweight")

    elif bmi < 18.5:
        st.warning("You are underweight")

    elif bmi < 24.9:
        st.success("You are Healthy")

    elif bmi < 30:
        st.warning("You are Overweight")

    else:
        st.error("You are extremly overweight")