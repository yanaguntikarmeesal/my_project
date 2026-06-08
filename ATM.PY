

import streamlit as st

# Initial balance setup using session state
if "balance" not in st.session_state:
    st.session_state.balance = 100

# ---------- CSS DESIGN ELEMENTS ----------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
            
    /* Background Application Window */
    .stApp {
        background: #fdfdfd;
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

    /* Core Balance Box Layout */
    .balance-box {
        background-color: #dff0d8;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        color: #2e7d32;
        margin-bottom: 20px;
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }

    .success-msg {
        color: green;
        font-weight: bold;
        font-size: 1.1rem;
    }

    .error-msg {
        color: red;
        font-weight: bold;
        font-size: 1.1rem;
    }

    /* Form Interactive Submission Button Elements */
    .stButton button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        border-radius: 10px;
        height: 45px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.2s ease;
    }
    
    .stButton button:hover {
        background-color: #155a8a;
        border-color: #155a8a;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Header Banner ----------
st.markdown("""
<div class="project-card">
    <h1>🏦 ATM Banking App</h1>
    <p>Securely Deposit or Withdraw funds from your bank account</p>
</div>
""", unsafe_allow_html=True)

# ---------- Real-time Balance Box ----------
st.markdown(
    f'<div class="balance-box">Current Balance: ₹ {st.session_state.balance:,.2f}</div>',
    unsafe_allow_html=True
)

# ---------- TWO COLUMN TRANSACTION WINDOW ----------
# Creates two horizontal layout column blocks inside your UI window
col1, col2 = st.columns(2)

with col1:
    choice = st.selectbox(
        "Select Transaction Type",
        ["Deposit", "Withdraw"]
    )

with col2:
    amount = st.number_input(
        "Enter Transaction Amount (₹)",
        min_value=0,
        step=100
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Interactive Action Processing ----------
if st.button("Submit Transaction"):
    try:
        if amount <= 0:
            raise Exception("Please enter a valid amount greater than zero.")

        # Process Deposit
        if choice == "Deposit":
            st.session_state.balance += amount
            st.markdown(
                '<p class="success-msg">Deposit Successful ✅</p>',
                unsafe_allow_html=True
            )

        # Process Withdrawal
        elif choice == "Withdraw":
            if amount > st.session_state.balance:
                raise Exception("Insufficient balance to complete withdrawal operation.")

            st.session_state.balance -= amount
            st.markdown(
                '<p class="success-msg">Withdrawal Successful ✅</p>',
                unsafe_allow_html=True
            )

        st.success(f"Updated Balance Ledger: ₹ {st.session_state.balance:,.2f}")
        st.rerun()  # Forces update to clean visual layout components immediately

    except Exception as e:
        st.markdown(
            f'<p class="error-msg">Transaction Failed ❌: {e}</p>',
            unsafe_allow_html=True
        )

# ---------- App Footer Notation Elements ----------
st.markdown("<br>", unsafe_allow_html=True)
finally_msg = "Thank you for choosing our banking platform ❤️ Visit Again!"
st.info(finally_msg)

st.markdown("---")
st.markdown("🚀 **Developed by Yanaguntikar**")
st.markdown("📧 Yanaguntikarm@gmail.com")