# Implementation Scripts: Airbus Telemetry Defense Pipeline

This folder contains the core Python implementation files for the Airbus A350 Final Assembly Line (FAL) Telemetry Defense Platform simulation. These scripts work together to simulate a live Industry 4.0 factory floor, execute MITRE-aligned cyberattacks, and defend against them using a Defense-in-Depth architecture (HMAC-SHA256, UUID Nonces, and ML).

## 📂 File Directory

*   **`1_generate_baseline.py`**
    *   **Role:** Data Science & ML Training.
    *   **Description:** Generates a synthetic dataset representing baseline mechanical physics (Thrust and Torque) for Airbus smart drills. It trains an Unsupervised Machine Learning model (Isolation Forest) and outputs `isolation_forest.pkl` for the dashboard to use.
*   **`2_smart_tool.py`**
    *   **Role:** Edge/IoT Simulator.
    *   **Description:** Simulates an Airbus smart drilling unit. It generates high-frequency telemetry, appends unique UUID v4 transaction nonces, signs the payload using an HMAC-SHA256 secret key, and publishes the data to the local MQTT broker.
*   **`3_attacker.py`**
    *   **Role:** Threat Emulator.
    *   **Description:** Simulates a compromised maintenance laptop on the factory VLAN. It actively monitors the MQTT network for failing tool logs and launches three distinct attacks:
        1.  **Tampering:** Modifies a 'FAIL' to a 'PASS' (caught by Crypto Layer).
        2.  **Replay:** Injects an old valid 'PASS' (caught by Replay Layer).
        3.  **Insider Threat:** Forges a valid signature for a spoofed payload using a stolen key (caught by ML Layer).
*   **`4_dashboard.py`**
    *   **Role:** SOC Monitoring & Alerting.
    *   **Description:** A Streamlit-based web application that acts as the Airbus Live Defense Dashboard. It subscribes to the MQTT broker and processes all incoming telemetry through a 3-layer security pipeline (Replay Check $\rightarrow$ Crypto Check $\rightarrow$ ML Anomaly Check) before rendering the results in a live UI grid.

---

## 🚀 How to Run the Simulation

To successfully run the simulated attack and defense pipeline, you must execute the processes in the following order using separate terminal windows:

1.  **Start the Local MQTT Broker:**
    ```bash
    amqtt
    ```
    *(Leave this running in Terminal 1).*

2.  **Generate the ML Model:**
    ```bash
    python 1_generate_baseline.py
    ```
    *(Run this once in Terminal 2. It will exit automatically).*

3.  **Launch the Defense Dashboard:**
    ```bash
    streamlit run 4_dashboard.py
    ```
    *(Leave this running in Terminal 2. Access via `http://localhost:8501`).*

4.  **Deploy the Attacker Script:**
    ```bash
    python 3_attacker.py
    ```
    *(Leave this running in Terminal 3).*

5.  **Start the Smart Tool Telemetry Stream:**
    ```bash
    python 2_smart_tool.py
    ```
    *(Leave this running in Terminal 4).*

Watch the Streamlit dashboard in your browser to see the attacks get intercepted and categorized in real-time!
