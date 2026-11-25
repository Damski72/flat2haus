# Quick Start Guide

Velkommen til dit optimerede workspace! Her er hvordan du kommer hurtigt i gang.

## 🚀 Første Skridt

### 1. Forstå Strukturen
```
/Users/larsdam/repos/
├── skills/          → AI agent skills (brug disse!)
├── projects/        → Dine projekter
├── automation/      → Scripts & workflows
├── templates/       → Project templates
└── docs/            → Din dokumentation
```

### 2. Brug Skills
Skills optimerer din interaktion med GitHub Copilot:

**Eksempel:**
```
@workspace Brug /skills/automation.md - 
lav et script der organiserer downloads mappen
```

### 3. Start et Projekt
```bash
# Fra templates (når du har tilføjet dem)
cp -r templates/python-cli projects/mit-nye-projekt
cd projects/mit-nye-projekt

# Eller start fra bunden
cd projects
mkdir mit-projekt && cd mit-projekt
```

## 💡 Daglig Brug

### Arbejd på Eksisterende Projekt
```
@workspace Åbn [projektnavn] og hjælp med at...
```

### Opret Automatisering
```
@workspace Brug /skills/automation.md
Lav et script til at [opgave]
```

### Debug Issues
```
@workspace Brug /skills/debugging.md
Fejl i [fil]: [fejlbeskrivelse]
```

### Lav Dokumentation
```
@workspace Brug /skills/documentation.md
Lav README for [projekt]
```

## 🎯 Best Practices

### Do ✅
- Reference skills når relevant
- Vær specifik i dine requests
- Lad agenten implementere direkte
- Gem gentagne workflows i automation/
- Opdater skills med dine præferencer

### Don't ❌
- Gentag kontekst agenten allerede ved
- Bed om forklaringer uden kode
- Ignorer skills systemet
- Glem at opdatere dokumentation

## 🔧 Tilpasning

### Opdater Dine Præferencer
Rediger skills filer for at inkludere:
- Dit foretrukne programmeringssprog
- Framework præferencer
- Kodestil guidelines
- Værktøjer du bruger

**Eksempel i /skills/code-development.md:**
```markdown
## Foretrukne Sprog & Frameworks
- **Python**: 3.11+, FastAPI for APIs, pytest for tests
- **JavaScript**: Node.js 20+, React for frontend
- **Style**: Type hints, Google docstrings, max 100 chars
```

### Tilføj Custom Skills
Opret nye skills for gentagne workflows:
```bash
# Eksempel: DevOps skill
/skills/devops.md
```

## 📚 Lær Mere

- [README.md](README.md) - Hovedoversigt
- [skills/README.md](skills/README.md) - Skills guide
- Individuelle skill filer - Detaljerede guidelines

## 🆘 Få Hjælp

```
@workspace Forklar hvordan jeg [opgave]
@workspace Hvilken skill skal jeg bruge til [opgave]?
@workspace Vis eksempel på [koncept]
```

## 🔄 Næste Skridt

1. **Tilpas skills** - Tilføj dine præferencer til skill filerne
2. **Opret templates** - Lav templates for projekter du ofte starter
3. **Første projekt** - Start et projekt for at teste strukturen
4. **Automatisér** - Identificér gentagne opgaver og automatisér dem

---

**Husk**: GitHub Copilot lærer fra dine conversations. Jo mere du bruger systemet,
jo bedre vil den forstå dine præferencer og arbejdsstil. Memory-systemet sikrer
at kontekst bevares på tværs af sessions!
