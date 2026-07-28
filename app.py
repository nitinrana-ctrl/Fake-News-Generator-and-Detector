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


left, right = st.columns(2)

with left:
    st.subheader("🔍 Detector")

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

            if "Real" in prediction:
                st.success(prediction)
            else:
                st.error(prediction)

            st.metric(
                "🎯 Prediction Confidence",
                f"{confidence:.2f}%"
            )

            st.progress(min(int(confidence), 100))

            col1, col2 = st.columns(2)

            with col1:
                st.metric("📝 Words", len(news.split()))

            with col2:
                st.metric("🔠 Characters", len(news))


with right:
    st.subheader("✨ Generator")

    topic = st.text_input(
        "🎯 Topic",
        placeholder="Example: Artificial Intelligence"
    )

    generation_type = st.radio(
        "Generation Type",
        ["Headline", "Short News Article"],
        horizontal=True
    )

    tone = st.selectbox(
        "Tone",
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

           with st.spinner("Generating..."):

            if generation_type == "Headline":
                content = generate_fake_headline(topic, tone)
            else:
                content = generate_fake_article(topic, tone)

        # Check if generation failed
        if content.startswith("⚠️"):

            st.error(content)

        else:

            st.success("✅ Content Generated Successfully")

            st.markdown("### 📰 Generated Content")

            st.markdown(
                f"""
        <div style="
        padding:20px;
        border-radius:10px;
        background-color:#ffffff;
        border-left:6px solid #ff9800;
        font-size:20px;
        font-weight:500;
        color:#000000;
        line-height:1.7;
        white-space:pre-wrap;">

        {content}

        </div>
        """,
                unsafe_allow_html=True,
            )

            st.warning(
                "⚠️ This content is AI-generated and intended only for educational purposes."
            )