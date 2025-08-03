# In-memory database for call interactions and applications
CUSTOMER_DB = {"calls": {}, "next_id": 1}

# Simulated loan products
OVERDRAFT_INFO = {
    "name": "Flexi Overdraft Facility",
    "monthly_interest": 1.25,
    "tenure_years": 8,
    "multiplier_range": (10, 22),  # times of salary
    "description": "Overdraft line with no EMI, only interest on used amount. Valid for 8 years."
}

# --- Functions for the financial agent ---

def open_call(customer_name):
    """Start a new call and log the customer."""
    call_id = CUSTOMER_DB["next_id"]
    CUSTOMER_DB["next_id"] += 1

    CUSTOMER_DB["calls"][call_id] = {
        "name": customer_name,
        "info": {},
        "status": "initiated"
    }
    return {"call_id": call_id, "message": f"Call started with {customer_name}."}


def collect_customer_info(call_id, info):
    """Collect basic employment and financial info."""
    call = CUSTOMER_DB["calls"].get(call_id)
    if not call:
        return {"error": "Call ID not found."}

    call["info"].update(info)
    call["status"] = "info_collected"
    return {"call_id": call_id, "message": "Customer info updated.", "info": call["info"]}


def check_eligibility(call_id):
    """Simulate an eligibility check."""
    call = CUSTOMER_DB["calls"].get(call_id)
    if not call or "info" not in call:
        return {"error": "Incomplete call or info."}

    salary = call["info"].get("net_salary", 0)
    if salary < 15000:
        call["status"] = "not_eligible"
        return {"call_id": call_id, "eligible": False, "message": "Customer not eligible (salary too low)."}

    min_limit = salary * OVERDRAFT_INFO["multiplier_range"][0]
    max_limit = salary * OVERDRAFT_INFO["multiplier_range"][1]
    call["status"] = "eligible"
    return {
        "call_id": call_id,
        "eligible": True,
        "limit_range": [min_limit, max_limit],
        "interest_rate": OVERDRAFT_INFO["monthly_interest"],
        "message": f"Eligible for overdraft between ₹{min_limit:.0f} to ₹{max_limit:.0f}"
    }


def explain_benefits():
    """Provide benefits of the overdraft facility."""
    return {
        "name": OVERDRAFT_INFO["name"],
        "description": OVERDRAFT_INFO["description"],
        "interest": f"{OVERDRAFT_INFO['monthly_interest']}% per month",
        "validity": f"{OVERDRAFT_INFO['tenure_years']} years",
        "example": "If ₹1,00,000 is used for 30 days, interest charged is ₹1,250"
    }


def close_call(call_id, outcome):
    """Finalize the call interaction."""
    call = CUSTOMER_DB["calls"].get(call_id)
    if not call:
        return {"error": "Call ID not found."}

    call["status"] = "closed"
    call["outcome"] = outcome
    return {"call_id": call_id, "message": f"Call closed with outcome: {outcome}"}


# Function mapping dictionary
FUNCTION_MAP = {
    'open_call': open_call,
    'collect_customer_info': collect_customer_info,
    'check_eligibility': check_eligibility,
    'explain_benefits': explain_benefits,
    'close_call': close_call
}
