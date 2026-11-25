# Skills Guide

Dette er samlingen af AI agent skills til at optimere dit arbejde.

## 📚 Tilgængelige Skills

| Skill | Brug Til | Fil |
|-------|----------|-----|
| **Code Development** | Implementering, refactoring, code review | [code-development.md](code-development.md) |
| **Automation** | Scripts, workflows, batch processing | [automation.md](automation.md) |
| **Debugging** | Fejlfinding, problemløsning | [debugging.md](debugging.md) |
| **Documentation** | README, docs, comments | [documentation.md](documentation.md) |
| **Data Analysis** | Data processing, visualization, insights | [data-analysis.md](data-analysis.md) |
| **Project Planning** | Struktur, planlægning, organization | [project-planning.md](project-planning.md) |

## 🎯 Sådan Bruger Du Skills

### Metode 1: Direct Reference
```
@workspace Brug /skills/automation.md - lav et script til at...
```

### Metode 2: Implicit Context
GitHub Copilot lærer automatisk fra workspace-strukturen.
Skills er designet til at blive indlæst som kontekst.

### Metode 3: Combine Skills
```
@workspace Brug /skills/code-development.md og /skills/debugging.md
til at finde og rette...
```

## 💡 Best Practices

1. **Vælg rigtig skill** - Hver skill er optimeret til specifik opgave type
2. **Kombiner ved behov** - Nogle opgaver kræver flere skills
3. **Tilpas skills** - Rediger skills til dine præferencer
4. **Tilføj nye skills** - Lav custom skills for gentagne workflows

## 🔧 Tilpasning

Hver skill kan tilpasses:

```markdown
## Foretrukne Værktøjer
- Python: 3.11+
- Frameworks: FastAPI, Flask
- Testing: pytest
- Linting: ruff

## Kodestil
- Type hints altid
- Docstrings i Google format
- Max line length: 100
```

Tilføj disse sektioner til dine skills så agenten lærer dine præferencer!

## 📈 Token Optimering

Skills er designet til at:
- ✅ Give præcis kontekst hurtigt
- ✅ Reducere behov for forklaringer
- ✅ Standardisere workflows
- ✅ Genbruge best practices

Dette sparer tokens og giver hurtigere, bedre svar.

## 🆕 Opret Ny Skill

Template til ny skill:

```markdown
# Skill: [Navn]

[Kort beskrivelse af hvad denne skill hjælper med]

## Arbejdsmetode
[Step-by-step approach]

## Best Practices
[Key principles og guidelines]

## Værktøjer
[Tools, libraries, commands]

## Output Format
[Hvordan resultatet skal præsenteres]

## Eksempler
[Konkrete eksempler]
```

Gem i `/skills/[navn].md` og opdater denne README.
