import streamlit as st
import pandas as pd
import time
import plotly.express as px

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

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Experiment Settings")

prompt = st.sidebar.text_area(
    "Prompt",
    value="Explain Retrieval Augmented Generation in simple terms.",
    height=150
)

temperatures = st.sidebar.multiselect(
    "Temperatures",
    [0.0, 0.2, 0.5, 0.7, 1.0],
    default=[0.0, 0.5, 1.0]
)

top_p = st.sidebar.slider(
    "Top-P",
    0.1,
    1.0,
    1.0,
    0.1
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    100,
    1000,
    300,
    50
)

run = st.sidebar.button("🚀 Run Experiment")

# -----------------------------
# Run Experiment
# -----------------------------
if run:

    results = []
    first_output = None

    for temp in temperatures:

        start = time.time()

        response = generate_response(
            prompt=prompt,
            temperature=temp,
            top_p=top_p,
            max_tokens=max_tokens
        )

        end = time.time()

        text = response["text"]

        latency = calculate_latency(start, end)

        tokens = response["usage"].total_tokens

        words = word_count(text)

        if first_output is None:
            first_output = text

        similarity = consistency_score(
            first_output,
            text
        )

        results.append(
            {
                "Temperature": temp,
                "Latency(s)": latency,
                "Tokens": tokens,
                "Word Count": words,
                "Consistency %": similarity,
                "Response": text
            }
        )

    df = pd.DataFrame(results)

    # -----------------------------
    # Metrics
    # -----------------------------
    st.success("✅ Experiment Completed")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Experiments",
        len(df)
    )

    col2.metric(
        "Average Tokens",
        int(df["Tokens"].mean())
    )

    col3.metric(
        "Average Latency",
        round(df["Latency(s)"].mean(), 2)
    )

    col4.metric(
        "Best Consistency",
        f"{df['Consistency %'].max()}%"
    )

    # -----------------------------
    # Summary Table
    # -----------------------------
    st.subheader("📊 Experiment Summary")

    summary_df = df.drop(columns=["Response"])

    st.dataframe(
        summary_df,
        use_container_width=True
    )
    # -----------------------------
    # Charts
    # -----------------------------
    st.subheader("📊 Experiment Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            df,
            x="Temperature",
            y="Latency(s)",
            text="Latency(s)",
            title="Latency vs Temperature"
        )

        fig.update_layout(height=400)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:
        fig = px.bar(
            df,
            x="Temperature",
            y="Tokens",
            text="Tokens",
            title="Token Usage"
        )

        fig.update_layout(height=400)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    with col3:
        fig = px.line(
            df,
            x="Temperature",
            y="Word Count",
            markers=True,
            title="Word Count vs Temperature"
        )

        fig.update_layout(height=400)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col4:
        fig = px.line(
            df,
            x="Temperature",
            y="Consistency %",
            markers=True,
            title="Consistency vs Temperature"
        )

        fig.update_layout(height=400)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -----------------------------
    # Best Configuration
    # -----------------------------
    best = df.sort_values(
        by="Consistency %",
        ascending=False
    ).iloc[0]

    st.success(
        f"""
### 🏆 Best Configuration

- **Temperature:** {best['Temperature']}
- **Consistency:** {best['Consistency %']}%
- **Latency:** {best['Latency(s)']} sec
- **Tokens:** {best['Tokens']}
"""
    )

    # -----------------------------
    # Download CSV
    # -----------------------------
    csv = summary_df.to_csv(index=False)

    st.download_button(
        label="⬇ Download Results CSV",
        data=csv,
        file_name="temperature_experiment_results.csv",
        mime="text/csv"
    )

    # -----------------------------
    # Responses
    # -----------------------------
    st.subheader("💬 Model Responses")

    for row in results:

        with st.expander(
            f"Temperature {row['Temperature']}"
        ):

            st.write(f"**Latency:** {row['Latency(s)']} sec")
            st.write(f"**Tokens:** {row['Tokens']}")
            st.write(f"**Word Count:** {row['Word Count']}")
            st.write(f"**Consistency:** {row['Consistency %']}%")

            st.markdown("---")

            st.write(row["Response"])