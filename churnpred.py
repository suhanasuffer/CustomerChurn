import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.dropna(inplace=True)

# Clean column names
df.columns = df.columns.str.strip()

# Convert target to binary
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

st.title("Telco Customer Churn Dashboard")

st.sidebar.header("Filter")
gender = st.sidebar.multiselect("Select Gender", options=df['gender'].unique(), default=df['gender'].unique())
contract = st.sidebar.multiselect("Contract Type", options=df['Contract'].unique(), default=df['Contract'].unique())

df_filtered = df[(df['gender'].isin(gender)) & (df['Contract'].isin(contract))]

# Pie chart
st.subheader("Churn Distribution")
churn_pie = df_filtered['Churn'].value_counts().rename({0: "No", 1: "Yes"})
fig_pie = px.pie(names=churn_pie.index, values=churn_pie.values)
st.plotly_chart(fig_pie)

# Boxplot
st.subheader("Monthly Charges by Churn")
fig_box = px.box(df_filtered, x="Churn", y="MonthlyCharges", color="Churn", points="all")
st.plotly_chart(fig_box)

# Bar chart of InternetService vs Churn
st.subheader("Internet Service vs Churn")
fig_bar = px.histogram(df_filtered, x="InternetService", color="Churn", barmode="group")
st.plotly_chart(fig_bar)

