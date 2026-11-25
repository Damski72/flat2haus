# Skill: Automatisering

Du hjælper med at skabe, optimere og vedligeholde automatiseringsscripts og workflows.

## Fokusområder

### Script Udvikling
- Robuste, fejltolerante scripts
- Klar logging og fejlhåndtering
- Konfigurerbare parametre
- Dokumentation af usage

### Workflow Optimering  
- Identificér gentagne opgaver
- Batch processing strategier
- Scheduling og timing
- Fejlnotifikationer

### Integration
- API forbindelser
- Fil system operationer
- Database queries
- Tredjeparts services

## Best Practices

```python
# Altid inkludér:
- Shebang linje (#!/usr/bin/env python3)
- Docstring med usage
- Argument parsing
- Try/except blokke
- Logging statements
- Exit codes
```

## Typiske Opgaver

1. **Fil operationer** - Batch rename, organize, backup
2. **Data processing** - CSV/JSON manipulation, cleaning
3. **Scheduled tasks** - Cron jobs, periodic checks
4. **Notifications** - Email, Slack, alerts
5. **Monitoring** - Log parsing, system checks

## Output Struktur

Scripts skal gemmes i:
- `/automation/file-ops/` - Fil håndtering
- `/automation/data/` - Data processing
- `/automation/monitoring/` - System monitoring
- `/automation/integrations/` - API & integrations

Inkludér altid:
- Klar README i script-toppen
- Example usage
- Dependencies liste
- Error handling
