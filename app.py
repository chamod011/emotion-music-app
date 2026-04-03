import streamlit as st
from emotion import detect_emotion
from recommender import recommend_songs

st.set_page_config(page_title="Emotion Music App", layout="centered")

st.title("🎧 Emotion-Based Music Recommender")
st.write("Detect your mood using your face and get song suggestions!")

if st.button("📸 Detect Emotion"):
    with st.spinner("Analyzing your face..."):
        emotion = detect_emotion()

    st.success(f"Detected Emotion: {emotion}")

    songs = recommend_songs(emotion)

    st.subheader("🎵 Recommended Songs:")
    for song in songs:
        st.write("👉 " + song)