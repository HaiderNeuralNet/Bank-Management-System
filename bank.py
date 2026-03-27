
#-------------tailor it with the help of AI same Code

import json
import random
import string
import os
from pathlib import Path

# Use /tmp for Streamlit Cloud compatibility (writable on all platforms)
DATABASE = "/tmp/data.json"


def load_data():
    path = Path(DATABASE)
    if path.exists():
        try:
            with open(DATABASE, "r") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except Exception as err:
            print(f"Error loading data: {err}")
            return []
    return []


def save_data(data):
    try:
        with open(DATABASE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as err:
        print(f"Error saving data: {err}")


def generate_account_no():
    alpha  = random.choices(string.ascii_letters, k=3)
    num    = random.choices(string.digits, k=3)
    spchar = random.choices("!@#$%^&*", k=1)
    parts  = alpha + num + spchar
    random.shuffle(parts)
    return "".join(parts)


def find_user(data, accnum, pin):
    """Return user dict if found, else None."""
    try:
        matches = [u for u in data if u["accountNo"] == accnum and u["pin"] == int(pin)]
        return matches[0] if matches else None
    except (ValueError, KeyError):
        return None


def create_account(name, age, email, pin):
    """
    Create a new bank account.
    Returns (success: bool, message: str, account_info: dict or None)
    """
    data = load_data()

    if int(age) < 18:
        return False, "You must be at least 18 years old.", None

    if not str(pin).isdigit() or len(str(pin)) != 4:
        return False, "PIN must be exactly 4 digits.", None

    accno = generate_account_no()
    info = {
        "name": name,
        "age": int(age),
        "email": email,
        "pin": int(pin),
        "accountNo": accno,
        "balance": 0
    }
    data.append(info)
    save_data(data)
    return True, "Account created successfully.", info


def deposit_money(accnum, pin, amount):
    """
    Deposit amount into account.
    Returns (success: bool, message: str, updated_balance: int or None)
    """
    data = load_data()
    user = find_user(data, accnum, pin)

    if not user:
        return False, "Account not found or wrong PIN.", None

    try:
        amount = int(amount)
    except (ValueError, TypeError):
        return False, "Invalid amount entered.", None

    if amount <= 0:
        return False, "Amount must be greater than 0.", None

    if amount > 10000:
        return False, "Amount must be between PKR 1 and PKR 10,000.", None

    user["balance"] += amount
    save_data(data)
    return True, f"{amount} PKR deposited successfully.", user["balance"]


def withdraw_money(accnum, pin, amount):
    """
    Withdraw amount from account.
    Returns (success: bool, message: str, updated_balance: int or None)
    """
    data = load_data()
    user = find_user(data, accnum, pin)

    if not user:
        return False, "Account not found or wrong PIN.", None

    try:
        amount = int(amount)
    except (ValueError, TypeError):
        return False, "Invalid amount.", None

    if amount <= 0:
        return False, "Amount must be greater than zero.", None

    if user["balance"] < amount:
        return False, f"Insufficient balance. Current balance: PKR {user['balance']:,}", None

    user["balance"] -= amount
    save_data(data)
    return True, "Withdrawal successful.", user["balance"]


def get_details(accnum, pin):
    """
    Get account details.
    Returns (success: bool, message: str, user_info: dict or None)
    """
    data = load_data()
    user = find_user(data, accnum, pin)

    if not user:
        return False, "Account not found or wrong PIN.", None

    return True, "Account found.", dict(user)


def update_details(accnum, pin, new_name=None, new_email=None, new_pin=None):
    """
    Update account details.
    Returns (success: bool, message: str)
    """
    data = load_data()
    user = find_user(data, accnum, pin)

    if not user:
        return False, "Account not found or wrong PIN."

    if new_name:
        user["name"] = new_name
    if new_email:
        user["email"] = new_email
    if new_pin:
        if not str(new_pin).isdigit() or len(str(new_pin)) != 4:
            return False, "New PIN must be exactly 4 digits."
        user["pin"] = int(new_pin)

    save_data(data)
    return True, "Details updated successfully."


def delete_account(accnum, pin):
    """
    Delete an account.
    Returns (success: bool, message: str)
    """
    data = load_data()
    user = find_user(data, accnum, pin)

    if not user:
        return False, "Account not found or wrong PIN."

    data.remove(user)
    save_data(data)
    return True, "Account deleted successfully."