"""
The code has been taken from Code Institute walkthrough project, and
modified for the project
"""
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def performance_metrics_page():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')
    st.info(
        f"* test - powdery_mildew: 422 images\n"
        f"* test - healthy: 422 images\n"
        f"* train - powdery_mildew: 1472 images\n"
        f"* train - healthy: 1472 images\n"
        f"* validation - powdery_mildew: 210 images\n"
        f"* validation - healthy: 210 images"
    )
    st.write("---")

    st.write("### Model History")
    col1, col2 = st.columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))
