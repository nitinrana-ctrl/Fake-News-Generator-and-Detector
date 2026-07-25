import streamlit as st
from predict import predict_news
from generator import generate_fake_headline, generate_fake_article

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Fake News Generator & Detector",
    page_icon="📰",
    layout="wide"
)

# -------------------- TITLE --------------------

st.title("📰 Fake News Generator & Detector using Generative AI and NLP")

st.markdown("""
### 📌 Project Description

This project consists of two modules:

### 🛡 Fake News Detector
- Uses Natural Language Processing (NLP)
- Uses Machine Learning (Multinomial Naive Bayes)
- Detects whether a news article is **Real** or **Fake**

### ✨ Fake News Generator
- Uses Google's Gemini Generative AI
- Generates fictional fake news headlines
- Created for educational purposes only

---

### 🛠 Technologies Used

- Python
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Google Gemini AI
- Streamlit
""")

# -------------------- TABS --------------------

tab1, tab2 = st.tabs(
    ["🛡 Fake News Detector", "✨ Fake News Generator"]
)

# ======================================================
# DETECTOR TAB
# ======================================================

with tab1:

    st.divider()

    news = st.text_area(
        "📝 Enter News Article",
        height=250,
        placeholder="Paste a complete news article here..."
    )

    if st.button("🔍 Analyze News", use_container_width=True):

        if news.strip() == "":
            st.warning("Please enter a news article.")

        else:

            prediction, confidence = predict_news(news)

            st.divider()

            if "Real" in prediction:
                st.success(prediction)
            else:
                st.error(prediction)

            st.metric(
                "Confidence Score",
                f"{confidence:.2f}%"
            )

            st.progress(min(int(confidence), 100))

            # News Statistics
            word_count = len(news.split())
            char_count = len(news)

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Words", word_count)

            with col2:
                st.metric("Characters", char_count)

            st.subheader("Model Information")

            st.info("""
Machine Learning Model : Multinomial Naive Bayes

Feature Extraction : TF-IDF Vectorizer

Dataset : ISOT Fake & Real News Dataset
""")

# ======================================================
# GENERATOR TAB
# ======================================================

with tab2:

    st.header("✨ Fake News Generator")

    topic = st.text_input(
        "Enter Topic",
        placeholder="Example: Artificial Intelligence"
    )
    
    generation_type = st.radio(
        "Select Generation Type",
        ["Headline", "Short News Article"],
        horizontal=True
    )

    tone = st.selectbox(
        "Select Tone",
        [
            "Shocking",
            "Clickbait",
            "Neutral",
            "Professional"
        ]
    )

    if st.button("✨ Generate Headline", use_container_width=True):

        if topic.strip() == "":
            st.warning("Please enter a topic.")

        else:

            with st.spinner("Generating headline..."):

                if generation_type == "Headline":
                    headline = generate_fake_headline(topic, tone)
                else:
                    headline = generate_fake_article(topic, tone)

            st.success("✅ AI Generated Fake News Headline")

            st.markdown("### 📰 Generated Headline")

            st.markdown(
                f"""
            <div style="
            padding:20px;
            border-radius:10px;
            background-color:#ffffff;
            border-left:6px solid red;
            font-size:20px;
            font-weight:500;
            color:#000000;
            line-height:1.7;
            white-space:pre-wrap;">

            {headline}

            </div>
            """,
                unsafe_allow_html=True,
            )

            st.warning("""
⚠ **Disclaimer**

This headline was generated using **Google Gemini AI**.

It is fictional and intended only for educational purposes.

Do not consider it factual news.
""")

# -------------------- FOOTER --------------------

st.divider()

st.caption(
    "PBEL Internship Project | Fake News Generator & Detector using Generative AI and NLP"
)