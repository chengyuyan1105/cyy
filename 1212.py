import streamlit as st
st.header("计算你的BMI")
st.subheader("按要求输入你的身高体重")

height = float(st.text_input("请输入身高（cm）", "168")) / 100

weight = float(st.text_input("请输入体重(kg)","48"))

BMI = weight / (height ** 2)
st.write(BMI)
















