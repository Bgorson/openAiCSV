from tempfile import NamedTemporaryFile

import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os


def main():
    load_dotenv()

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV")

    file = st.file_uploader("upload file", type="csv")

    if file:
        # Specify your custom temporary directory
        custom_temp_dir = "C:/Users/Maverick/Documents/coding/pythonGPT/temp"
        with NamedTemporaryFile(delete=False, mode='w+b', dir=custom_temp_dir, suffix=".csv") as f:
            f.write(file.getvalue())
            f.flush()
            llm = OpenAI(temperature=0)
            user_input = st.text_input("Question here:")
            agent = create_csv_agent(llm, f.name, verbose=True)
            if user_input:
                response = agent(user_input)
                st.write(response)


if __name__ == "__main__":
    main()