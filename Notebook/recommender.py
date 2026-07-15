import pandas as pd
from rapidfuzz import process, fuzz, utils

# --- load the cleaned data (Step 5A saved this) ---
df = pd.read_csv('data/clean_reviews.csv')

# --- Phase 1: stats table (one row per condition+drug) ---
stats = (
    df.groupby(['condition', 'drugName'])
      .agg(
          avg_rating=('rating', 'mean'),
          reviews_count=('rating', 'count'),
      )
      .reset_index()
)

# --- Phase 2: Bayesian score ---
C = df['rating'].mean()      # global average (anchor)
m = 25                       # trust threshold
v = stats['reviews_count']
R = stats['avg_rating']
stats['score'] = (v / (v + m)) * R + (m / (v + m)) * C


# --- list of known conditions (for matching) ---
conditions = sorted(stats['condition'].unique())

# --- Phase 3: recommend drugs for a condition ---
def recommend(condition, top_n=5):
    rows = stats[stats['condition'] == condition]
    rows = rows.sort_values('score', ascending=False).head(top_n)
    return rows[['drugName', 'avg_rating', 'reviews_count', 'score']].reset_index(drop=True)

# --- Phase 4: match free text to a condition ---
def match_condition(text, limit=3, cutoff=60):
    hits = process.extract(text, conditions,
                           scorer=fuzz.WRatio,
                           processor=utils.default_process,
                           limit=limit)
    return [name for name, score, _ in hits if score >= cutoff]
