# Flat2Haus 

> From flat blueprints to 3D-printed models.

En guidet web-app (Human-in-the-Loop Wizard), der konverterer indscannede byggetegninger og plantegninger til printbare 3D-modeller (`.STL` / `.3MF`) med automatisk sikring af vægtykkelser.

## Workflow
1. **Upload & Billedrens:** Beskær og ret skæve scanninger op (OpenCV).
2. **Kalibrering:** Sæt et kendt mål på tegningen og vælg print-skala (f.eks. 1:100).
3. **2D Trace & Rettelser:** Tegn/ret vægge, vinduer og døre oven på tegningen (Konva.js).
4. **3D-generering & Print-sikring:** Ekstruder til 3D med automatisk minimumsvægtykkelse og tag-generator (`build123d`).
5. **Eksport:** Download printklar `.STL` eller `.3MF`.

## Lokal opsætning (Backend)
```bash
cd backend
pip install -r requirements.txt
python generate_floorpl# Lars' Personlige Arbejdsområde

Dette er mit strukturerede workspace til projekter, automatisering og AI-agent arbejde.

## 📁 Mappestruktur

- **skills/** - AI agent skills til forskellige arbejdstyper
- **projects/** - Aktive projekter
- **automation/** - Automatiseringsscripts og workflows
- **templates/** - Genbrugelige templates
- **docs/** - Dokumentation og notater

## 🤖 Sådan Bruger Du Skills

Skills er instruktioner til GitHub Copilot som optimerer token-forbrug og svarklariteter.

### Aktivér en Skill:
1. Åbn en skill-fil fra `skills/` mappen
2. Kopier indholdet
3. Brug `@workspace` mention med skill-instruktionerne

Eller reference skills direkte: `@workspace /skills/code-development.md`

## 💡 Tips til Effektiv Agent-brug

1. **Brug skills** - De er optimeret til at give agenten kontekst hurtigt
2. **Vær specifik** - Jo mere præcis din forespørgsel, jo bedre svar
3. **Husk kontekst** - Agenten lærer fra samtalen, men skills hjælper
4. **Genbrugelighed** - Gem ofte brugte kommandoer i automation/

## 🔄 Automatisering

Se [automation/README.md](automation/README.md) for guide til automatiseringsworkflows.

## 📝 Hukommelse & Kontekst

GitHub Copilot bruger memory-systemet til at huske dine præferencer på tværs af samtaler.
- Personlige præferencer gemmes automatisk
- Check `/memories/` for hvad der er gemt

---
*Opdateret: April 2026*



