import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("HHS_Unaccompanied_Alien_Children_Program.csv")

# Clean numeric columns
cols = [
    'Children in CBP custody',
    'Children transferred out of CBP custody',
    'Children in HHS Care',
    'Children discharged from HHS Care'
]

for col in cols:
    df[col] = df[col].astype(str).str.replace(',', '').astype(float)

# KPIs
df['Transfer_Eff'] = df['Children transferred out of CBP custody'] / df['Children in CBP custody']
df['Discharge_Eff'] = df['Children discharged from HHS Care'] / df['Children in HHS Care']
df['Backlog'] = df['Children in CBP custody'] - df['Children transferred out of CBP custody']

# Dashboard
st.title("Healthcare Data Analysis Dashboard")

st.subheader("Key Metrics")
st.metric("Avg Transfer Efficiency", round(df['Transfer_Eff'].mean(),2))
st.metric("Avg Discharge Efficiency", round(df['Discharge_Eff'].mean(),4))
st.metric("Avg Backlog", int(df['Backlog'].mean()))

st.subheader("Efficiency Trends")
st.line_chart(df[['Transfer_Eff', 'Discharge_Eff']])

st.subheader("System Load")
st.bar_chart(df[['Children in CBP custody', 'Children in HHS Care']])

st.subheader("Backlog Trend")
st.line_chart(df['Backlog'])