import streamlit as st
import pandas as pd
import paho.mqtt.client as mqtt
import json, pickle, time, random, hmac, hashlib

st.set_page_config(page_title="Advanced Defense Dashboard", layout="wide")
st.title("Aerospace Assembly: Defense-in-Depth Architecture")

SECRET_KEY = b"aerospace_secure_key_2026"

@st.cache_resource
def load_model():
    with open('isolation_forest.pkl', 'rb') as f:
        return pickle.load(f)
model = load_model()

@st.cache_resource
def get_state():
    return {
        "telemetry": [], 
        "seen_tx": set(),
        "stats": {"Total": 0, "Safe": 0, "Replay": 0, "Tamper": 0, "Insider": 0}
    }
state = get_state()

def verify_signature(payload):
    data_string = f"{payload['Thrust']}_{payload['Torque']}_{payload['Status']}_{payload['Transaction_ID']}"
    expected_sig = hmac.new(SECRET_KEY, data_string.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_sig, payload.get("Signature", ""))

@st.cache_resource
def start_mqtt_client():
    def on_message(client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            tx_id = payload.get("Transaction_ID")
            state["stats"]["Total"] += 1
            
            # Layer 1: Replay Detection
            if tx_id in state["seen_tx"]:
                payload["Security_Alert"] = "🚨 BLOCKED: Replay Attack"
                state["stats"]["Replay"] += 1
            else:
                state["seen_tx"].add(tx_id)
                
                # Layer 2: Cryptographic Signature Check
                if not verify_signature(payload):
                    payload["Security_Alert"] = "🚨 BLOCKED: Invalid Signature (Tampering)"
                    state["stats"]["Tamper"] += 1
                else:
                    # Layer 3: ML Anomaly Detection (Physics Check)
                    df_current = pd.DataFrame([payload])
                    prediction = model.predict(df_current[['Thrust', 'Torque']])[0]
                    
                    if prediction == -1 and payload.get("Status") == "PASS":
                        payload["Security_Alert"] = "⚠️ COMPROMISED: ML Anomaly (Insider)"
                        state["stats"]["Insider"] += 1
                    else:
                        payload["Security_Alert"] = "✅ SAFE"
                        state["stats"]["Safe"] += 1
                        
            # Format payload for display
            display_data = {
                "Tx_ID": tx_id[:8],
                "Thrust": round(payload["Thrust"], 2),
                "Torque": round(payload["Torque"], 2),
                "Status": payload["Status"],
                "Security_Alert": payload["Security_Alert"]
            }
            state["telemetry"].append(display_data)
        except Exception as e:
            pass

    client_id = f"SOC_Dashboard_{random.randint(1000, 9999)}"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id)
    client.on_message = on_message
    client.connect("127.0.0.1", 1883) 
    client.subscribe("aerospace/assembly/telemetry")
    client.loop_start()
    return client

client = start_mqtt_client()

# --- UI RENDERING ---
# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Logs Analyzed", state["stats"]["Total"])
col2.metric("Replay Attacks Blocked", state["stats"]["Replay"])
col3.metric("Tamper Attempts Blocked", state["stats"]["Tamper"])
col4.metric("Insider Threats Detected (ML)", state["stats"]["Insider"])

st.markdown("---")
placeholder = st.empty()

if len(state["telemetry"]) > 0:
    df = pd.DataFrame(state["telemetry"][-15:])
    
    def highlight_alerts(val):
        if 'Tampering' in val or 'Replay' in val:
            return 'background-color: #ff9900; color: black; font-weight: bold'
        elif 'Insider' in val:
            return 'background-color: #ff4b4b; color: white; font-weight: bold'
        elif 'SAFE' in val:
            return 'background-color: #00cc66; color: white'
        return ''
        
    placeholder.dataframe(df.style.map(highlight_alerts, subset=['Security_Alert']), use_container_width=True)
else:
    placeholder.info("⏳ Waiting for secure telemetry...")

time.sleep(1)
st.rerun()
