

import streamlit as st

# Page config - icon, title, layout
st.set_page_config(
    page_title="Multiplication Table Generator",
    page_icon="✖️",
    layout="centered"
)

# Custom CSS for colors + styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
            
    
    /* Primary Application Brand Card */
    .project-card {
        background: linear-gradient(135deg, #ff6a00, #ee0979);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
    }

    .project-card h1 {
        margin: 0;
        color: white;
        font-size: 2.4rem;
        font-weight: bold;
    }

    .project-card p {
        margin-top: 10px;
        font-size: 1rem;
        opacity: 0.95;
    }



    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }


    </style>
""", unsafe_allow_html=True)

# ---------- Header Banner ----------
st.markdown("""
<div class="project-card">
    <h1>✖️ Multiplication Table Generator</h1>
    <p>Enter a number to generate its multiplication table instantly</p>
</div>
""", unsafe_allow_html=True)



# Input section in a nice container
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        num = st.number_input("Enter a number:", min_value=1, max_value=100, value=5, step=1)
    with col2:
        limit = st.number_input("Up to:", min_value=1, max_value=20, value=10, step=1)

# Generate table button
if st.button("Generate Table"):
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader(f"Multiplication Table of {num}")
    
    for i in range(1, limit + 1):
        st.write(f"**{num} × {i} = {num * i}**")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.balloons()

# Footer with credit
st.markdown("---")
st.markdown("🚀 **Developed by Yanaguntikar**")
st.markdown("📧 Yanaguntikarm@gmail.com")