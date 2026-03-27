<div align="center">

# 🏦 Haider's Bank Management System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-F7DF1E?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

**A production-ready, modular bank management system built with Python & Streamlit**

[Features](#features) · [Getting Started](#getting-started) · [Architecture](#architecture) · [Contributing](#contributing)

</div>

---

## Overview

A complete bank management system with a polished dark-themed web interface built using Streamlit. All account data is persisted in a local JSON file. The project follows a clean separation of concerns — `bank.py` handles all business logic while `app.py` manages the UI.

---

## Features

| Feature | Description |
|---|---|
| 🆕 Create account | Age validation (18+), 4-digit PIN, unique account number |
| 💰 Deposit money | Up to PKR 10,000 per transaction with input validation |
| 💸 Withdraw money | Real-time balance check before processing |
| 📋 Account details | PIN-authenticated secure account view |
| ✏️ Update details | Update name, email and PIN independently |
| 🗑️ Delete account | Permanent deletion with confirmation checkbox |

---

## Project Structure

```
Bank-Management/
  ├── app.py          # Streamlit web UI
  ├── bank.py         # Core banking logic & data layer
  ├── main.py         # CLI / terminal version
  ├── data.json       # Auto-generated local database
  └── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/HaiderNeuralNet/Bank-Management-System.git
cd Bank-Management-System

# 2. Install dependencies
pip install streamlit

# 3. Launch the Streamlit app
streamlit run app.py
```

> The app opens automatically at `http://localhost:8501`

### Run the terminal version (optional)

```bash
python main.py
```

---

## Architecture

The project is split into two clear layers:

### `bank.py` — Logic layer
Pure Python functions with no UI dependency. Each function returns a `(success, message, data)` tuple.

```python
create_account(name, age, email, pin)   # → (bool, str, dict)
deposit_money(accnum, pin, amount)      # → (bool, str, int)
withdraw_money(accnum, pin, amount)     # → (bool, str, int)
get_details(accnum, pin)                # → (bool, str, dict)
update_details(accnum, pin, ...)        # → (bool, str)
delete_account(accnum, pin)             # → (bool, str)
```

### `app.py` — UI layer
Imports all functions from `bank.py` and renders them in a Streamlit interface with:
- Dark-themed sidebar navigation
- Masked PIN input fields
- Form validation and error handling
- Session state for multi-step authentication
- Styled balance cards and account badges

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Web UI | Streamlit |
| Data storage | JSON (local file) |
| File handling | pathlib |
| Account generation | random, string |

---

## Security Notes

- ✅ PIN masking on all input fields
- ✅ Two-step authentication for sensitive operations (update)
- ✅ Confirmation checkbox required before account deletion
- ⚠️ PINs are stored in plaintext — this project is for educational purposes

---

## Contributing

This is a personal learning project. Feel free to fork it and build on top of it.
If you find a bug, open an issue and I'll take a look!

---

<div align="center">
Made by <strong>Haider Ali Shah</strong> · <a href="https://github.com/HaiderNeuralNet">github.com/HaiderNeuralNet</a>
</div>
