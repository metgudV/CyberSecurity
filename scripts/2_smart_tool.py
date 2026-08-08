import hmac, hashlib, uuid
SECRET_KEY = b"aerospace_secure_key_2026"

def generate_signature(thrust, torque, status, tx_id):
    data_string = f"{thrust}_{torque}_{status}_{tx_id}"
    return hmac.new(SECRET_KEY, data_string.encode(), hashlib.sha256).hexdigest()

# Inside while loop:
tx_id = str(uuid.uuid4())
signature = generate_signature(thrust, torque, status, tx_id)
payload = {
    "Transaction_ID": tx_id,
    "Thrust": thrust, 
    "Torque": torque, 
    "Status": status,
    "Signature": signature
}
