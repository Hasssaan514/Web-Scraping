import streamlit as st
from scrape import scrape_website
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load .env file
load_dotenv()

st.title("AI Web Scraper with Gemini")

url = st.text_input("Enter a website URL")

if st.button("Scrape site"):
    with st.spinner("Scraping website..."):
        html = scrape_website(url)
        st.success("Scraping complete ✅")

        # Use API key from environment
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("❌ GOOGLE_API_KEY not set. Please add it to .env or environment.")
        else:
            # Initialize Gemini
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=api_key
            )

            # Define prompt
            prompt = ChatPromptTemplate.from_template("""
            You are a helpful assistant. I will give you the HTML of a website.
            Extract and summarize the most important information in a structured way:

            - Website Title
            - Main Headings
            - First 5 links (with description if possible)
            - Any contact info (emails, phone numbers)

            HTML:
            {html}
            """)

            # Build chain
            chain = prompt | llm

            # ✅ FIX: Pass dictionary instead of raw string
            response = chain.invoke({"html": html[:6000]})

            st.write("### Extracted Info")
            st.write(response.content)
