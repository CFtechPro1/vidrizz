import streamlit as st
import time

# -------------------------------
# Title and Intro
# -------------------------------
st.set_page_config(page_title="Vidrizz - Viral Video Generator", layout="centered")
st.title("🎬 Vidrizz - Viral Video Generator for Creators")
st.markdown("Turn your ideas into viral-ready videos using AI. Just drop a topic, and we'll handle script, visuals, voice, and music.")

# -------------------------------
# User Input Section
# -------------------------------
prompt = st.text_area("💡 Your idea, tweet, or topic:", placeholder="e.g. Why most people fail at side hustles")

col1, col2 = st.columns(2)
with col1:
    platform = st.selectbox("📱 Platform", ["YouTube Shorts", "TikTok", "Instagram Reels"])
    aspect_ratio = st.selectbox("📐 Aspect Ratio", ["9:16 (Vertical)", "1:1 (Square)", "16:9 (Wide)"])
    caption_style = st.selectbox("💬 Caption Style", ["Bold & Centered", "Bottom Subtitle", "TikTok Style"])
with col2:
    voice = st.selectbox("🎙️ Voice Style", ["Narrator", "Female Creator", "TikTok Voice"])
    music_style = st.selectbox("🎵 Music Style", ["Chill", "Upbeat", "Cinematic", "None"])
    hook_style = st.selectbox("🚀 Hook Style", ["Question", "Surprising Fact", "Controversial Statement"])

# -------------------------------
# Optional Branding & CTA
# -------------------------------
st.markdown("### ✍️ Personal Branding")
with st.expander("Add your logo, watermark, or CTA overlay"):
    logo_url = st.text_input("🔗 Logo or Watermark URL")
    cta_text = st.text_input("📣 Call-to-Action (e.g. Follow for more!)")

# -------------------------------
# Generate Button
# -------------------------------
if st.button("🚀 Generate Video"):
    if not prompt:
        st.warning("Please enter a topic or idea to start.")
    else:
        with st.spinner("Generating your video using AI magic..."):
            time.sleep(3)  # Simulate processing time
            st.success("✅ Your video is ready!")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            st.download_button("⬇️ Download Video", data=b"fake_video_bytes", file_name="vidrizz_video.mp4")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Made with ❤️ for creators. [Vidrizz.com](http://vidrizz.com)")
