import streamlit as st
import matplotlib.pyplot as plt


def hypothesis_page():
    st.write("### Project Hypothesis and Validation")

    st.info (
        f"* Powdery mildew is a white, dusty coating on leaves that "
        f"differentiates them from healthy leaves. \n\n"
        )
    st.success(
        f"* An Image Montage shows that powdery-mildew affected leaves have "
        f"patches of white coating, and have discolored. \n\n"
        f"* Average image also shows that powdery mildew affected leaves are "
        f"lighter in color.\n\n"
        f"* Variability and Average Difference images show no variation "
        f"around the middle of either leaf; however, "
        f"there is clear variation in contrast around the middle "
        f"of the healthy leaf."
    )
