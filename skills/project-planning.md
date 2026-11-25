# Skill: Projekt Planlægning

Du hjælper med at strukturere, planlægge og organisere projekter fra start til slut.

## Projekt Start Checklist

### 1. Definition
- [ ] Klar formålsbeskrivelse
- [ ] Succeskriterier defineret
- [ ] Scope afgrænset (hvad er IN/OUT)
- [ ] Deadlines identificeret

### 2. Setup
- [ ] Folder struktur oprettet
- [ ] README med projekt overview
- [ ] Git repository initialiseret
- [ ] Dependencies dokumenteret

### 3. Planlægning
- [ ] Break down i milestones
- [ ] Identificér dependencies
- [ ] Prioritér tasks
- [ ] Estimér tid (realistisk)

## Projekt Struktur Template

```
projekt-navn/
├── README.md              # Projekt overview
├── requirements.txt       # Python deps
├── package.json          # Node deps  
├── .gitignore            # Ignore rules
├── src/                  # Source code
│   ├── main.py
│   └── utils/
├── tests/                # Test files
├── docs/                 # Documentation
│   ├── architecture.md
│   └── api.md
├── config/               # Config files
└── scripts/              # Utility scripts
```

## Task Management

### Brug TODO System
```python
# TODO: Implement user authentication
# FIXME: Bug in data validation
# NOTE: Consider caching here
# HACK: Temporary workaround for API issue
```

### Milestone Tracking
Opdel projektet i 3-5 major milestones:
1. **Setup & Foundation** - Basic structure
2. **Core Features** - Main functionality
3. **Integration** - Connect components
4. **Polish** - UI/UX, performance
5. **Deploy** - Production ready

## Collaboration

Hvis du arbejder med andre:
- Klar git commit messages
- Pull request descriptions
- Code review process
- Communication plan

## Progress Reviews

Ugentligt/jævnligt check:
- Hvad er gjort? ✅
- Hvad mangler? 📝
- Blockers? 🚧
- Justeringer nødvendige? 🔄

## Project Memory

Gem projektspecifikke noter i:
- `/projects/[projekt-navn]/docs/decisions.md`
- `/projects/[projekt-navn]/docs/learnings.md`

Dette hjælper AI agenten med kontekst næste gang!
