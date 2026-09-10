# FitFlow UI Analysis

Statistical comparison of four FitFlow interface designs to find which one lets users start a workout the fastest.

## Designs Tested
| Design | Type              |
|--------|-------------------|
| A      | Traditional Dropdown |
| B      | Visual Grid       |
| C      | Search Bar        |
| D      | Personalized Feed |

## Method
- One-Way ANOVA
- Tukey’s HSD post-hoc test
- Effect size (η²)

## Files
- `ANOVA.ipynb` – full analysis notebook
- `anova_testing.py` – standalone script

## Setup
```bash
pip install -r requirements.txt
```
## Run

```bash
python anova_testing.py
```
## License

This project is licensed under the [MIT License](LICENSE).
