import streamlit as st
from query_handler import classify_query
from query_handler import extract_info
from answer_generator import generate_answer
from recommender import recommend_product
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="E-commerce Chatbot", layout="wide")
st.title(" Smart E-commerce Customer Support Assistant")

user_query = st.text_input("Ask your question:")

if user_query:
    query_type = classify_query(user_query)
    query_data = extract_info(user_query)

    if query_type == "recommendation":
        response = recommend_product(query_data)
    else:
        response = generate_answer(query_type, query_data)

    st.markdown("### Bot Response:")
    st.write(response)
