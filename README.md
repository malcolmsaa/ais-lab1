# Lab 1 – Centraliserad säkerhetsövervakning med Wazuh

## Introduction
I detta projekt har jag byggt en centraliserad säkerhetslösning med Wazuh.  
Målet var att samla loggar, upptäcka hot och automatisera respons.

Systemet består av:
- Wazuh manager (Docker)
- Wazuh agent
- Egna regler
- AI-baserad anomalidetektion

---

## Architecture
Arkitekturen bygger på en klassisk SIEM-modell:

1. Agent samlar loggar från systemet  
2. Skickar data till Wazuh manager  
3. Manager analyserar data mot regler  
4. Alerts skapas i dashboarden  
5. AI analyserar vidare för avvikelser  

Se `docs/architecture.md` för mer detaljer.

---

## Detection Rules
Jag implementerade egna regler i:

`configs/local_rules.xml`

Exempel:
- Filändringar (FIM)
- Misstänkta kommandon
- Attack-simuleringar (test_attacks.sh)

Dessa regler triggar alerts direkt när ett mönster matchar.

---

## AI Detection
Jag skapade ett Python-script för anomalidetektion:

`ai-detection/anomaly_detector.py`

Funktion:
- Läser alerts från Wazuh
- Identifierar avvikande beteende
- Sparar resultat i:
  - `anomaly_results.csv`
  - `anomaly_report.txt`

Jag jämförde även:
- Regelbaserad detektion
- AI-baserad detektion

Resultat finns i:
`detection_comparison.json`

---

## Automated Response
Jag implementerade automatiserad respons:

`ai-detection/response_playbook.py`

Exempel:
- Logga incidenter
- Flagga misstänkta händelser
- Simulera åtgärder

Detta visar hur man kan bygga ett enklare SOAR-flöde.

---

## Scripts
Jag använde scripts för test och automation:

- `run_pipeline.sh` – kör hela flödet  
- `test_attacks.sh` – triggar attacker  
- `export_alerts.sh` – exporterar data  

---

## Results
Jag testade systemet genom att trigga attacker och mäta responstid.

Responstid:
Tid från attack → alert i Wazuh

Exempel:
- Filändring → alert på några sekunder
- Regelbaserad detektion → snabb och stabil
- AI-detektion → varierande men fångar mönster

Resultat finns i:
- `evidence/`
- `screenshots/`

---

## Screenshots
Projektet innehåller bevis på fungerande system:

- Dashboard (Wazuh UI)
- Alerts
- Regler som triggas
- Terminal output

Se mappen:
`screenshots/`

---

## Problems and Solutions
Jag stötte på flera problem:

Problem:
- Agent visades inte i dashboard
- “Never connected”
- Docker-konflikter
- Version mismatch

Lösning:
- Rensade hela Docker-miljön
- Installerade om Wazuh
- Säkerställde samma version på alla delar
- Konfigurerade rätt IP-adress
- Startade om alla tjänster

Efter detta fungerade systemet stabilt.

---

## Reflection
I början var det svårt att förstå:

- Vad SIEM innebär
- Hur Wazuh är uppbyggt
- Hur alla komponenter hänger ihop

Jag löste det genom att:
- Läsa dokumentation
- Testa steg för steg
- Felsöka praktiskt

Jag lärde mig:
- Hur logghantering fungerar
- Hur man bygger en SIEM-lösning
- Skillnaden mellan regler och AI-detektion
- Hur man felsöker Docker och nätverk

---

## Repository Structure
```text
ais-lab1/
├── configs/
├── ai-detection/
├── scripts/
├── docs/
├── evidence/
├── screenshots/
└── README.md
