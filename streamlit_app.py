import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
@st.cache
def load_data():
    data = pd.read_csv("owid-covid-data.csv")
    return data

data = load_data()

# Streamlit App Layout
st.title("COVID-19 Data Dashboard")
st.write("This dashboard visualizes COVID-19 data using various plots to provide insights into the pandemic.")

# New COVID-19 Cases Over Time
st.subheader("1. New COVID-19 Cases Over Time")
time_series_fig = px.line(
    data,
    x="date",
    y="new_cases",
    title="New Cases Over Time",
    labels={"date": "Date", "new_cases": "New Cases"},
)
time_series_fig.update_layout(title_font_size=20)
st.plotly_chart(time_series_fig)

# Total Cases by Continent
st.subheader("2. Total Cases by Continent")
continent_fig = px.bar(
    data.groupby("continent")["total_cases"].sum().reset_index(),
    x="continent",
    y="total_cases",
    title="Total Cases by Continent",
    labels={"continent": "Continent", "total_cases": "Total Cases"},
)
continent_fig.update_layout(title_font_size=20)
st.plotly_chart(continent_fig)

# World Map of Total Cases
#st.subheader("3. Geographical Distribution of Total Cases")
#map_fig = px.choropleth(
 #   data,
  #  locations="iso_code",
   # color="total_cases",
   # hover_name="location",
  #  title="World Map of Total Cases",
   # labels={"total_cases": "Total Cases"},
   # color_continuous_scale="Blues",
#)
#map_fig.update_layout(title_font_size=20)
#st.plotly_chart(map_fig)

# World Map of Total Cases with Separate Colors for Each Continent
#st.subheader("3. Geographical Distribution of Total Cases by Continent")
#map_fig = px.choropleth(
 #   data,
  #  locations="iso_code",
   # color="continent",  # Separate color for each continent
    #hover_name="location",
   # title="World Map of Total Cases by Continent",
   # labels={"continent": "Continent"},
   # category_orders={"continent": ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"]},
    #color_discrete_sequence=px.colors.qualitative.Set2  # Use a qualitative color palette
#)
#map_fig.update_layout(title_font_size=20, legend_title_text="Continent")
#st.plotly_chart(map_fig)


data = load_data()

# Streamlit App Layout
st.title("COVID-19 Heatmap Dashboard")
st.write("This dashboard visualizes COVID-19 data using a geographical heatmap with filtering options.")

# Dropdown for Continent Selection
st.subheader("Geographical Heatmap of COVID-19 Data")
continents = data['continent'].dropna().unique().tolist()
continents.sort()
continents.insert(0, "World")  # Add 'World' as an option
selected_continent = st.selectbox("Select a Continent or View the Entire World:", continents)

# Filter Data Based on Selected Continent
if selected_continent != "World":
    filtered_data = data[data["continent"] == selected_continent]
else:
    filtered_data = data

# Heatmap Visualization
heatmap_fig = px.choropleth(
    filtered_data,
    locations="iso_code",
    color="total_cases",  # Heatmap based on total cases
    hover_name="location",
    title=f"COVID-19 Heatmap: {selected_continent}",
    labels={"total_cases": "Total Cases"},
    color_continuous_scale=px.colors.sequential.Plasma,  # Heatmap color scale
)
heatmap_fig.update_layout(title_font_size=20, legend_title_text="Total Cases")
st.plotly_chart(heatmap_fig)

# Footer
st.write("---")
st.write("**Data Source**: Our World in Data (OWID)")

# End of Streamlit App

# Total Deaths Over Time
st.subheader("4. Total Deaths Over Time")
deaths_fig = px.line(
    data,
    x="date",
    y="total_deaths",
    title="Total Deaths Over Time",
    labels={"date": "Date", "total_deaths": "Total Deaths"},
)
deaths_fig.update_layout(title_font_size=20)
st.plotly_chart(deaths_fig)

# Total Vaccinations by Country
st.subheader("5. Total Vaccinations by Country")
vaccination_fig = px.bar(
    data.groupby("location")["total_vaccinations"].max().dropna().reset_index(),
    x="location",
    y="total_vaccinations",
    title="Total Vaccinations by Country",
    labels={"location": "Country", "total_vaccinations": "Total Vaccinations"},
)
vaccination_fig.update_layout(title_font_size=20)
st.plotly_chart(vaccination_fig)

# Footer
st.write("---")
st.write("**Data Source**: Our World in Data (OWID)")

# End of Streamlit App
