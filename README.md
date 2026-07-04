# 🌡️ LLM Temperature Experiment Dashboard

An interactive dashboard for evaluating how different **LLM inference parameters** influence response quality, latency, token usage, and consistency. The application enables prompt engineers and AI developers to perform controlled experiments by varying **temperature**, **top-p**, and **max tokens**, then visualizing the impact through interactive charts and experiment metrics.

---

## 🚀 Features

* Compare LLM responses across multiple temperature values
* Configure inference parameters:

  * Temperature
  * Top-p
  * Max Tokens
* Measure response latency
* Track total token usage
* Calculate response word count
* Compare response consistency across different temperatures
* Interactive visualizations using Plotly
* Automatic best-configuration recommendation
* Download experiment results as CSV
* Expandable view for generated responses

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API
* Plotly
* Pandas
* python-dotenv

---

## 📂 Project Structure

```text
llm-temperature-dashboard/
│
├── app.py               # Streamlit dashboard
├── llm.py               # Groq API integration
├── evaluator.py         # Evaluation metrics
├── test.py              # API testing script
├── requirements.txt
├── .env                 # API Key (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. Enter a prompt.
2. Select one or more temperature values.
3. Configure **Top-p** and **Max Tokens**.
4. Run the experiment.
5. The application sends the prompt to the selected LLM for each temperature.
6. Responses are evaluated using multiple metrics.
7. Results are displayed as tables and interactive charts.

---

## 📊 Evaluation Metrics

The dashboard evaluates every experiment using the following metrics:

* **Latency** – Time taken to generate a response.
* **Token Usage** – Total tokens consumed by the model.
* **Word Count** – Number of words in the generated response.
* **Consistency Score** – Text similarity between responses generated with different temperatures.

---

## 📈 Visualizations

The dashboard provides interactive charts for:

* Latency vs Temperature
* Token Usage vs Temperature
* Word Count vs Temperature
* Consistency vs Temperature

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/llm-temperature-dashboard.git
```

Move into the project directory:

```bash
cd llm-temperature-dashboard
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## 📷 Dashboard Preview

Add screenshots here after running the application.

* Dashboard Home
* Experiment Results
* Charts
* Best Configuration
* Response Comparison

---

## 🎯 Learning Outcomes

This project demonstrates practical understanding of:

* LLM inference parameter tuning
* Prompt experimentation
* Temperature sampling
* Response evaluation
* Latency analysis
* Token analysis
* Prompt consistency measurement
* Interactive AI dashboards
* Prompt engineering workflows

---

## 🔮 Future Improvements

* Model comparison (Llama, Qwen, Gemma, DeepSeek)
* Prompt A vs Prompt B evaluation
* Experiment history
* PDF report generation
* JSON export
* Automated benchmark reports

---

## 👨‍💻 Author

**Kiran Basava**

AI • Machine Learning • Generative AI • LLM Applications
