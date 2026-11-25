#!/usr/bin/env python3
"""
File Organizer - Organiser downloads mappe efter filtype

Dette script flytter filer fra downloads til organiserede undermapper
baseret på filtyper (images, documents, videos, etc.)

Usage:
    python organize_downloads.py [downloads_path]
    
Example:
    python organize_downloads.py ~/Downloads
    
Author: Lars
Date: 2026-04-25
"""

import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List


# Fil type mappings
FILE_TYPES: Dict[str, List[str]] = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"],
    "Other": []  # Fallback for unknown types
}


def get_file_category(file_path: Path) -> str:
    """Determine category for file based on extension."""
    extension = file_path.suffix.lower()
    
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    
    return "Other"


def organize_directory(directory: Path, dry_run: bool = False) -> None:
    """
    Organize files in directory into subdirectories by type.
    
    Args:
        directory: Path to directory to organize
        dry_run: If True, only print what would happen
    """
    if not directory.exists():
        print(f"Error: Directory {directory} does not exist")
        return
    
    # Get all files (not directories)
    files = [f for f in directory.iterdir() if f.is_file()]
    
    if not files:
        print("No files to organize")
        return
    
    print(f"Found {len(files)} files to organize")
    
    moved_count = 0
    for file_path in files:
        category = get_file_category(file_path)
        target_dir = directory / category
        target_path = target_dir / file_path.name
        
        # Handle name conflicts
        counter = 1
        while target_path.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            target_path = target_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        
        if dry_run:
            print(f"Would move: {file_path.name} -> {category}/")
        else:
            # Create category directory if needed
            target_dir.mkdir(exist_ok=True)
            
            # Move file
            shutil.move(str(file_path), str(target_path))
            print(f"Moved: {file_path.name} -> {category}/")
            moved_count += 1
    
    if not dry_run:
        print(f"\nSuccessfully organized {moved_count} files")


def main(argv: List[str] = None) -> int:
    """Main entry point."""
    if argv is None:
        argv = sys.argv[1:]
    
    # Parse arguments
    if not argv:
        downloads_path = Path.home() / "Downloads"
    else:
        downloads_path = Path(argv[0]).expanduser()
    
    dry_run = "--dry-run" in argv or "-n" in argv
    
    print(f"Organizing: {downloads_path}")
    if dry_run:
        print("DRY RUN MODE - No files will be moved\n")
    
    try:
        organize_directory(downloads_path, dry_run=dry_run)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
