import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import time

## A basic line chart

df = pd.read_csv("./data/top_15_tea_countries_2004_2023.csv")

st.title("Top Tea Producing Countries from 2004-2023")

df_long = df.melt(id_vars=["country"], var_name="year", value_name="quantity")

# Convert 'year' to integer for sorting
df_long["year"] = df_long["year"].astype(int)

# Convert 'quantity' to numeric, forcing errors to NaN
df_long["quantity"] = pd.to_numeric(df_long["quantity"], errors="coerce")

# Drop rows where 'quantity' is NaN (invalid data)
df_long = df_long.dropna(subset=["quantity"])


# Create an interactive line plot using Plotly
fig = st.line_chart(df_long, x="year", y="quantity", color="country")

## An animated line chart

# Create a figure with Plotly
fig = go.Figure()

# Create a progress bar
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Define years and countries
years = sorted(df_long["year"].unique())
countries = df_long["country"].unique()

# Add initial trace (empty)
for country in countries:
    fig.add_trace(go.Scatter(x=[], y=[], mode="lines+markers", name=country))

# Display the empty chart first
chart = st.plotly_chart(fig, use_container_width=True)

# Loop through years and add data progressively
for i, year in enumerate(years):
    # Filter data for the current year
    year_data = df_long[df_long["year"] == year]

    # Update the traces for each country (add data year by year)
    for country in countries:
        country_data = year_data[year_data["country"] == country]
        # Find the corresponding trace index
        trace_index = list(countries).index(country)
        # Update the trace data for the year
        fig.data[trace_index].x = np.concatenate(
            [fig.data[trace_index].x, country_data["year"].values]
        )
        fig.data[trace_index].y = np.concatenate(
            [fig.data[trace_index].y, country_data["quantity"].values]
        )
    # Update the chart and progress
    chart.plotly_chart(fig, use_container_width=True)

    progress_bar.progress(int((i + 1) / len(years) * 100))
    status_text.text(f"{int((i + 1) / len(years) * 100)}% complete")

    time.sleep(0.5)  # Add a small delay for animation effect

# Clear the progress bar
progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Rerun")
