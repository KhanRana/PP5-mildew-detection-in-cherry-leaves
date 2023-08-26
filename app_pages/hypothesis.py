import streamlit as st
import matplotlib.pyplot as plt


def hypothesis_page():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Powdery mildew is a white, dusty coating that "
        f"differentiates them from healthy leaves. \n\n"
        f"* An Image Montage shows that powdery-mildew affected leaves have "
        f"patches of white coating, and have discolored. \n\n"
        f"* Average Image shows that powdery mildew affected leaves are " 
        f"lighter in color; Variability Image shows variance around the edges in "
        f"healthy leaves compared to no significant in afected leaves. "
        f"and; Difference between Averages studies also also reveal similar affect to "
        f"variabillity."
    )