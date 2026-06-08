

# How to use:
# pip install streamlit
# streamlit run gk_quiz.py


import streamlit as st
import random
import time

st.set_page_config(page_title="India GK Quiz", page_icon="🇮🇳", layout="centered")

# Custom CSS for beautiful layout
st.markdown("""
    <style>
.main {background: linear-gradient(135deg, #ff9933 0%, #ffffff 50%, #138808 100%); min-height: 100vh;}
    h1 {text-align: center; color: #2c3e50; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);}
# .quiz-card {
#         background-color: white;
#         padding: 30px;
#         border-radius: 20px;
#         box-shadow: 0 8px 16px rgba(0,0,0,0.15);
#         margin-top: 20px;
#     }
.question-text {font-size: 1.3em; font-weight: 600; color: #2c3e50; margin-bottom: 20px;}
.stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 12px;
        padding: 12px;
        font-size: 16px;
        font-weight: 600;
        border: none;
        transition: all 0.3s;
    }
.stButton>button:hover {transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.2);}
.score-box {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.2em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🇮🇳 India General Knowledge Quiz")

# India GK Q&A - Add more to reach 100
QUESTIONS = [
    {"q": "What is the capital of India?", "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"], "ans": "New Delhi"},
    {"q": "Who is known as the Father of the Nation?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "B.R. Ambedkar"], "ans": "Mahatma Gandhi"},
    {"q": "Which is the longest river in India?", "options": ["Yamuna", "Brahmaputra", "Ganga", "Godavari"], "ans": "Ganga"},
    {"q": "In which year did India gain independence?", "options": ["1945", "1947", "1950", "1930"], "ans": "1947"},
    {"q": "What is the national animal of India?", "options": ["Lion", "Tiger", "Elephant", "Peacock"], "ans": "Tiger"},
    {"q": "Which city is called the Silicon Valley of India?", "options": ["Mumbai", "Delhi", "Bengaluru", "Hyderabad"], "ans": "Bengaluru"},
    {"q": "Who wrote the Indian national anthem?", "options": ["Bankim Chandra", "Rabindranath Tagore", "Sarojini Naidu", "Muhammad Iqbal"], "ans": "Rabindranath Tagore"},
    {"q": "Which state has the largest population?", "options": ["Maharashtra", "Uttar Pradesh", "Bihar", "West Bengal"], "ans": "Uttar Pradesh"},
    {"q": "What is the national currency of India?", "options": ["Rupee", "Dollar", "Taka", "Yuan"], "ans": "Rupee"},
    {"q": "Which monument is known as the symbol of love?", "options": ["Qutub Minar", "India Gate", "Taj Mahal", "Red Fort"], "ans": "Taj Mahal"},
    {"q": "Who was the first Prime Minister of India?", "options": ["Atal Bihari Vajpayee", "Jawaharlal Nehru", "Indira Gandhi", "Lal Bahadur Shastri"], "ans": "Jawaharlal Nehru"},
    {"q": "Which is the largest state by area in India?", "options": ["Rajasthan", "Madhya Pradesh", "Maharashtra", "Uttar Pradesh"], "ans": "Rajasthan"},
    {"q": "What is the national sport of India?", "options": ["Cricket", "Hockey", "Football", "Kabaddi"], "ans": "Hockey"},
    {"q": "Which planet is called the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "ans": "Mars"},
    {"q": "In which city is the Golden Temple located?", "options": ["Delhi", "Amritsar", "Varanasi", "Haridwar"], "ans": "Amritsar"},
]

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'q_num' not in st.session_state:
    st.session_state.q_num = 0
if 'shuffled_q' not in st.session_state:
    st.session_state.shuffled_q = random.sample(QUESTIONS, len(QUESTIONS))
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'quiz_over' not in st.session_state:
    st.session_state.quiz_over = False

# Quiz logic
if st.session_state.quiz_over:
    st.markdown(f'<div class="score-box">🎉 Quiz Over! Your Score: {st.session_state.score}/{len(QUESTIONS)}</div>', unsafe_allow_html=True)
    if st.button("Restart Quiz"):
        for key in ['score', 'q_num', 'shuffled_q', 'answered', 'quiz_over']:
            del st.session_state[key]
        st.rerun()
else:
    current_q = st.session_state.shuffled_q[st.session_state.q_num]

    st.markdown(f'<div class="quiz-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="score-box">Question {st.session_state.q_num + 1}/{len(QUESTIONS)} | Score: {st.session_state.score}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="question-text">{current_q["q"]}</div>', unsafe_allow_html=True)

    # Display options as buttons
    for option in current_q["options"]:
        if st.button(option, key=option, disabled=st.session_state.answered):
            st.session_state.answered = True
            if option == current_q["ans"]:
                st.session_state.score += 1
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! Correct answer: {current_q['ans']}")
            time.sleep(1.5)
            st.session_state.q_num += 1
            st.session_state.answered = False
            if st.session_state.q_num >= len(QUESTIONS):
                st.session_state.quiz_over = True
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)



st.markdown("---")
st.markdown("🚀 **Developed by Yanaguntikar**")
st.markdown("📧 Yanaguntikarm@gmail.com")


