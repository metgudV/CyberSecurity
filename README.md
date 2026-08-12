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
* **Confidentiality Statement:** This submission uses a realistic simulated enterprise architecture inspired by aerospace assembly telemetry. No proprietary or confidential organizational information is disclosed.

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

## Repository Structure

```text
aerospace-cybersecurity-assignment/
├── report/
│   ├── final-report.md       # Comprehensive security evaluation report
│   └── final-report.pdf      # Compiled PDF report for LMS submission
│
├── diagrams/
│   ├── c4-context.puml       # C4 Level 1 Context Diagram (PlantUML)
│   ├── c4-container.puml     # C4 Level 2 Container Diagram (PlantUML)
│   ├── c4-component.puml     # C4 Level 3 Component Diagram (PlantUML)
│   ├── attack-graph-1.puml   # MITRE-aligned Topic Spoofing Attack Graph
│   └── attack-graph-2.puml   # Defense-in-Depth Control Stack Diagram
└── scripts/
    ├── 1_generate_baseline.py    # Generates mechanical dataset & trains Isolation Forest ML model
    ├── 2_smart_tool.py           # Simulates OPC UA smart tool & HMAC-signed MQTT publisher
    ├── 3_attacker.py             # Threat emulation script (Tampering, Replays, Insider Spoofing)
    ├── 4_dashboard.py            # Streamlit Live Defense Console & multi-layer detection pipeline
    └── requirements.txt          # Python dependency specifications
