# Drugs-Recommendation-
Chatbot that recommends medications for a condition using Bayesian weighted rankings over 215k real patient reviews. Built with Python, pandas, RapidFuzz &amp; Streamlit.


A simple chatbot that recommends medications for a given condition, based on
~215k real patient reviews from Drugs.com. Type a condition (e.g. "I have a
headache") and it returns the best-rated drugs for it.
⚠️ Educational project only — NOT medical advice.

# How it works
Bayesian weighted score ranks drugs by rating adjusted for how many
reviews they have, so a drug with a single 10/10 review can't beat a
well-tested one.
Fuzzy matching maps free-form text to a known condition.
Streamlit provides the chat interface.

# Run it locally
pip install -r requirements.txt
streamlit run app.py
​
Then open the URL Streamlit prints (usually http://localhost:8501).
# Project structure
app.py            # Streamlit chat UI
recommender.py    # recommend() + match_condition()
data/stats.csv    # precomputed drug stats (condition, drug, rating, score)
requirements.txt  # dependencies
​
# Data
Source: Drugs.com review dataset (UCI Machine Learning Repository). The raw
review files are large and not stored here; the app uses the precomputed
data/stats.csv.
