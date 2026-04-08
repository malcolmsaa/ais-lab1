## Reflection

During this lab, I designed and implemented a security monitoring system using Wazuh together with an AI-based anomly detection script. The hole goal was to detect  suspicous activity, analyze alerts, and automate parts of the response process.

One of the main things I learned was how diffrent components in a SIEM system interact. In the beginning, I found it diffcult to fully understand what SIEM is, how Wazuh works, and what each component actually does. Terms like agents, managers, rules, and alerts were intially unclear, which made it harder to understand how the system should function as a whole.

By working pratically with the system and reviewing the course material, I gardually built a clearer understanding of how logs are collected,processed, and analyzed. This helped me understand hoe Wazuh detects threats and how different parts of the system are connected.

A major challenge during the lab was  troubleshooting errors in the environment. I encountered issues with Docker, agent communication, and permission errors such as the "admin is reserved" problem. At first, it was diffcult to understand the cause of these issues.

To solve this, I reviewed the provided course material and researched how Wazuh and Docker handle configurtion and authentication. By analyzing the problem step by step, I identified that inconsistent versions and incorrect setup caused the errors. I resolved this by cleaning the environment and reinstalling the system with consistent configutrions.

Another important insight was the difference between ruled-based and AI-based detection. Rule-based detection is effective for known patterns, while AI-based detection can identify anomalies that do not match predefined rules. This showed how combining both approaches improves detection capability.

Overall,this lab helped me develop practical skills in security monitoring, troubleshooting, and system configuration. I also imporved my ability to understand complex system by breaking them down into smaller parts ana analyzing how they interact.
