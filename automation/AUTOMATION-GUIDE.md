# Automation Scripts

Klar-til-brug automation scripts til almindelige opgaver.

## 📁 Fil Operationer (/file-ops/)

### organize_downloads.py
Organiser downloads mappe automatisk efter filtype.

**Usage:**
```bash
# Organiser standard Downloads mappe
python automation/file-ops/organize_downloads.py

# Organiser specifik mappe
python automation/file-ops/organize_downloads.py ~/Downloads

# Dry run (se hvad der ville ske)
python automation/file-ops/organize_downloads.py --dry-run
```

**Filtyper:**
- Images → .jpg, .png, .gif, etc.
- Documents → .pdf, .doc, .txt, etc.
- Videos → .mp4, .mov, .mkv, etc.
- Audio → .mp3, .wav, etc.
- Archives → .zip, .rar, .7z, etc.
- Code → .py, .js, .html, etc.

### backup.py
Lav timestamped backups af vigtige mapper.

**Usage:**
```bash
# Standard backup
python automation/file-ops/backup.py

# Custom destination
python automation/file-ops/backup.py --destination ~/MyBackups

# Custom sources
python automation/file-ops/backup.py --sources ~/Documents ~/repos

# Verbose output
python automation/file-ops/backup.py --verbose

# Behold flere backups (standard er 5)
python automation/file-ops/backup.py --keep 10
```

**Features:**
- Timestamped backup folders
- Automatisk cleanup af gamle backups
- Size reporting
- Handles filkonvergens automatisk

## 🚀 Sådan Kommer Du I Gang

### 1. Gør Scripts Executable
```bash
chmod +x automation/file-ops/*.py
```

### 2. Test Scripts
```bash
# Test organize_downloads i dry-run mode
python automation/file-ops/organize_downloads.py --dry-run

# Test backup
python automation/file-ops/backup.py --verbose
```

### 3. Tilpas til Dine Behov

**organize_downloads.py:**
Rediger `FILE_TYPES` dictionary for at tilføje/fjerne filtyper.

**backup.py:**
Rediger `DEFAULT_SOURCES` og `DEFAULT_DESTINATION` konstanter.

### 4. Automatiser med Cron (macOS/Linux)

```bash
# Åbn crontab editor
crontab -e

# Tilføj job (eksempel: daglig backup kl 02:00)
0 2 * * * cd ~/repos && python automation/file-ops/backup.py

# Eksempel: organiser downloads hver dag kl 18:00
0 18 * * * cd ~/repos && python automation/file-ops/organize_downloads.py
```

## 💡 Idéer til Flere Scripts

- **cleanup.py** - Slet gamle/store filer
- **sync_folders.py** - Synkroniser to mapper
- **batch_rename.py** - Batch omdøb filer
- **compress_images.py** - Komprimér billeder
- **duplicate_finder.py** - Find duplikerede filer
- **git_backup.py** - Backup alle git repos

Bed GitHub Copilot om at hjælpe:
```
@workspace Brug /skills/automation.md
Lav et script til at [din opgave]
```

## 🔧 Dependencies

Mest scripts bruger kun Python standard library, men nogle kan kræve:

```bash
# For mere avancerede scripts
pip install click      # CLI framework
pip install rich       # Pretty output
pip install watchdog   # File system monitoring
```

## 📝 Best Practices

1. **Test først** - Brug --dry-run eller test på copies
2. **Backup kritiske data** - Før du kører destruktive operationer
3. **Log alt** - Behold record af hvad scripts har gjort
4. **Error handling** - Scripts skal håndtere fejl gracefully
5. **Dokumentér** - Klar usage i toppen af hvert script

## 🆘 Troubleshooting

**Permission denied:**
```bash
chmod +x script_name.py
```

**Module not found:**
```bash
pip install [module_name]
```

**Script ikke virker:**
- Check Python version (brug Python 3.8+)
- Læs error message carefully
- Test i verbose mode
- Bed GitHub Copilot om hjælp med debugging
