# Advanced Cyber Security Assignment

#Aerospace Assembly Telemetry: ML-Driven Anomaly Detection & Defense-in-Depth Platform

## Student Information
- Name: Vijayalaxmi Metgud 
- Student ID:2024ab12508
- Name: Pallotu Devisri 
- Student ID:2024ab12507
- Course: SS*ZG681 / SE*ZG681 Advanced Cyber Security
* **System Selected:** Aerospace Drilling & Fastening Telemetry Data Pipeline
* **System Type:** Industry 4.0 Simulated Architecture
  
## 🔒 Confidentiality Statement
This repository does not contain proprietary, sensitive, or confidential organizational information. All sensitive details have been anonymized, and the architecture represents a safe, academic simulation of an Industry 4.0 manufacturing environment.

---

## Executive Overview
Aircraft section assembly relies on automated precision tools (smart drilling and fastening units) that stream high-frequency telemetry—specifically Thrust and Torque curves—to a Manufacturing Execution System (MES) to verify structural integrity and record Quality Assurance (QA) passes. 

Telemetry traveling over local industrial networks over unencrypted MQTT topics is vulnerable to **MQTT Topic Spoofing** attacks. An adversary possessing local network access (e.g., via a compromised maintenance laptop) can intercept a failing job log and inject a fake "PASS" value into the stream, bypassing QA checks and severely threatening aircraft safety.

This project implements a multi-layered **Defense-in-Depth Architecture** that combines:
1. **Cryptographic Telemetry Signing (HMAC-SHA256):** Provides mathematical payload integrity and origin authenticity at the edge.
2. **Replay Attack Protection (UUID Nonces):** Rejects duplicate or stale telemetry injections.
3. **Unsupervised Machine Learning IDS (Isolation Forest):** Evaluates mathematical correlations between Thrust and Torque curves to catch insider threats or key compromises.
4. **Live Defense Dashboard (Streamlit):** Real-time Security Operations Center (SOC) console tracking live telemetry, flagging compromised data entries, and displaying active threat metrics.

---

## 📂 Repository Structure

```text
├── README.md                                # This detailed project overview
├── report/
│   ├── final-report.md                      # Markdown version of the engineering report
│   └── final-report.pdf                     # Final PDF submission
├── diagrams/
│   ├── c4-context.puml                      # C4 Level 1 System Context Diagram
│   ├── c4-container.puml                    # C4 Level 2 Container Diagram
│   ├── c4-component.puml                    # C4 Level 3 Component Diagram
│   ├── attack-graph-1.puml                  # MITRE-Aligned Threat 1 (Topic Spoofing)
│   └── attack-graph-2.puml                  # MITRE-Aligned Threat 2 (Insider Threat)
├── risk/
│   ├── cvss-table.md                        # CVSS v3.1 Scoring & Gap Analysis
│   └── risk-register.csv                    # Quantified Risk Register
├── scripts/
│   ├── check_structure.py                   # Automated repo structure validation
│   ├── grade_report.py                      # Automated grading keyword check
│   └── implementation/                      # Core Python Simulation Files
│       ├── 1_generate_baseline.py           # Trains the ML Isolation Forest
│       ├── 2_smart_tool.py                  # Simulates edge hardware & HMAC signing
│       ├── 3_attacker.py                    # Threat emulator (Spoofing/Replay)
│       └── 4_dashboard.py                   # Streamlit SOC Monitoring UI
├       └── requirements.txt                 # Python dependency specifications
└── presentation/
    └── viva-presentation-outline.md         # Slide outline for Viva assessment
```
🚀 How to Run the Simulation
If you wish to test the live Python implementation of the Defense-in-Depth pipeline, follow these steps using separate terminal windows:

1. Start the MQTT Broker (Terminal 1):
``` text
amqtt
```

2. Train the ML Model (Terminal 2):
``` text
cd scripts/implementation/
python 1_generate_baseline.py
```

3. Launch the SOC Dashboard (Terminal 2):
``` text
streamlit run 4_dashboard.py
```

4. Start the Attacker Script (Terminal 3):
``` text
python 3_attacker.py
```

5. Start the Smart Tool Telemetry (Terminal 4):
``` text
python 2_smart_tool.py
``` 
View the live UI at http://localhost:8501 to watch the attacks get blocked in real-time!
