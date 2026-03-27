import streamlit as st
from bank import (
    create_account,
    deposit_money,
    withdraw_money,
    get_details,
    update_details,
    delete_account,
)

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Haider's Bank",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="expanded"          
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

/* ── Base ── */
html, body, [class*="css"] { font-family: 'Syne', sans-serif; }
.stApp { background: #f0f4ff; color: #1a1a2e; }

/* ── Hide Streamlit chrome, keep sidebar toggle ── */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: visible !important; }
[data-testid="stHeader"] { background: transparent !important; box-shadow: none !important; }

/* ── Hero ── */
.hero { text-align:center; padding:2.5rem 1rem 1.5rem; border-bottom:2px solid #c7d2fe; margin-bottom:2rem; }
.hero h1 { font-family:'Syne',sans-serif; font-weight:800; font-size:3rem; letter-spacing:-2px;
           background:linear-gradient(135deg,#4f46e5,#7c3aed);
           -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin:0; }
.hero p  { color:#6366f1; font-family:'Space Mono',monospace; font-size:0.75rem;
           letter-spacing:3px; text-transform:uppercase; margin-top:0.4rem; }

/* ── Cards ── */
.card { background:#ffffff; border:1px solid #c7d2fe; border-radius:16px;
        padding:1.8rem; margin-bottom:1.2rem; box-shadow:0 2px 12px rgba(99,102,241,0.08); }
.card-title { font-size:0.7rem; letter-spacing:3px; text-transform:uppercase;
              color:#4f46e5; font-family:'Space Mono',monospace; margin-bottom:0.5rem; }
.card-value { font-size:2.2rem; font-weight:800; color:#1e1b4b; font-family:'Syne',sans-serif; }
.card-sub   { font-size:0.8rem; color:#818cf8; font-family:'Space Mono',monospace; margin-top:0.3rem; }

/* ── Info rows ── */
.info-row   { display:flex; justify-content:space-between; padding:0.7rem 0;
              border-bottom:1px solid #e0e7ff; font-size:0.9rem; }
.info-label { color:#6366f1; font-family:'Space Mono',monospace; font-size:0.75rem; font-weight:600; }
.info-value { color:#1e1b4b; font-weight:700; }

/* ── Account badge ── */
.acc-badge { display:inline-block; background:#eef2ff; border:1.5px solid #a5b4fc;
             border-radius:8px; padding:0.3rem 0.8rem; font-family:'Space Mono',monospace;
             font-size:1rem; color:#4f46e5; letter-spacing:2px; }

/* ── Buttons ── */
.stButton > button { background:linear-gradient(135deg,#4f46e5 0%,#7c3aed 100%) !important;
                     color:#ffffff !important; font-family:'Syne',sans-serif; font-weight:700;
                     font-size:0.95rem; letter-spacing:1px; border:none !important;
                     border-radius:10px; width:100%; padding:0.6rem; }
.stButton > button:hover { opacity: 0.9; }

/* ── Text & Number inputs ── */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background:#ffffff !important; border:1.5px solid #a5b4fc !important;
    border-radius:8px !important; color:#1e1b4b !important;
    font-family:'Space Mono',monospace !important; font-size:0.95rem !important; }
.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color:#4f46e5 !important; box-shadow:0 0 0 3px rgba(99,102,241,0.15) !important; }

/* ── All labels (form fields, checkboxes, radio) ── */
label, .stTextInput label, .stNumberInput label,
.stCheckbox label, .stRadio label,
[data-testid="stForm"] label,
[data-baseweb="form-control-label"] {
    color:#1e1b4b !important; font-weight:600 !important; font-size:0.95rem !important; }

/* ── Sidebar (Enhanced) ── */
[data-testid="stSidebar"] { background:#ffffff !important; border-right:2px solid #c7d2fe !important; }
[data-testid="stSidebar"] * { color:#1e1b4b !important; }
[data-testid="stSidebar"] h3 { color:#4f46e5 !important; font-weight:800 !important; }
[data-testid="stSidebar"] hr { border-color:#c7d2fe !important; }

/* Sidebar radio menu – improved visibility */
[data-testid="stSidebar"] .stRadio label {
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    color: #1e1b4b !important;
    padding: 0.5rem 0.75rem !important;
    border-radius: 10px !important;
    transition: background 0.2s ease;
    display: flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    font-family: 'Syne', 'Segoe UI Emoji', 'Apple Color Emoji', sans-serif !important;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: #eef2ff !important;
}

[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p {
    margin: 0 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
}

/* ── HIDE SIDEBAR COLLAPSE BUTTON (FIXED SIDEBAR) ── */
[data-testid="stSidebarCollapseButton"] {
    display: none !important;
}

/* ── Page headings ── */
h1, h2, h3 { color:#1e1b4b !important; }

/* ── Markdown text ── */
p, li, span { color:#1e1b4b; }
</style>
""", unsafe_allow_html=True)

# ─── Hero ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero"><h1>Haider Bank</h1><p>Modern Banking · Secure · Simple</p></div>', unsafe_allow_html=True)

# ─── Sidebar ───────────────────────────────────────────────────────────────────
MENU_OPTIONS = [
    "🆕 Create Account",
    "💰 Deposit Money",
    "💸 Withdraw Money",
    "📋 Account Details",
    "✏️ Update Details",
    "🗑️ Delete Account",
]

with st.sidebar:
    st.markdown("### 🏦 Navigation")
    st.markdown("---")
    menu = st.radio("", MENU_OPTIONS, label_visibility="collapsed")

# ══════════════════════════════════════════════════════════════════════════════
# 1. CREATE ACCOUNT
# ══════════════════════════════════════════════════════════════════════════════
if menu == "🆕 Create Account":
    st.markdown("## Create Account")
    st.markdown("---")
    with st.form("create_form"):
        name  = st.text_input("Full Name")
        age   = st.number_input("Age", min_value=1, max_value=120, step=1, value=18)
        email = st.text_input("Email Address")
        pin   = st.text_input("4-Digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Open Account")

    if submitted:
        if not all([name.strip(), email.strip(), pin.strip()]):
            st.error("Please fill in all fields.")
        else:
            success, message, info = create_account(name, age, email, pin)
            if not success:
                st.error(f"❌ {message}")
            else:
                st.success(f"✅ {message}")
                st.markdown(
                    f'<div class="card">'
                    f'<div class="card-title">Your Account Number</div>'
                    f'<div class="acc-badge">{info["accountNo"]}</div>'
                    f'<div class="card-sub">Save this — you\'ll need it to log in.</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )
                col1, col2 = st.columns(2)
                col1.metric("Name", info["name"])
                col2.metric("Balance", "PKR 0")

# ══════════════════════════════════════════════════════════════════════════════
# 2. DEPOSIT
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "💰 Deposit Money":
    st.markdown("## Deposit Money")
    st.markdown("---")
    with st.form("deposit_form"):
        accnum = st.text_input("Account Number")
        pin    = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount (PKR)", min_value=1, max_value=10000, step=100, value=1000)
        submitted = st.form_submit_button("Deposit")

    if submitted:
        success, message, balance = deposit_money(accnum, pin, amount)
        if not success:
            st.error(f"❌ {message}")
        else:
            st.success(f"✅ {message}")
            st.markdown(
                f'<div class="card">'
                f'<div class="card-title">Updated Balance</div>'
                f'<div class="card-value">PKR {balance:,}</div>'
                f'<div class="card-sub">Account: {accnum}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

# ══════════════════════════════════════════════════════════════════════════════
# 3. WITHDRAW
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "💸 Withdraw Money":
    st.markdown("## Withdraw Money")
    st.markdown("---")
    with st.form("withdraw_form"):
        accnum = st.text_input("Account Number")
        pin    = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount (PKR)", min_value=1, step=100, value=500)
        submitted = st.form_submit_button("Withdraw")

    if submitted:
        success, message, balance = withdraw_money(accnum, pin, amount)
        if not success:
            st.error(f"❌ {message}")
        else:
            st.success(f"✅ {message}")
            st.markdown(
                f'<div class="card">'
                f'<div class="card-title">Remaining Balance</div>'
                f'<div class="card-value">PKR {balance:,}</div>'
                f'<div class="card-sub">Account: {accnum}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

# ══════════════════════════════════════════════════════════════════════════════
# 4. DETAILS
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "📋 Account Details":
    st.markdown("## Account Details")
    st.markdown("---")
    with st.form("details_form"):
        accnum = st.text_input("Account Number")
        pin    = st.text_input("PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("View Details")

    if submitted:
        success, message, user = get_details(accnum, pin)
        if not success:
            st.error(f"❌ {message}")
        else:
            st.markdown(
                f'<div class="card">'
                f'<div class="card-title">Account Balance</div>'
                f'<div class="card-value">PKR {user["balance"]:,}</div>'
                f'</div>'
                f'<div class="card">'
                f'<div class="info-row"><span class="info-label">Name</span><span class="info-value">{user["name"]}</span></div>'
                f'<div class="info-row"><span class="info-label">Age</span><span class="info-value">{user["age"]}</span></div>'
                f'<div class="info-row"><span class="info-label">Email</span><span class="info-value">{user["email"]}</span></div>'
                f'<div class="info-row"><span class="info-label">Account No</span><span class="info-value"><span class="acc-badge">{user["accountNo"]}</span></span></div>'
                f'</div>',
                unsafe_allow_html=True
            )

# ══════════════════════════════════════════════════════════════════════════════
# 5. UPDATE DETAILS
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "✏️ Update Details":
    st.markdown("## Update Details")
    st.markdown("---")

    with st.form("update_auth_form"):
        accnum = st.text_input("Account Number")
        pin    = st.text_input("Current PIN", type="password", max_chars=4)
        auth   = st.form_submit_button("Authenticate")

    if auth:
        success, message, user = get_details(accnum, pin)
        if not success:
            st.error(f"❌ {message}")
        else:
            st.session_state["update_accnum"] = accnum
            st.session_state["update_pin"]    = pin

    if "update_accnum" in st.session_state:
        st.info(f"Authenticated: **{st.session_state['update_accnum']}**")
        with st.form("update_form"):
            new_name  = st.text_input("New Name  (leave blank to keep)")
            new_email = st.text_input("New Email (leave blank to keep)")
            new_pin   = st.text_input("New PIN   (leave blank to keep)", type="password", max_chars=4)
            save      = st.form_submit_button("Save Changes")

        if save:
            success, message = update_details(
                st.session_state["update_accnum"],
                st.session_state["update_pin"],
                new_name  or None,
                new_email or None,
                new_pin   or None,
            )
            if not success:
                st.error(f"❌ {message}")
            else:
                st.success(f"✅ {message}")
                del st.session_state["update_accnum"]
                del st.session_state["update_pin"]

# ══════════════════════════════════════════════════════════════════════════════
# 6. DELETE ACCOUNT
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🗑️ Delete Account":
    st.markdown("## Delete Account")
    st.markdown("---")
    st.warning("⚠️ This action is permanent and cannot be undone.")

    with st.form("delete_form"):
        accnum   = st.text_input("Account Number")
        pin      = st.text_input("PIN", type="password", max_chars=4)
        confirm  = st.checkbox("I understand this is permanent")
        submitted = st.form_submit_button("Delete Account")

    if submitted:
        if not confirm:
            st.error("Please tick the confirmation checkbox.")
        else:
            success, message = delete_account(accnum, pin)
            if not success:
                st.error(f"❌ {message}")
            else:
                st.success(f"✅ {message}")

# ─── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#818cf8;font-family:Space Mono,monospace;"
    "font-size:0.7rem;letter-spacing:2px;'>HaiderBank · SECURE BANKING SYSTEM</p>",
    unsafe_allow_html=True
)
