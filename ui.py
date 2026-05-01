import streamlit as st
from youtube_analyzer import youtube_analyzer

st.set_page_config(
    page_title="AI YouTube Video Analyzer",
    page_icon="🎥",
    layout="wide",
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
}
.title {
    font-size: 42px;
    font-weight: 800;
    color: white;
}
.subtitle {
    color: #bdbdbd;
    font-size: 18px;
}
.result-box {
    background: #111;
    padding: 25px;
    border-radius: 18px;
    border-left: 5px solid #ff0000;
}
.stButton button {
    background: #ff0000;
    color: white;
    border-radius: 10px;
    padding: 10px 25px;
    font-weight: 700;
    border: none;
}
.stTextInput input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_agent():
    return youtube_analyzer()


with st.sidebar:
    st.title("⚙️ Analyzer Options")
    st.markdown("Choose what you want from the video.")

    analyze_type = st.radio(
        "Analysis Type",
        [
            "Full Video Analysis",
            "Short Summary",
            "Important Timestamps",
            "Key Points",
            "Content Ideas"
        ]
    )

    st.markdown("---")
    st.info("Paste any YouTube video URL and click Analyze.")


st.markdown('<div class="title">🎥 AI YouTube Video Analyzer</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Analyze YouTube videos using AI — summary, timestamps, key points and insights.</p>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    video_url = st.text_input(
        "Enter YouTube Video Link",
        placeholder="https://www.youtube.com/watch?v=..."
    )

    analyze_button = st.button("🚀 Analyze Video", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✨ Features")
    st.markdown("""
    - Video summary  
    - Topic breakdown  
    - Timestamp analysis  
    - Key learning points  
    - Content insights  
    """)
    st.markdown('</div>', unsafe_allow_html=True)


if analyze_button:
    if not video_url.strip():
        st.warning("Please enter a YouTube video link.")
    elif "youtube.com" not in video_url and "youtu.be" not in video_url:
        st.error("Please enter a valid YouTube URL.")
    else:
        agent = get_agent()

        prompt = f"""
        Analyze this YouTube video: {video_url}

        Analysis type: {analyze_type}

        Give output in clean markdown format.
        """

        with st.spinner("Analyzing video... Please wait."):
            try:
                response = agent.run(prompt)

                st.success("Analysis complete!")

                st.markdown("## 📌 Analysis Result")
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown(response.content)
                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error("Something went wrong while analyzing the video.")
                st.code(str(e))