import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
covid_data = pd.read_csv('owid-covid-data.csv')

# Filter data
countries = st.multiselect("Select countries:", covid_data['location'].unique())
filtered_data = covid_data[covid_data['location'].isin(countries)]

# Create visualizations
st.title("COVID-19 Dashboard")
st.line_chart(filtered_data.groupby('date')['new_cases'].sum(), use_container_width=True)
st.bar_chart(filtered_data.groupby('location')['total_cases'].max(), use_container_width=True)

# Interactive map example
if 'location' in covid_data.columns:
    fig = px.scatter_geo(filtered_data, locations="location", color="total_cases", hover_name="location")
    st.plotly_chart(fig)
