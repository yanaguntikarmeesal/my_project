

# How to run:
# pip install streamlit
# streamlit run age_calculator.py

import streamlit as st
from datetime import date
import calendar

# Page Configuration
st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Project Card */
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
    font-size: 2.4rem;
    font-weight: bold;
}

.project-card p {
    margin-top: 10px;
    font-size: 1rem;
    opacity: 0.95;
}

# /* Calculator Card */
# .calc-card {
#     background: white;
#     padding: 35px;
#     border-radius: 20px;
#     box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
# }

/* Input Styling */
.stSelectbox label {
    font-weight: 600;
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
    background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
    color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
    animation: fadeIn 0.5s ease;
}

.age-text {
    font-size: 2rem;
    font-weight: bold;
    margin: 10px 0;
}

.label {
    font-size: 1rem;
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

/* Footer */
.footer {
    text-align: center;
    color: white;
    margin-top: 20px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# Project Name Card
st.markdown("""
<div class="project-card">
    <h1>🎂 AGE CALCULATOR</h1>
    <p>Calculate your exact age in Years, Months, and Days</p>
</div>
""", unsafe_allow_html=True)

# Age Calculation Function
def calculate_age(birth_date, today):
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1

        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year

        days += calendar.monthrange(prev_year, prev_month)[1]

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Main Calculator Card
st.markdown('<div class="calc-card">', unsafe_allow_html=True)

st.subheader("📅 Select Your Date of Birth")

today = date.today()

col1, col2, col3 = st.columns(3)

with col1:
    year = st.selectbox(
        "Year",
        range(today.year, 1899, -1)
    )

with col2:
    month = st.selectbox(
        "Month",
        range(1, 13),
        format_func=lambda x: calendar.month_name[x]
    )

with col3:
    max_day = calendar.monthrange(year, month)[1]
    day = st.selectbox(
        "Day",
        range(1, max_day + 1)
    )

if st.button("Calculate My Age", use_container_width=True):

    try:
        birth_date = date(year, month, day)

        if birth_date > today:
            st.error("❌ Birth date cannot be in the future!")

        else:
            years, months, days = calculate_age(
                birth_date,
                today
            )

            total_days = (today - birth_date).days

            st.markdown(
                f"""
                <div class="result-box">
                    <div class="label">You are</div>
                    <div class="age-text">
                        {years} Years, {months} Months, {days} Days
                    </div>
                    <div class="label">
                        Total: {total_days:,} days old
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    except ValueError:
        st.error("❌ Invalid date selected!")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    '<div class="footer">✨ Find your exact age instantly ✨</div>',
    unsafe_allow_html=True
)




st.markdown("---")
st.markdown("🚀 **Developed by Yanaguntikar**")
st.markdown("📧 Yanaguntikarm@gmail.com")





