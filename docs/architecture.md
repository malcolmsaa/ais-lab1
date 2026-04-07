# Arkitektur

## Komponenter

- Wazuh agent samlar loggar
- Wazuh manager analyserar regler
- AI-modul analyserar anomalier
- Alert manager klassificerar hot
- Response playbook hanterar åtgärder

## Flöde

1. Loggar genereras
2. Wazuh skapar alerts
3. Alerts exporteras till JSON
4. AI analyserar data
5. Alerts klassificeras
6. Åtgärder triggas
