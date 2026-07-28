import streamlit as st
from predict import predict_news
from generator import generate_fake_headline, generate_fake_article

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Fake News Generator & Detector",
    page_icon="📰",
    layout="wide"
)

# -------------------- HEADER --------------------

st.caption("📚 PBEL Internship Project")

st.title("📰 Fake News Generator & Detector")

st.markdown("""
#### Detect **Fake or Real News** using Machine Learning or generate
AI-powered fake news using **Google Gemini AI**.
""")

st.caption("Python • NLP • TF-IDF • Multinomial Naive Bayes • Google Gemini AI")

st.divider()

# -------------------- TABS --------------------

tab1, tab2 = st.tabs(
    ["🔍 Detector", "✨ Generator"]
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

    if st.button("🔍 Analyze", use_container_width=True):

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
                "🎯 Prediction Confidence",
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

    if st.button("✨ Generate", use_container_width=True):

        if topic.strip() == "":
            st.warning("Please enter a topic.")

        else:

            with st.spinner("Generating headline..."):

                if generation_type == "Headline":
                    headline = generate_fake_headline(topic, tone)
                else:
                    headline = generate_fake_article(topic, tone)

            st.success("✅ Content Generated Successfully")

            st.markdown("### 📰 Generated Content")

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

st.markdown("""
<style>
.dev-badge{position:fixed;bottom:18px;right:18px;background:#262730;color:white;padding:10px 16px;border-radius:12px;font-size:13px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.3);z-index:999;}
.dev-badge span{color:#d0d0d0;font-size:12px;}
</style>
<div class="dev-badge"><span>Developed by</span><br><b>Nitin Rana</b></div>
""", unsafe_allow_html=True)
