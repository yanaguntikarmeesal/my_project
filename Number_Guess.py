


import streamlit as st
import random

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Number Guess Game",
    page_icon="🎯",
    layout="centered"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}

/* Header Card */
.header-card {
    background: linear-gradient(135deg, #FFD700, #FFA500);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
}

.header-title {
    font-size: 32px;
    font-weight: bold;
    color: #000000;
}

/* Main Game Card */
.game-card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Secret Number Card */
.secret-card {
    background: rgba(255,255,255,0.10);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 20px;
    border: 2px solid #FFD700;
}

.secret-text {
    font-size: 24px;
    font-weight: bold;
    color: #FFD700;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: bold;
    color: #FFD700;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    color: #EAEAEA;
    margin-top: 10px;
}

/* Input Label */
label {
    color: white !important;
    font-weight: bold !important;
}

/* Success Message */
.success-box {
    background: #28a745;
    padding: 15px;
    border-radius: 10px;
    color: white;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}

/* Info Card */
.info-box {
    background: rgba(255,255,255,0.10);
    padding: 15px;
    border-radius: 10px;
    color: white;
    text-align: center;
    font-size: 18px;
    margin-top: 15px;
}
            


/* Green Buttons */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #28a745, #20c997) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 18px !important;
    font-weight: bold !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.stButton > button:hover {
    background: yellow !important;
    transform: translateY(-2px);
    color: black !important;
}



/* Footer */
.footer{
    text-align:center;
    color:white;
    font-size:16px;
    margin-top:20px;
    padding:15px;
}

.footer a{
    color:#06b6d4;
    text-decoration:none;
    font-weight:bold;
}

.footer a:hover{
    color:#38bdf8;
    text-decoration:underline;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Session State
# -------------------------------
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# -------------------------------
# Header Card
# -------------------------------
st.markdown("""
<div class="header-card">
    <div class="header-title">
        🎮 PROJECT : NUMBER GUESS GAME
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Game Card
# -------------------------------
st.markdown("""
<div class="game-card">
    <div class="title">🎯 Number Guess Game</div>
    <div class="subtitle">
        Guess the secret number between 1 and 100
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Secret Number Card
# -------------------------------
st.markdown(
    f"""
    <div class="secret-card">
        <div class="secret-text">
            🔐 Secret Number : {st.session_state.secret_number}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# User Input
# -------------------------------
guess = st.number_input(
    "Enter Your Guess",
    min_value=1,
    max_value=100,
    step=1
)

# -------------------------------
# Buttons
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    check = st.button("🔍 Check Guess", use_container_width=True)

with col2:
    reset = st.button("🔄 New Game", use_container_width=True)

# -------------------------------
# Guess Logic
# -------------------------------
if check:
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("📉 Too Low! Try a Higher Number.")

    elif guess > st.session_state.secret_number:
        st.warning("📈 Too High! Try a Lower Number.")

    else:
        st.markdown(
            f"""
            <div class="success-box">
                🎉 Congratulations!<br><br>
                You guessed the secret number
                <b>{st.session_state.secret_number}</b>
                in <b>{st.session_state.attempts}</b> attempts.
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------
# Attempts Card
# -------------------------------
st.markdown(
    f"""
    <div class="info-box">
        🎯 Total Attempts : {st.session_state.attempts}
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Reset Game
# -------------------------------
if reset:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("✅ New Game Started Successfully!")

# 
# -------------------------------
# Footer
# -------------------------------
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Developed by <b>Yanaguntikar Meesal</b><br><br>

📧 Yanaguntikarm@gmail.com
</div>
""", unsafe_allow_html=True)