import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

## A basic chart

data = pd.read_csv("../data/uk_landmarks.csv")

st.title("British culture overview")

options = data["Category"].unique()

selected_cat = st.multiselect(label="Select the category", options=options)

if selected_cat:
    filtered_data = data[data["Category"].isin(selected_cat)]
    st.scatter_chart(data=filtered_data, x="Year", y="Name", size="Visitors")
else:
    st.scatter_chart(data=data, x="Year", y="Name", size="Visitors")

"""
Ok, that's nice but can we make it look better?
Let's use matplotlib!
"""

import matplotlib.pyplot as plt  # noqa: E402

timeline_df = data[["Year", "Name", "Level"]]

with plt.style.context("fivethirtyeight"):
    fig, ax = plt.subplots(figsize=(9, 18))

    ax.plot(
        [
            0,
        ]
        * len(timeline_df),
        timeline_df.Year,
        "-o",
        color="black",
        markerfacecolor="white",
    )

    ax.set_xlim(-20, 20)

    for idx in range(len(timeline_df)):
        dt, product, level = (
            timeline_df["Year"][idx],
            timeline_df["Name"][idx],
            timeline_df["Level"][idx],
        )
        ax.annotate(
            dt.astype(str) + "-" + product,
            xy=(0.1, dt),
            xytext=(level, dt),
            arrowprops=dict(arrowstyle="-", color="red", linewidth=0.8),
            va="center",
            linespacing=0.5,
            fontsize="small",
        )
    ax.set_title("British Culture Timeline", pad=10, loc="left", fontsize=16)
    ax.grid(False)

st.write(fig)
