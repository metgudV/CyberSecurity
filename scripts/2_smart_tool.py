import time
import json
import random
import hmac
import hashlib
import uuid
import paho.mqtt.client as mqtt

MQTT_BROKER = "127.0.0.1"
MQTT_TOPIC = "aerospace/assembly/telemetry"
SECRET_KEY = b"aerospace_secure_key_2026" # The shared secret key

def generate_signature(thrust, torque, status, tx_id):
    # Combine data into a single string to sign
    data_string = f"{thrust}_{torque}_{status}_{tx_id}"
    return hmac.new(SECRET_KEY, data_string.encode(), hashlib.sha256).hexdigest()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="SmartTool_Drill")
client.connect(MQTT_BROKER, 1883)

print("Simulating Secure OPC UA telemetry...")
while True:
    thrust = random.uniform(200, 500)
    
    if random.random() < 0.30:
        torque = thrust * 0.10
        status = "FAIL"
    else:
        torque = (thrust * 0.45) + random.uniform(-2, 2)
        status = "PASS"
        
    tx_id = str(uuid.uuid4()) # Unique ID to prevent replays
    signature = generate_signature(thrust, torque, status, tx_id)
    
    payload = {
        "Transaction_ID": tx_id,
        "Thrust": thrust, 
        "Torque": torque, 
        "Status": status,
        "Signature": signature
    }
    
    client.publish(MQTT_TOPIC, json.dumps(payload))
    print(f"Published: {payload['Transaction_ID'][:8]}... | {status}")
    time.sleep(1)
