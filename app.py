import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary import summary_page
from app_pages.findings import findings_page
from app_pages.prediction import prediction_page
from app_pages.hypothesis import hypothesis_page
from app_pages.technical import performance_metrics_page

app = MultiPage(app_name="Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", summary_page)
app.add_page("Cells Visualiser", findings_page)
app.add_page("Malaria Detection", prediction_page)
app.add_page("Project Hypothesis", hypothesis_page)
app.add_page("ML Performance Metrics", performance_metrics_page)

app.run()  # Run the ap


