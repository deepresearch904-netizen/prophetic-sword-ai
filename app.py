import streamlit as st
import google.generativeai as genai
import os

# গিটহাব সিক্রেটস থেকে API Key সংগ্রহ করা হবে
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

st.set_page_config(
    page_title="Prophetic Sword AI",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Majestic Dark Prophetic Styling
st.markdown("""
<style>
    .stApp {
        background-color: #0b0c10;
        color: #c5c6c7;
    }
    h1, h2, h3 {
        color: #66fcf1 !important;
        font-family: 'Cinzel', serif, Georgia;
    }
    .stSidebar {
        background-color: #1f2833 !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1f2833, #45a29e);
        color: white;
        border: 1px solid #66fcf1;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

PROPHETIC_SWORD_SYSTEM_PROMPT = """
You are the "PROPHETIC SWORD AI" (প্রভাবশালী ভবিষ্যদ্বাণীমূলক তরবারি).
Your foundation is Hebrews 4:12 — "For the word of God is quick, and powerful, and sharper than any twoedged sword, piercing even to the dividing asunder of soul and spirit, and of the joints and marrow, and is a discerner of the thoughts and intents of the heart."

CORE PERSONA RULES:
1. UNAPOLOGETIC BIBLICAL FIRE: You speak with the authority, gravity, and unflinching conviction of an Old Testament Prophet (like Elijah, Isaiah, Jeremiah) and an early Apostle (like John the Baptist).
2. MASTER-LEVEL EXEGESIS: Every answer must cut to the bone. You despise lukewarm theological compromise.
3. UNSHAKABLE BIBLICAL ANCHOR: Cite Scripture (Book, Chapter, Verse) explicitly. Explain the text in its rigorous grammatical-historical context.
4. LINGUISTIC PRECISION: Expose the original Hebrew (Tanakh) or Greek (Koine) root words and grammatical nuance (e.g., Hesed, Shalom, Logos, Metanoia).
5. TONE: Solemn, majestic, piercing, righteous, commanding.

Language Instruction: Deliver responses primarily in rich, powerful Bengali (উচ্চমার্গীয় ও শাণিত ভাষা).
"""

# Sidebar
with st.sidebar:
    st.title("⚔️ PROPHETIC SWORD")
    st.caption('"Sharper than any two-edged sword" (Heb 4:12)')
    st.markdown("---")
    
    mode = st.radio(
        "নির্বাচন করুন মোড:",
        [
            "🔥 Prophetic Exegesis",
            "🏛️ Parallel Bible & Roots"
        ]
    )
    
    st.markdown("---")
    st.markdown("**Core Philosophy:**\nএখানে কোনো মনভোলানো আপস নেই। কেবল শাস্ত্রের সরাসরি সত্য।")

if not GEMINI_API_KEY:
    st.error("⚠️ GEMINI_API_KEY পাওয়া যায়নি! দয়া করে Streamlit Secrets-এ কি যুক্ত করুন।")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-3.6-flash",
    system_instruction=PROPHETIC_SWORD_SYSTEM_PROMPT
)

# ----------------- 1. Prophetic Exegesis -----------------
if mode == "🔥 Prophetic Exegesis":
    st.title("🔥 The Prophetic Sword")
    st.write("যেকোনো ভ্রান্ত মতবাদ, আধুনিক নৈতিক দ্বিধা বা ধর্মতাত্ত্বিক প্রশ্ন উত্থাপন করুন। শাস্ত্রীয় খড়্গ তার প্রকৃত মুখোশ উন্মোচন করবে।")
    
    user_query = st.text_area("আপনার প্রশ্ন বা বিষয়বস্তু লিখুন:", height=120, placeholder="যেমন: আধুনিক সমাজে সমৃদ্ধি সুসমাচার কেন আত্মিক বিষ?")
    
    if st.button("সত্যের শাণিত জবাব নিন ⚔️"):
        if not user_query.strip():
            st.warning("অনুগ্রহ করে কোনো প্রশ্ন বা শাস্ত্রীয় বিষয় লিখুন!")
        else:
            with st.spinner("শাস্ত্রীয় হাড়-মজ্জা চিরে সত্য উন্মোচিত হচ্ছে..."):
                try:
                    response = model.generate_content(user_query)
                    st.markdown("### ⚖️ The Divine Verdict:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"সার্ভার ত্রুটি: {str(e)}")

# ----------------- 2. Parallel Bible & Roots -----------------
elif mode == "🏛️ Parallel Bible & Roots":
    st.title("🏛️ Parallel Bible & Linguistic Roots")
    st.write("নির্দিষ্ট কোনো পদ লিখুন। সিস্টেম KJV ও ESV-র আলোকে এবং মূল হিব্রু/গ্রিক ভাষার আভিধানিক অর্থ বিশ্লেষণ করবে।")
    
    verse_input = st.text_input("পদের নাম লিখুন:", placeholder="যেমন: John 1:1, Genesis 1:1, Romans 8:1")
    
    if st.button("মূল শেকড় ব্যবচ্ছেদ করুন 🌿"):
        if not verse_input.strip():
            st.warning("পদের নাম উল্লেখ করুন!")
        else:
            with st.spinner("হিব্রু এবং গ্রিক টেক্সটের গভীরে যাওয়া হচ্ছে..."):
                prompt = f"""
                [TASK: DEEP EXEGESIS & ROOT ANALYSIS]
                Analyze the following Scripture reference: "{verse_input}"
                Structure response into:
                1. ⚔️ **Parallel Translations (KJV & ESV Context)**
                2. 📜 **Root Analysis (Hebrew / Koine Greek Lexicon)**
                3. 🔥 **Prophetic Piercing Exegesis**
                4. ⚖️ **The Verdict of Truth**
                """
                try:
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"সার্ভার ত্রুটি: {str(e)}")
