# we are creating simple Image identification application using gemini api

from dotenv import load_dotenv
load_dotenv() #loading all env variables

import streamlit as st 
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini model and get responses
model = genai.GenerativeModel("gemini-1.5-flash") #for image its gemini-pro-vision
def get_gemini_response(image):
        response= model.generate_content(image)
        return response.text

## initialize streamlit app
st.set_page_config(page_title="Image_Identification")

st.header("GEMINI APPLICATION")
st.subheader("Upload an Image to get Interpretation")

uploaded_file = st.file_uploader("Choose an Image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Interpret about Image.")

if submit:
    response = get_gemini_response(image)
    st.subheader("The Response is")
    st.write(response)
