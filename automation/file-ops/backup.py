#!/usr/bin/env python3
"""
Backup Script - Simpel backup af vigtige mapper

Laver timestamped backup af specificerede mapper til backup destination.

Usage:
    python backup.py [--destination /path/to/backup]
    
Example:
    python backup.py --destination ~/Backups
    
Author: Lars
Date: 2026-04-25
"""

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional


# Mapper der skal backuppes (tilpas efter behov)
DEFAULT_SOURCES = [
    "~/Documents",
    "~/repos",
]

# Standard backup destination (tilpas efter behov)
DEFAULT_DESTINATION = "~/Backups"


def create_backup(
    sources: List[Path],
    destination: Path,
    verbose: bool = False
) -> bool:
    """
    Create backup of source directories.
    
    Args:
        sources: List of source directories to backup
        destination: Backup destination directory
        verbose: Print detailed progress
        
    Returns:
        True if successful, False otherwise
    """
    # Create timestamped backup folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = destination / f"backup_{timestamp}"
    
    try:
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        if verbose:
            print(f"Creating backup in: {backup_dir}")
        
        for source in sources:
            if not source.exists():
                print(f"Warning: Source {source} does not exist, skipping")
                continue
            
            target = backup_dir / source.name
            
            if verbose:
                print(f"Backing up: {source} -> {target}")
            
            if source.is_dir():
                shutil.copytree(source, target, symlinks=True)
            else:
                shutil.copy2(source, target)
        
        print(f"\n✓ Backup completed successfully!")
        print(f"Location: {backup_dir}")
        
        # Calculate backup size
        total_size = sum(
            f.stat().st_size 
            for f in backup_dir.rglob('*') 
            if f.is_file()
        )
        size_mb = total_size / (1024 * 1024)
        print(f"Size: {size_mb:.2f} MB")
        
        return True
        
    except Exception as e:
        print(f"Error creating backup: {e}", file=sys.stderr)
        return False


def cleanup_old_backups(
    destination: Path,
    keep_count: int = 5,
    verbose: bool = False
) -> None:
    """
    Remove old backups, keeping only the most recent.
    
    Args:
        destination: Backup directory
        keep_count: Number of recent backups to keep
        verbose: Print detailed progress
    """
    if not destination.exists():
        return
    
    # Find all backup directories
    backups = sorted(
        [d for d in destination.iterdir() if d.is_dir() and d.name.startswith("backup_")],
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )
    
    # Remove old backups
    for old_backup in backups[keep_count:]:
        if verbose:
            print(f"Removing old backup: {old_backup}")
        shutil.rmtree(old_backup)


def main(argv: Optional[List[str]] = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Backup important directories"
    )
    
    parser.add_argument(
        "-d", "--destination",
        type=str,
        default=DEFAULT_DESTINATION,
        help=f"Backup destination (default: {DEFAULT_DESTINATION})"
    )
    
    parser.add_argument(
        "-s", "--sources",
        type=str,
        nargs="+",
        help="Source directories to backup (overrides defaults)"
    )
    
    parser.add_argument(
        "-k", "--keep",
        type=int,
        default=5,
        help="Number of recent backups to keep (default: 5)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args(argv)
    
    # Prepare paths
    destination = Path(args.destination).expanduser().resolve()
    
    if args.sources:
        sources = [Path(s).expanduser().resolve() for s in args.sources]
    else:
        sources = [Path(s).expanduser().resolve() for s in DEFAULT_SOURCES]
    
    # Print configuration
    print("Backup Configuration:")
    print(f"  Destination: {destination}")
    print(f"  Sources:")
    for source in sources:
        print(f"    - {source}")
    print()
    
    # Create backup
    success = create_backup(sources, destination, args.verbose)
    
    if success:
        # Cleanup old backups
        cleanup_old_backups(destination, args.keep, args.verbose)
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
