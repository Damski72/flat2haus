# Sådan Opdaterer Du Systemet

Guide til at vedligeholde skills, memory og best practices over tid.

## 🎯 Hvad Skal Hvor?

### Skills (`/repos/skills/`)
**Brug til**: Arbejdsmetoder, best practices, generelle guidelines

**Eksempler på hvad der hører hjemme her:**
```markdown
## Best Practices
- Brug type hints i Python
- Skriv docstrings i Google format
- Tests skal være i separate test/ mappe
- Error handling med try/except
- Logging i stedet for print statements
```

**Opdater når:**
- ✅ Nye best practices dukker op i branchen
- ✅ Du lærer en bedre måde at gøre noget
- ✅ Nye værktøjer bliver standard
- ✅ Du vil standardisere en arbejdsmetode

### Memory (`/memories/lars-preferences.md`)
**Brug til**: Dine personlige præferencer og valg

**Eksempler på hvad der hører hjemme her:**
```markdown
## Foretrukne Værktøjer
- Python: 3.11+, FastAPI for APIs
- Testing: pytest with coverage
- Linting: ruff (ikke flake8)
- Formatting: black med 100 char limit

## Kodestil
- Max line length: 100
- Naming: snake_case for Python
- Always use type hints
```

**Opdater når:**
- ✅ Du skifter til nyt værktøj
- ✅ Din præference ændrer sig
- ✅ Du vil have agenten arbejder anderledes
- ✅ Nye personlige mønstre opstår

### Project Docs (`/projects/[projekt]/docs/`)
**Brug til**: Projekt-specifikke beslutninger

**Eksempler:**
```markdown
## Architectural Decisions
- Valgte PostgreSQL over MongoDB fordi...
- Bruger JWT for authentication
- API versioning med /v1/ prefix

## Learnings
- Performance issue med X løst ved Y
- Database migration strategy
```

## 🔄 Opdaterings Workflow

### 1. Når Du Lærer Noget Nyt

**Hvis det er generelt (best practice):**
```
@workspace Opdater /skills/[relevant].md med:
- Ny best practice om [emne]
- Tilføj sektion om [værktøj]
```

**Hvis det er personligt (din præference):**
```
@workspace Opdater /memories/lars-preferences.md:
Jeg foretrækker nu [værktøj] over [gammelt værktøj]
```

### 2. Regulær Gennemgang

**Månedligt eller kvartalsvist:**
```bash
# Gennemgå skills
ls -l skills/
# Læs igennem og opdater forældede info

# Check memory
cat /memories/lars-preferences.md
# Er det stadig accurate?
```

### 3. Før Stort Projekt

Start nyt projekt med opdaterede guidelines:
```
@workspace Gennemgå /skills/ og /memories/
Er der noget der skal opdateres før vi starter?
```

## 📝 Quick Commands

### Tilføj Præference
```
@workspace Husk at jeg foretrækker [X] til [Y]
```
→ Jeg opdaterer `/memories/lars-preferences.md`

### Opdater Best Practice
```
@workspace Opdater /skills/code-development.md
Tilføj best practice: [praksis]
```

### Tilføj Ny Skill
```
@workspace Lav ny skill: /skills/[navn].md
Fokus på [område]
```

## 🤖 Agenten Kan Selv

**Ja, jeg kan antage generelle best practices:**
- Industry standards (PEP 8, etc.)
- Sikkerhedsprincipper
- Performance best practices
- Clean code principles

**Men jeg ved ikke dine specifikke præferencer:**
- Hvilket framework du foretrækker
- Din kodestil (80 vs 100 vs 120 chars)
- Hvilke værktøjer du bruger
- Dine naming conventions

**Derfor**: 
- Generelt = jeg ved det (eller kan antage)
- Specifikt til dig = skal i memory
- Dit workflow = skal i skills

## 🎓 Nye Modeller & Teknologier

Når nye ting kommer:

### Nye AI Modeller
- Ingen action nødvendig
- Jeg opdateres automatisk med ny viden

### Nye Programmeringssprog/-frameworks
```
@workspace Opdater /skills/code-development.md
Tilføj sektion om [nyt framework]
```

### Nye Best Practices
```
@workspace Opdater relevante skills med ny praksis
```

### Nye Værktøjer Du Vil Bruge
```
@workspace Tilføj til /memories/lars-preferences.md
Jeg bruger nu [værktøj] til [formål]
```

## 💡 Pro Tips

### 1. Start Bredt, Specificer Gradvist
Start med generelle skills, tilføj specifikke præferencer over tid.

### 2. Dokumentér Hvorfor
```markdown
## Foretrukne Værktøjer
- ruff (ikke flake8) - hurtigere, moderne
- FastAPI (ikke Flask) - async support, type safety
```

### 3. Versioner Store Ændringer
Hvis du laver store ændringer, gem backup:
```bash
cp /memories/lars-preferences.md /memories/lars-preferences.backup.md
```

### 4. Hold Det Simpelt
- For mange skills = forvirrende
- For detaljeret memory = spild af tokens
- Balance mellem komplet og koncis

### 5. Test Efter Opdatering
```
@workspace Test at nye guidelines virker
Lav et quick eksempel på [opgave]
```

## 📊 Eksempel Opdatering

### Scenario: Du skifter fra Flask til FastAPI

**1. Opdater Memory (personlig præference):**
```markdown
# /memories/lars-preferences.md

## Foretrukne Frameworks
- **Web APIs**: FastAPI (skiftet fra Flask 2026-04)
  - Async support
  - Automatic API docs
  - Type safety
```

**2. Opdater Skills (arbejdsmetode):**
```markdown
# /skills/code-development.md

## FastAPI Best Practices
- Brug Pydantic models for validation
- Dependency injection for shared resources
- Background tasks for async operations
- APIRouter for code organization
```

**3. Opdater Template:**
Lav ny `/templates/fastapi-api/` template

**4. Test:**
```
@workspace Lav et quick FastAPI endpoint
med Pydantic validation
```

## 🚀 Du Er I Kontrol

**Systemet er dit værktøj:**
- Opdater når DU vil
- Tilføj hvad DU har brug for
- Fjern hvad der ikke virker

**Jeg tilpasser mig:**
- Lærer fra dine opdateringer
- Bruger seneste info
- Foreslår improvements

Men du bestemmer strukturen og indholdet!
