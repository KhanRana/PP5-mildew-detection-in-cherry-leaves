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