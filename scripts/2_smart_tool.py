import time, json, random
import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="SmartTool_Drill")
client.connect("127.0.0.1", 1883)

while True:
    thrust = random.uniform(200, 500)
    if random.random() < 0.30:
        torque, status = thrust * 0.10, "FAIL"
    else:
        torque, status = (thrust * 0.45) + random.uniform(-2, 2), "PASS"
        
    payload = {"Thrust": thrust, "Torque": torque, "Status": status}
    client.publish("aerospace/assembly/telemetry", json.dumps(payload))
    time.sleep(1)
