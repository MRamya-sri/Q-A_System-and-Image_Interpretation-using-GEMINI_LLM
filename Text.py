# we are creating simple Q/A text application using gemini api

from dotenv import load_dotenv
load_dotenv() #loading all env variables

import streamlit as st 
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini model and get responses
model = genai.GenerativeModel("gemini-pro") #for text its gemini-pro
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#setting up streamlit app

st.set_page_config(page_title="Q&A")

st.header("GEMINI LLM APPLICATION")

input= st.text_input('Input: ', key="input")
submit = st.button("Click here for Response to Your Question.")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)