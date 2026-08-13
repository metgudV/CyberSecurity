# CVSS v3.1 Scoring & Gap Analysis

## 1. Gap Analysis

### Current State
The native OPC UA smart tools stream unencrypted, unsigned JSON telemetry across the industrial network via a vulnerable MQTT broker. There is implicit trust of all data arriving at the Enterprise Manufacturing Execution System (MES).

### Proposed State
Target architecture introduces an edge gateway to append UUIDs and HMAC signatures, while routing traffic through a Live Defense Dashboard equipped with an Isolation Forest ML engine to catch advanced physics anomalies and replay attacks.

### Gap Table
| Area | Current State | Proposed Target State | Remediation |
| :--- | :--- | :--- | :--- |
| **Integrity** | Plaintext JSON MQTT | HMAC-SHA256 Signatures | Implement edge payload signing |
| **Replay Protection** | None | UUID nonces & state tracking | Add Layer 1 Replay Detector |
| **Insider Threat** | Implicit trust of signed data | Physics correlation validation | Deploy Isolation Forest ML model |

---

## 2. CVSS Scoring for Top Two Vulnerabilities

| Vulnerability | Vector | Base Score | Severity | Explanation |
| :--- | :--- | :--- | :--- | :--- |
| **1. MQTT Topic Spoofing (Unauthenticated Injection)** | `AV:A/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H` | **9.3** | **Critical** | Adjacent network access, no privileges required. Attacker injects forged data, causing high integrity impact (falsified QA logs) and high availability impact (crashing the MES parser). Scope is changed from the broker to the MES database. |
| **2. Replay Attack on Structural QA Logs** | `AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N` | **6.5** | **Medium** | Adjacent network access. Attacker replays a previously recorded, valid "PASS" payload to cover up a current tool failure. High integrity impact due to fraudulent safety records, but no availability impact. |

---

## 3. CVSS Metric Tables (Vulnerability 1: MQTT Topic Spoofing)

### CVSS Base Metric Table
| Metric | Abbreviation | Student Selection | Explanation |
| :--- | :--- | :--- | :--- |
| **Attack Vector** | AV | A (Adjacent) | Attacker must be on the FAL factory floor local network (VLAN) to sniff and inject MQTT traffic. |
| **Attack Complexity** | AC | L (Low) | Unencrypted MQTT requires standard, easily available scripting tools (like Python `paho-mqtt`). |
| **Privileges Required** | PR | N (None) | The local broker does not require username/password authentication. |
| **User Interaction** | UI | N (None) | The attack is completely automated against the M2M (Machine-to-Machine) pipeline. |
| **Scope** | S | C (Changed) | The vulnerable component is the MQTT broker, but the impact breaches the Enterprise MES database (a separate system). |
| **Confidentiality** | C | N (None) | Telemetry interception does not expose sensitive PII or corporate secrets, just mechanical physics. |
| **Integrity** | I | H (High) | Falsifying structural QA passes entirely compromises the integrity of the aircraft manufacturing record. |
| **Availability** | A | H (High) | Flooding the broker or poisoning the MES halts the automated assembly line, causing total loss of availability. |

### Temporal Metric Table
| Metric | Abbreviation | Student Selection | Explanation |
| :--- | :--- | :--- | :--- |
| **Exploit Code Maturity** | E | F (Functional) | No advanced weaponized exploit is required. Standard, widely available Python libraries are fully functional to execute this attack. |
| **Remediation Level** | RL | W (Workaround) | While the ultimate official fix is firmware-level HMAC signing, the immediate remediation available is a workaround: deploying the ML Isolation Forest model and strict VLAN segmentation. |
| **Report Confidence** | RC | C (Confirmed) | The vulnerability is fully confirmed and verified, as demonstrated by the successful spoofing attack in our simulated FAL factory environment. |

### Environmental Metric Table (Business Context)
| Metric | Abbreviation | Student Selection | Explanation |
| :--- | :--- | :--- | :--- |
| **Confidentiality Requirement** | CR | L (Low) | Raw thrust numbers are not highly classified intellectual property. |
| **Integrity Requirement** | IR | H (High) | EASA/FAA compliance strictly mandates 100% accuracy in aircraft structural joint QA logs. |
| **Availability Requirement** | AR | H (High) | Factory downtime costs the enterprise millions of dollars per hour; high availability is critical. |

---

## 4. Leadership Interpretation
Without cryptographic enforcement, our factory network currently operates on implicit trust, meaning any compromised laptop on the FAL can authorize defective aircraft parts. By implementing edge signing and Machine Learning validation, we mathematically guarantee QA data integrity and protect the enterprise from catastrophic safety failures, EASA non-compliance, and devastating reputational damage.
