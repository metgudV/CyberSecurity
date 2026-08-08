def verify_signature(payload):
    data_string = f"{payload['Thrust']}_{payload['Torque']}_{payload['Status']}_{payload['Transaction_ID']}"
    expected_sig = hmac.new(SECRET_KEY, data_string.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_sig, payload.get("Signature", ""))

# Added inside on_message for Layered Defense:
if tx_id in state["seen_tx"]:
    payload["Security_Alert"] = "🚨 BLOCKED: Replay Attack"
else:
    state["seen_tx"].add(tx_id)
    if not verify_signature(payload):
        payload["Security_Alert"] = "🚨 BLOCKED: Invalid Signature (Tampering)"
    else:
        # ML check happens here

# Added UI Metrics:
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Logs", state["stats"]["Total"])
col2.metric("Replay Blocked", state["stats"]["Replay"])
col3.metric("Tamper Blocked", state["stats"]["Tamper"])
col4.metric("Insider Detected", state["stats"]["Insider"])


