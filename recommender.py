import pandas as pd

df = pd.read_csv("songs.csv")

def recommend_songs(emotion):
    filtered = df[df['emotion'] == emotion]

    if filtered.empty:
        return ["No songs found"]

    results = []
    for _, row in filtered.head(5).iterrows():
        results.append(f"{row['song']} - {row['artist']}")

    return results