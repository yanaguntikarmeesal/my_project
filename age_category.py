

# How to run:
# pip install streamlit
# streamlit run age_category.py

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Age Category Finder",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Project Name Card */
.project-card {
    background: linear-gradient(135deg, #ff6a00, #ee0979);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.25);
}

.project-card h1 {
    margin: 0;
    color: white;
    font-size: 2.3rem;
    font-weight: bold;
}

.project-card p {
    margin-top: 10px;
    font-size: 1rem;
    opacity: 0.95;
}

# /* Main Card */
# .card {
#     background: white;
#     padding: 35px;
#     border-radius: 25px;
#     box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
# }

/* Input Box */
.stNumberInput > div > div > input {
    font-size: 20px;
    text-align: center;
    font-weight: 600;
    border-radius: 10px;
}

/* Button Styling */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #6a11cb, #2575fc);
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

.stButton > button:active {
    transform: scale(0.98);
}

/* Result Box */
.result-box {
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-top: 25px;
    color: white;
    font-weight: bold;
    animation: fadeIn 0.6s ease;
}

.category {
    font-size: 2.5rem;
    margin: 10px 0;
}

.desc {
    font-size: 1.1rem;
    opacity: 0.95;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.footer {
    text-align: center;
    color: white;
    font-size: 14px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# Project Card
st.markdown("""
<div class="project-card">
    <h1>🎯 AGE CATEGORY FINDER</h1>
    <p>Discover your life stage instantly based on your age</p>
</div>
""", unsafe_allow_html=True)

# Function
def get_age_category(age):
    if age < 13:
        return (
            "Child",
            "Playful, curious, and full of energy!",
            "linear-gradient(90deg, #4facfe 0%, #00f2fe 100%)"
        )

    elif age < 18:
        return (
            "Teenager",
            "Exploring, learning, and growing fast!",
            "linear-gradient(90deg, #fa709a 0%, #fee140 100%)"
        )

    elif age < 35:
        return (
            "Young Adult",
            "Building career and chasing dreams!",
            "linear-gradient(90deg, #43e97b 0%, #38f9d7 100%)"
        )

    elif age < 55:
        return (
            "Adult",
            "Experienced, responsible, and balanced!",
            "linear-gradient(90deg, #f093fb 0%, #f5576c 100%)"
        )

    else:
        return (
            "Senior",
            "Wise, respected, and enjoying life!",
            "linear-gradient(90deg, #ff9a9e 0%, #fecfef 100%)"
        )

# Main Card
st.markdown('<div class="card">', unsafe_allow_html=True)

age = st.number_input(
    "Enter Your Age",
    min_value=0,
    max_value=120,
    step=1
)

if st.button("Find My Category", use_container_width=True):

    category, description, gradient = get_age_category(age)

    st.markdown(
        f"""
        <div class="result-box" style="background:{gradient};">
            <div>You are a</div>
            <div class="category">{category}</div>
            <div class="desc">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("### 📌 Age Categories")

st.markdown("""
- **0 - 12 years** → Child
- **13 - 17 years** → Teenager
- **18 - 34 years** → Young Adult
- **35 - 54 years** → Adult
- **55+ years** → Senior
""")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    '<div class="footer">✨ Enter your age and discover your category instantly ✨</div>',
    unsafe_allow_html=True
)

