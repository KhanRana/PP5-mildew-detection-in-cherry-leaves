import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import tensorflow as tf
from tf.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def resize_input_image(img, version):
    """
    Reshape image to 50x50 image size and normalise it
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/mildew_detection_model.h5")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'healthy': 0, 'powdery_mildew': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the sample cell is "
        f"**{pred_class.lower()}** with malaria.")

    return pred_proba, pred_class