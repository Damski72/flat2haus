# Python CLI Template

Template til Python command-line applikationer.

## Struktur

```
projekt-navn/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   └── utils/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── docs/
    └── usage.md
```

## main.py Template

```python
#!/usr/bin/env python3
"""
[Projekt Navn] - [Kort beskrivelse]

Author: Lars
Date: 2026-04-25
"""

import sys
from typing import Optional


def main(args: Optional[list[str]] = None) -> int:
    """Main entry point."""
    if args is None:
        args = sys.argv[1:]
    
    # Din logik her
    print("Hello from template!")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## cli.py Template (med argparse)

```python
"""Command-line interface."""

import argparse
from typing import Sequence, Optional


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser."""
    parser = argparse.ArgumentParser(
        description="[Beskrivelse af CLI tool]"
    )
    
    parser.add_argument(
        "input",
        help="Input file eller parameter"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output destination",
        default="output.txt"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)
    
    if args.verbose:
        print(f"Processing {args.input}...")
    
    # Din logik her
    
    return 0
```

## requirements.txt

```
# Core dependencies
click>=8.0.0  # Alternativ til argparse

# Development dependencies
pytest>=7.0.0
pytest-cov>=4.0.0
black>=23.0.0
ruff>=0.1.0
mypy>=1.0.0
```

## .gitignore

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

## Sådan Bruger Du

1. Kopier template til projects:
```bash
cp -r templates/python-cli projects/mit-projekt
cd projects/mit-projekt
```

2. Opret virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

3. Installer dependencies:
```bash
pip install -r requirements.txt
```

4. Tilpas kode og start udvikling!
