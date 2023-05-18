import openai
import pandas as pd
import streamlit as st
from datetime import datetime

# Set up OpenAI API credentials
openai.api_key = ""

# Load the sample questions and answers from the text file
with open("train_dataset.txt", "r") as file:
    qa_pairs = file.read().splitlines()

# Load the additional data from the CSV file into a DataFrame
df = pd.read_excel('dummy_data.xlsx')

# Define a function to query the chatbot
def ask_chatbot(question):
    # Append the question to the existing QA pairs
    qa_pairs.append(f"Question: {question}")

    # Generate a response from the chatbot
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="\n".join(qa_pairs),
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the answer from the response
    answer = response.choices[0].text.strip().split(": ")[-1]

    # Return the answer
    return answer

# # Streamlit app
# st.title("Chatbot App")

# # Display the welcome message
# st.write("Chatbot: Hi! I'm here to help. Feel free to ask me any questions.")

# # User input
# user_input = st.text_input("User")

# if user_input:
#     answer = ask_chatbot(user_input)
#     st.write("Chatbot:", answer)
