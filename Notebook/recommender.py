import pandas as pd
from rapidfuzz import process, fuzz, utils

# stats.csv is pre-aggregated: one row per (condition, drugName) with
# avg_rating, reviews_count, and Bayesian score.
# It's produced offline by cleaning_data.ipynb — see there for the math.
# We commit stats.csv to the repo instead of the 100MB+ raw reviews.
stats = pd.read_csv('data/stats.csv')

conditions = sorted(stats['condition'].unique())

def recommend(condition, top_n=5):
    rows = stats[stats['condition'] == condition]
    rows = rows.sort_values('score', ascending=False).head(top_n)
    return rows[['drugName', 'avg_rating', 'reviews_count', 'score']].reset_index(drop=True)

def match_condition(text, limit=3, cutoff=60):
    hits = process.extract(text, conditions,
                           scorer=fuzz.WRatio,
                           processor=utils.default_process,
                           limit=limit)
    return [name for name, score, _ in hits if score >= cutoff]
