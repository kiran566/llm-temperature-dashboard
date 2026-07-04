import streamlit as st
import pandas as pd
import time

from llm import generate_response
from evaluator import (
    calculate_latency,
    word_count,
    consistency_score
)

st.set_page_config(
    page_title="LLM Temperature Dashboard",
    layout="wide"
)

st.title("🌡️ LLM Temperature Experiment Dashboard")

prompt = st.text_area(
    "Enter Prompt",
    height=150,
    value="Explain Retrieval Augmented Generation in simple terms."
)

temperatures = st.multiselect(
    "Select Temperatures",
    [0.0,0.2,0.5,0.7,1.0],
    default=[0.0,0.5,1.0]
)

top_p = st.slider(
    "Top P",
    0.1,
    1.0,
    1.0,
    0.1
)

max_tokens = st.slider(
    "Max Tokens",
    100,
    1000,
    300,
    50
)

if st.button("Run Experiment"):

    results = []

    first_output = None

    for temp in temperatures:

        start = time.time()

        response = generate_response(
            prompt,
            temp,
            top_p,
            max_tokens
        )

        end = time.time()

        text = response["text"]

        latency = calculate_latency(start,end)

        tokens = response["usage"].total_tokens

        words = word_count(text)

        if first_output is None:
            first_output = text

        similarity = consistency_score(
            first_output,
            text
        )

        results.append({

            "Temperature": temp,

            "Latency(s)": latency,

            "Tokens": tokens,

            "Word Count": words,

            "Consistency %": similarity,

            "Response": text

        })

    df = pd.DataFrame(results)

    st.success("Experiment Completed")

    st.dataframe(df)

    st.subheader("Responses")

    for row in results:

        st.markdown(f"## Temperature {row['Temperature']}")

        st.write(f"Latency : {row['Latency(s)']} sec")

        st.write(f"Tokens : {row['Tokens']}")

        st.write(f"Consistency : {row['Consistency %']}%")

        st.write(row["Response"])

        st.divider()