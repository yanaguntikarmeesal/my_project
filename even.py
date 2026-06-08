


# How to run:
# pip install streamlit
# streamlit run even_odd.py

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Even Odd Checker",
    page_icon="🔢",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
}

/* Project Card */
.project-card {
    background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
}

.project-card h1 {
    margin: 0;
    color: white;
    font-size: 2.2rem;
    font-weight: bold;
}

.project-card p {
    margin-top: 10px;
    font-size: 1rem;
    opacity: 0.9;
}

# /* Main Card */
# .card {
#     background: white;
#     padding: 35px;
#     border-radius: 20px;
#     box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
# }

/* Number Input */
.stNumberInput > div > div > input {
    font-size: 22px;
    text-align: center;
    font-weight: bold;
    border-radius: 10px;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
}

/* Result Box */
.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
    color: white;
    font-size: 1.8rem;
    font-weight: bold;
    animation: pop 0.4s ease;
}

.even {
    background: linear-gradient(90deg, #00b09b, #96c93d);
}

.odd {
    background: linear-gradient(90deg, #f093fb, #f5576c);
}

@keyframes pop {
    from {
        opacity: 0;
        transform: scale(0.8);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.footer {
    text-align: center;
    color: #333;
    font-size: 14px;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# Project Name Card
st.markdown("""
<div class="project-card">
    <h1>🔢 EVEN OR ODD NUMBER</h1>
    <p>Check whether a number is Even or Odd instantly</p>
</div>
""", unsafe_allow_html=True)

# Main Card
st.markdown('<div class="card">', unsafe_allow_html=True)

num = st.number_input(
    "Enter a Number",
    value=0,
    step=1,
    format="%d"
)

if st.button("Check Now"):
    
    if num % 2 == 0:
        st.markdown("""
        <div class="result-box even">
            ✅ EVEN NUMBER
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

    else:
        st.markdown("""
        <div class="result-box odd">
            ⚡ ODD NUMBER
        </div>
        """, unsafe_allow_html=True)

st.markdown("### How it Works")
st.markdown("""
- If a number is divisible by **2** with no remainder → **Even Number**
- If a number leaves a remainder of **1** → **Odd Number**
""")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="footer">✨ Enter any integer and find out instantly ✨</div>',
    unsafe_allow_html=True
)

