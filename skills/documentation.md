# Skill: Dokumentation

Du hjælper med at skabe klar, koncis og brugbar dokumentation.

## Dokumentations Typer

### README Files
```markdown
# Projekt Navn

Kort beskrivelse (1-2 linjer)

## Installation
Hvordan man kommer i gang

## Usage  
Eksempler på brug

## Konfiguration
Nødvendige settings

## Bidrag
Hvordan man bidrager (hvis relevant)
```

### Code Comments
- **Class/Function docstrings** - Hvad, ikke hvordan
- **Inline comments** - Kun for kompleks logik
- **TODOs** - Klar formatering: `# TODO: beskrivelse`

### API Documentation
- Endpoints og methods
- Request/response examples
- Authentication requirements
- Error codes og håndtering

### Guides & Tutorials
- Step-by-step instruktioner
- Screenshots/examples
- Troubleshooting sektion
- Related resources

## Principper

✅ **Klarhed** - Skriv for målgruppen
✅ **Konchesion** - Vær præcis, undgå fluff
✅ **Eksempler** - Vis, ikke kun fortæl
✅ **Struktur** - Logisk flow, god formatting
✅ **Opdatering** - Hold synkroniseret med kode

## Formater

- **Markdown** (.md) - Standard for de fleste docs
- **Docstrings** - In-code documentation
- **Comments** - Kode forklaringer
- **README** - Projekt overviews

## Quick Templates

Gem ofte brugte doc templates i `/templates/docs/`:
- `project-readme-template.md`
- `api-doc-template.md`
- `guide-template.md`
- `changelog-template.md`

## Anti-Patterns

❌ Over-documentation af selvforklarende kode
❌ Forældet dokumentation (værre end ingen)
❌ Copy-paste fra kode som "dokumentation"
❌ Manglende eksempler
