# Skill: Data Analyse

Du hjælper med at analysere, visualisere og udtrække indsigt fra data.

## Workflow

1. **Forstå dataen** - Struktur, typer, kvalitet
2. **Rens dataen** - Håndter missing values, outliers
3. **Analysér** - Statistik, patterns, correlations
4. **Visualisér** - Graphs, charts, dashboards
5. **Konkludér** - Actionable insights

## Værktøjer

### Python Stack
```python
import pandas as pd           # Data manipulation
import numpy as np           # Numerical computing
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns        # Statistical viz
```

### Typiske Opgaver

**Data Loading**
```python
# CSV, Excel, JSON, SQL
df = pd.read_csv('data.csv')
```

**Exploration**
```python
df.info()           # Structure
df.describe()       # Statistics
df.isnull().sum()   # Missing values
```

**Cleaning**
```python
df.dropna()         # Remove nulls
df.fillna(value)    # Fill nulls
df.drop_duplicates() # Remove dupes
```

**Analysis**
```python
df.groupby('col').agg({'col2': 'mean'})
df.corr()           # Correlations
```

## Output Format

### Notebooks
- Jupyter notebooks i `/projects/data-analysis/`
- Clear markdown cells med forklaringer
- Reproducible code
- Inline visualizations

### Reports
- Summary statistics
- Key findings
- Visualizations
- Recommendations

### Scripts
- Reusable analysis scripts i `/automation/data/`
- Configurable parameters
- Export results (CSV, JSON, plots)

## Best Practices

✅ **Version data** - Track data sources og versions
✅ **Document assumptions** - Note decisions og rationale
✅ **Validate results** - Sanity checks
✅ **Reproducibility** - Same input = same output
✅ **Visualize early** - Plots reveal patterns

## Common Pitfalls

❌ Not checking data quality først
❌ Ignoring missing values
❌ Overcomplicated analysis
❌ Cherry-picking results
❌ Poor visualization choices
