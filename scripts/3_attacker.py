import random, hmac, hashlib, uuid
STOLEN_KEY = b"aerospace_secure_key_2026"

# Inside on_message logic:
attack_type = random.choice(["TAMPER", "REPLAY", "INSIDER"])

if attack_type == "TAMPER": # Forges ID, invalid signature
    spoofed["Transaction_ID"] = str(uuid.uuid4())
elif attack_type == "REPLAY" and last_valid_pass: # Reuses old valid message
    client.publish(MQTT_TOPIC, json.dumps(last_valid_pass))
elif attack_type == "INSIDER": # Forges ID and Signature
    spoofed["Transaction_ID"] = str(uuid.uuid4())
    data_string = f"{spoofed['Thrust']}_{spoofed['Torque']}_{spoofed['Status']}_{spoofed['Transaction_ID']}"
    spoofed["Signature"] = hmac.new(STOLEN_KEY, data_string.encode(), hashlib.sha256).hexdigest()
