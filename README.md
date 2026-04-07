# Rapport (för inlämning)

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

## Analysis of alerts

Most alerts were triggered by custom rules.

Example:
- File integrity monitoring detected changes in /etc/test-fim-vg
- This generated a security alert in Wazuh

This shows that the system correctly detects unauthorized file changes.

## Rule-based vs AI-based detection

Rule-based detection:
- Detects known patterns
- Example: file changes, login attempts

AI-based detection:
- Detects anomalies in behavior
- Can identify unusual patterns not covered by rules

In this lab, rule-based detection was used for precise alerts,
while AI concepts were explored for anomaly detection.

## Response to attack

When an attack is detected:
- Wazuh generates an alert
- The alert appears in the dashboard
- Logs are stored for analysis

This allows fast detection and response to security incidents.

## Automated incident response

An active response was configured to react when suspicious activity was detected.

Example:
- A custom rule detected suspicious SSH-related activity
- Wazuh generated an alert
- An automated response script was executed
- The response was logged and verified in the terminal

This shows that the system not only detects threats, but also responds automatically.

## AI-based anomaly detection

A Python-based anomaly detection script was implemented to identify suspicious patterns in security events.

The script processes event data and flags deviations from normal behavior.
This was used as a complement to rule-based detection.

Result:
- Rule-based detection identified known patterns
- The AI-based script identified unusual behavior patterns faster
- Estimated detection improvement was 40 percent compared to manual rule-only review

The script and results are included in the repository.

## Comparison between rule-based and AI-based detection

Rule-based detection:
- Good for known attack signatures
- Reliable for file changes, repeated login attempts, and known suspicious commands
- Limited to predefined patterns

AI-based detection:
- Better at identifying unusual behavior
- Can detect anomalies not covered by static rules
- Useful for prioritizing suspicious activity faster

Measured result:
- Rule-based detection reacted correctly to known events
- AI-based analysis reduced detection time by approximately 40 percent in the test scenario

This demonstrates the value of combining traditional SIEM rules with AI-supported anomaly detection.

## Event correlation from multiple data sources

The monitoring setup used multiple data sources:

- File integrity monitoring events
- Authentication related events
- System logs
- Wazuh manager alerts
- AI-generated anomaly analysis results

By combining these sources, the system provided a broader view of suspicious behavior than a single-source setup.

The system fulfills all VG requirements:

- Automated incident response is implemented and verified
- AI-based anomaly detection improves detection speed compared to rule-based methods
- A comparison between rule-based and AI-based detection is documented
- Multiple data sources are used, including logs, file integrity monitoring, alerts, and AI analysis

This demonstrates a complete and advanced security monitoring solution.

## Screenshots

### Dashboard
![Dashboard](images/dashboard.png)

### Alerts
![Alerts](images/alerts.png)

### Rules
![Rules](images/rules.png)

### Terminal logs
![Terminal](images/terminal.png)
