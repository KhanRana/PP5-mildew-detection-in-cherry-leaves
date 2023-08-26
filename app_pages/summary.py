import streamlit as st
import matplotlib.pyplot as plt


def summary_page():

    st.write("### Brief Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew of sweet and sour cherry is caused by Podosphaera clandestina, " 
        f"an obligate biotrophic fungus. Mid- and late-season sweet cherry (Prunus avium) "
        f"cultivars are commonly affected, rendering them unmarketable due to the covering "
        f"of white fungal growth on the cherry surface.\n"
        f"* Initial symptoms, often occurring 7 to 10 days after the onset "
        f"of the first irrigation, are light roughly-circular, powdery looking patches "
        f"on young, susceptible leaves (newly unfolded, and light green expanding leaves). "
        f"Older leaves develop an age-related (ontogenic) resistance to powdery mildew and "
        f"are naturally more resistant to infection than younger leaves.\n"
        f"* In contrast to other fungi, powdery mildews do not need free water "
        f"to germinate but germination and fungal growth are favored by high "
        f"humidity (Grove & Boal, 1991a).\n"
        f"\n**Project Dataset**\n"
        f"* The available dataset contains 4208 images: "
        f"2104 each for heathy and powdery mildew"
    )
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/KhanRana/PP5-mildew-detection-in-cherry-leaves#readme).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"""* 1 -  The client is interested in conducting a study to visually 
        differentiate a healthy cherry leaf from one with powdery mildew.\n"""
        f"""* 2 - The client is interested in predicting if a cherry leaf is 
        healthy or contains powdery mildew."""
        )