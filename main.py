import Scrape_text
import streamlit as st
import Clean
import transformers
from transformers import pipeline
from transformers.pipelines import base
base.infer_framework_from_model(model=None)

nlp = pipeline("question-answering")
file=open('ML interview.txt','r')
interview=file.read()
interview=Clean.clean_book(interview)




# Project Title
st.header("Welcome to Automated Q&A bot")

# To fetch the query that is the question  
#question=st.text_input('Ask a question here:') 

# To fetch the query that is the question  
question=st.text_input('Ask a question here:') 

st.text(nlp(question=question, context=interview))



