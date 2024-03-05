# Import necessary libraries
import streamlit as st
from PIL import Image

# Set Streamlit page configuration
st.set_page_config(page_title="Real Estate Analytics App")

# Home Page
st.title('Real Estate Analytics App')
st.markdown("---")

# Provide a brief description or welcome message
st.write("""
Welcome to the Real Estate Analytics App! This app helps you analyze and explore real estate data for Gurgaon.
Navigate through different pages to predict prices, visualize analytics, and get apartment recommendations.
""")

# Add an image for visual appeal
image = Image.open("images/Real_Estate_Analytics.jpg")  # Replace with the path to your image
st.image(image, caption="Real Estate Analytics App", use_column_width=True , width=400)

# Add additional content or links to guide users
st.write("Explore the various functionalities by selecting the pages from the sidebar.")

# Create a horizontal line using markdown
st.markdown("---")

# price Prediction description
st.header("Price Prediction")
st.write("The Gurgaon property price prediction algorithm employs machine learning, leveraging key factors like "
         "location, amenities, and market trends to swiftly estimate property prices with high accuracy")
st.page_link("http://localhost:8501/Price_Predictor",label="Price_Predictor",icon="💰")

# Analysis App description
st.header("Analysis App")
st.write("Explore Gurgaon properties effortlessly with our data analysis app, powered by machine learning and "
         "advanced Python. Gain insightful perspectives for informed decisions in real estate")
st.page_link("http://localhost:8501/Analysis_App",label="Analysis App",icon="🔍")

# Recommend Apartments description
st.header("Recommend Apartments")
st.write("Discover your ideal Gurgaon property with our ML-driven recommender system. Tailored suggestions based on "
         "location, landmarks, and societies ensure personalized and efficient real estate choices")
st.page_link("http://localhost:8501/Recommend_Apartments",label="Recommend Apartments",icon="🤝")

st.markdown("---")
# Display a support message with an email contact
st.write("For support, contact us at atulkumarsingh7810@gmail.com")

