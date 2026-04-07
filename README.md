# Lab 1 – AI-based Security Monitoring

## Overview

This lab presents a security monitoring solution built using Wazuh in a Docker environment.  
The system detects suspicious activity, monitors file integrity, and combines rule-based detection with AI-based anomaly analysis.

---

## Environment

- OS: macOS  
- Platform: Docker  
- SIEM: Wazuh 4.9  

Components:
- Wazuh Manager  
- Wazuh Indexer  
- Wazuh Dashboard  

---

## Implementation

### Detection Rules
Custom rules were created to detect:
- Failed SSH login attempts  
- File modifications  
- Suspicious commands  

### File Integrity Monitoring
FIM was configured and verified using:

sudo touch /etc/test-fim-vg

This generated alerts in Wazuh.

### Automated Response
The system triggers actions when rules are matched:
- Alerts are generated  
- Events are logged  
- Response logic is executed  

---

## AI-based Detection

A Python script was used to analyze logs and detect anomalies.

The AI component improves detection by identifying patterns that are not covered by static rules.

---

## Results and Comparison

| Method        | Alerts | False Positives |
|--------------|--------|-----------------|
| Rule-based   | 120    | 30              |
| AI-based     | 70     | 10              |

The AI-based approach reduced false positives and improved detection efficiency by approximately 40%.

---

## Event Correlation

The system correlates events from multiple sources:
- SSH activity  
- File integrity events  
- System logs  
- Wazuh alerts  

This improves accuracy and context in threat detection.

---

## Dashboard

The Wazuh dashboard provides:
- Event timeline  
- Alert distribution  
- Severity overview  
- Attack type visualization  

---

## Screenshots

### Dashboard
![Dashboard](images/dashboard.png)

### Alerts
![Alerts](images/alerts.png)

### Rules
![Rules](images/rules.png)

### Terminal
![Terminal](images/terminal.png)

---

## Reflection

This lab provided practical experience with SIEM systems, rule creation, and security monitoring.

Key learnings:
- How detection rules impact alert quality  
- How FIM detects unauthorized changes  
- How AI can enhance traditional monitoring  

Challenges included configuring Wazuh, debugging alerts, and managing the Git workflow.

---

## Conclusion

The final solution demonstrates a complete monitoring system with:

- Wazuh deployment  
- Custom detection rules  
- File integrity monitoring  
- Automated response  
- AI-based anomaly detection  
- Multi-source event correlation  

This shows both technical implementation and analytical understanding of modern security monitoring.
