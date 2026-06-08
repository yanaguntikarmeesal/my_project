

import streamlit as st

st.set_page_config(
    page_title="India States & Capitals",
    page_icon="🇮🇳",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #ff9933 0%,
        #ffffff 50%,
        #138808 100%
    );
}

/* Header Card */
.header-card {
    background: linear-gradient(135deg,#FF6B35,#FFB347,#138808);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.25);
}

.header-card h1 {
    margin: 0;
    color: white;
    font-size: 2.3rem;
}


/* Output Box */
.capital-box {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.2);
}

.capital-name {
    font-size: 2.5rem;
    font-weight: bold;
    color: #FFD700;
}



</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-card">
    <h1> INDIA STATE TO CAPITAL FINDER</h1>
</div>
""", unsafe_allow_html=True)

# State-Capital Mapping
state_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata",
    "Delhi": "New Delhi",
    "Puducherry": "Puducherry",
    "Chandigarh": "Chandigarh",
    "Jammu and Kashmir": "Srinagar",
    "Ladakh": "Leh"
}

# Main Card
st.markdown('<div class="main-card">', unsafe_allow_html=True)

selected_state = st.selectbox(
    "Select State / Union Territory",
    sorted(state_capitals.keys())
)

if selected_state:
    capital = state_capitals[selected_state]

    st.markdown(
        f"""
        <div class="capital-box">
            <div class="capital-name">{capital}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("🚀 **Developed by Yanaguntikar**")
st.markdown("📧 Yanaguntikarm@gmail.com")