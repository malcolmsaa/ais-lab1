---

# Rapport (för inlämning)

```md
# Lab 1 – AI-based Security Monitoring

## 1. Introduction

The purpose of this lab was to design and implement a security monitoring system using Wazuh combined with AI-based anomaly detection.

The goal was to detect suspicious behavior, classify threats, and automate response actions.

---

## 2. Architecture

The system consists of five main components:

- Wazuh agent
- Wazuh manager
- AI anomaly detection module
- Alert manager
- Response playbook

### Data Flow

1. System logs are generated
2. Wazuh analyzes logs using rules
3. Alerts are exported as JSON
4. AI processes the alerts
5. Alerts are classified by severity
6. Automated responses are triggered

---

## 3. Implementation

### 3.1 Wazuh Rules

Custom rules were created to detect:

- Suspicious SSH logins
- Successful logins from unusual sources
- AI-detected anomalies

Severity levels were assigned based on risk.

---

### 3.2 AI Detection

A Python-based anomaly detector was implemented.

It processes alert data and flags abnormal patterns based on:

- Frequency
- Behavior deviation
- Severity indicators

---

### 3.3 Alert Management

The alert manager assigns severity:

- Low
- Medium
- High
- Critical

This enables prioritization of threats.

---

### 3.4 Response Playbook

Automated actions were defined:

- Critical → Block IP + isolate host
- High → Block IP
- Medium → Monitor
- Low → Ignore

---

### 3.5 Automation

Scripts were created:

- `run_pipeline.sh` → runs full pipeline
- `test_attacks.sh` → simulates attacks
- `export_alerts.sh` → handles alert data

---

## 4. Results

The system successfully:

- Detected simulated attacks
- Classified threats correctly
- Triggered appropriate responses

The pipeline worked end-to-end without manual intervention.

---

## 5. Challenges

- Git conflicts during setup
- Handling file structure issues
- Ensuring correct JSON formatting

These were resolved through debugging and restructuring.

---

## 6. Conclusion

The lab demonstrates how AI can enhance traditional security monitoring.

Combining Wazuh with AI improves:

- Detection accuracy
- Response speed
- Automation capability

---

## 7. Future Improvements

- Train ML model on real datasets
- Add dashboard visualization
- Integrate with SIEM systems
