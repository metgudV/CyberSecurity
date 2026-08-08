import streamlit as st, pandas as pd, paho.mqtt.client as mqtt, json, pickle, time, random

st.title("Aerospace Assembly: ML Anomaly Detection")
model = pickle.load(open('isolation_forest.pkl', 'rb'))
telemetry_data = []

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    df_current = pd.DataFrame([payload])
    prediction = model.predict(df_current[['Thrust', 'Torque']])[0]
    
    if prediction == -1 and payload.get("Status") == "PASS":
        payload["Security_Alert"] = "COMPROMISED"
    else:
        payload["Security_Alert"] = "SAFE"
    telemetry_data.append(payload)
